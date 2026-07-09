"""PyAutoGUI 自动化引擎。

把「步骤列表」（普通 dict）翻译成真实的鼠标 / 键盘 / 图像操作。
支持在后台 QThread 中运行，可暂停 / 停止 / 循环，并通过信号回报日志与进度。

步骤（step）是一个 dict，字段 type 决定动作：

    {"type": "move",        "x", "y", "duration"}
    {"type": "click",       "x", "y", "button", "clicks"}
    {"type": "double_click","x", "y"}
    {"type": "right_click", "x", "y"}
    {"type": "drag",        "x1", "y1", "x2", "y2", "duration"}
    {"type": "scroll",      "amount"}
    {"type": "type",        "text", "interval"}
    {"type": "key",         "key"}
    {"type": "hotkey",      "keys": ["ctrl", "c"]}
    {"type": "wait",        "seconds"}
    {"type": "screenshot",  "path", "region"}
    {"type": "find_image",  "template", "confidence", "region", "click"}
    {"type": "window_find", "title", "focus"}
    {"type": "window_move", "x", "y", "width", "height"}
"""
from __future__ import annotations

import os
import random
import time
from dataclasses import dataclass
from typing import Callable, List, Optional

from . import image_match
from . import window as _win


@dataclass
class HumanizeConfig:
    """拟人化配置：让模拟操作更像真人，降低被反作弊系统识别的风险。

    建议在游戏测试环境下启用。

    Attributes:
        enabled: 是否启用拟人化
        inter_step_min: 步骤间随机等待最小秒数
        inter_step_max: 步骤间随机等待最大秒数
        click_jitter: 点击位置随机偏移像素范围（±N），0 = 不偏移
        speed_vary_pct: 移动耗时的随机变化比例（0.0~1.0），0.2 表示 ±20%
        scroll_vary_pct: 滚轮量的随机变化比例（0.0~1.0）
        bezier_deviation: 曲线偏移量（px），路线偏离直线的最大像素距离，0 = 走直线
        bezier_points: 曲线采样点数，越多越平滑但也越慢
        overshoot: 终点过冲/回拉像素范围，0 = 不过冲
    """
    enabled: bool = True
    inter_step_min: float = 0.05
    inter_step_max: float = 0.25
    click_jitter: int = 2
    speed_vary_pct: float = 0.15
    scroll_vary_pct: float = 0.1
    bezier_deviation: int = 30
    bezier_points: int = 40
    overshoot: int = 4


def _lazy_pyautogui():
    """延迟导入 pyautogui（导入时会尝试连接显示器，放到需要时再做）。"""
    import pyautogui
    pyautogui.FAILSAFE = True   # 鼠标甩到左上角紧急停止
    pyautogui.PAUSE = 0.0
    return pyautogui


class StopRequested(Exception):
    """内部信号：请求停止执行。"""


class AutomationEngine:
    """无 GUI 依赖的核心引擎，可被 GUI worker 或脚本直接调用。"""

    def __init__(
        self,
        log_cb: Optional[Callable[[str], None]] = None,
        step_cb: Optional[Callable[[int, int], None]] = None,
        humanize: Optional[HumanizeConfig] = None,
    ) -> None:
        self.log_cb = log_cb or (lambda msg: None)
        self.step_cb = step_cb or (lambda i, total: None)
        self.humanize = humanize or HumanizeConfig()
        self._paused = False
        self._stopped = False
        self._last_hwnd = 0

    # ----------------------------- 控制 ----------------------------------- #
    def pause(self) -> None:
        self._paused = True
        self.log("⏸ 已暂停")

    def resume(self) -> None:
        self._paused = False
        self.log("▶ 继续")

    def stop(self) -> None:
        self._stopped = True

    def reset(self) -> None:
        self._paused = False
        self._stopped = False

    def log(self, msg: str) -> None:
        self.log_cb(msg)

    def _checkpoint(self) -> None:
        """在每个动作前检查暂停 / 停止。"""
        while self._paused and not self._stopped:
            time.sleep(0.05)
        if self._stopped:
            raise StopRequested()

    # ----------------------------- 执行 ----------------------------------- #
    def run(self, steps: List[dict], loops: int = 1) -> bool:
        """执行步骤列表，可循环 loops 次（loops<=0 表示无限循环）。

        返回 True 表示正常跑完，False 表示中途停止。
        """
        self.reset()
        pyautogui = _lazy_pyautogui()
        loop_idx = 0
        try:
            while not self._stopped:
                loop_idx += 1
                self.log(f"—— 第 {loop_idx} 轮 ——")
                total = len(steps)
                for i, step in enumerate(steps, 1):
                    self._checkpoint()
                    self.step_cb(i, total)
                    self._execute(pyautogui, step)
                    if self.humanize.enabled:
                        delay = random.uniform(
                            self.humanize.inter_step_min,
                            self.humanize.inter_step_max,
                        )
                        time.sleep(delay)
                if loops > 0 and loop_idx >= loops:
                    break
            self.log("✅ 执行完成")
            return True
        except StopRequested:
            self.log("⏹ 已停止")
            return False
        except Exception as exc:  # pragma: no cover - 运行期异常
            self.log(f"❌ 出错：{exc}")
            return False

    # ----------------------------- 单步 ----------------------------------- #
    def _execute(self, pyautogui, step: dict) -> None:
        t = step.get("type")
        handler = getattr(self, f"_do_{t}", None)
        if handler is None:
            self.log(f"⚠ 未知步骤类型：{t}")
            return
        handler(pyautogui, step)

    def _jit(self, x: int, y: int) -> tuple:
        """拟人化：对坐标施加随机像素偏移。"""
        if not self.humanize.enabled or self.humanize.click_jitter <= 0:
            return x, y
        j = self.humanize.click_jitter
        return x + random.randint(-j, j), y + random.randint(-j, j)

    def _vary_dur(self, dur: float) -> float:
        """拟人化：随机变化移动耗时。"""
        if not self.humanize.enabled:
            return dur
        pct = self.humanize.speed_vary_pct
        return max(0.02, dur * (1.0 + random.uniform(-pct, pct)))

    def _vary_scroll(self, amount: int) -> int:
        """拟人化：随机变化滚轮量。"""
        if not self.humanize.enabled:
            return amount
        pct = self.humanize.scroll_vary_pct
        return int(amount * (1.0 + random.uniform(-pct, pct)))

    def _bezier_curve(self, x1: int, y1: int, x2: int, y2: int) -> list:
        """生成贝塞尔曲线路径点列表。

        起点 (x1,y1) 到终点 (x2,y2)，中间插入两个随机偏移控制点。
        返回 [(x, y), ...] 均匀采样点列表。
        """
        dev = self.humanize.bezier_deviation
        n = max(self.humanize.bezier_points, 5)
        dx, dy = x2 - x1, y2 - y1
        dist = (dx * dx + dy * dy) ** 0.5
        if dist < 5 or dev <= 0:
            return [(x2, y2)]

        # 垂直于直线的单位方向
        if abs(dx) > abs(dy):
            perp_x = -dy / abs(dx) if abs(dx) > 1e-6 else 0
            perp_y = 1.0 if dx >= 0 else -1.0
        else:
            perp_x = 1.0 if dy >= 0 else -1.0
            perp_y = dx / abs(dy) if abs(dy) > 1e-6 else 0
        plen = (perp_x * perp_x + perp_y * perp_y) ** 0.5
        perp_x, perp_y = perp_x / plen, perp_y / plen

        # 两个控制点：沿直线 1/3 和 2/3 处，向两侧偏移
        c1_off = int(dev * (0.3 + random.random() * 0.7))  # 30%-100% of max deviation
        c2_off = int(dev * (0.3 + random.random() * 0.7))
        c1_sign = 1 if random.random() > 0.5 else -1
        c2_sign = -c1_sign if random.random() > 0.3 else c1_sign

        cx1 = int(x1 + dx * 0.33 + perp_x * c1_off * c1_sign)
        cy1 = int(y1 + dy * 0.33 + perp_y * c1_off * c1_sign)
        cx2 = int(x1 + dx * 0.66 + perp_x * c2_off * c2_sign)
        cy2 = int(y1 + dy * 0.66 + perp_y * c2_off * c2_sign)

        # 三次贝塞尔: P(t) = (1-t)^3*P0 + 3(1-t)^2*t*P1 + 3(1-t)*t^2*P2 + t^3*P3
        points = []
        for i in range(n):
            t = i / (n - 1)
            mt = 1 - t
            x = int(mt**3 * x1 + 3 * mt**2 * t * cx1 + 3 * mt * t**2 * cx2 + t**3 * x2)
            y = int(mt**3 * y1 + 3 * mt**2 * t * cy1 + 3 * mt * t**2 * cy2 + t**3 * y2)
            # 对中间点添加微小抖动
            if 0 < i < n - 1 and self.humanize.click_jitter > 0:
                j = self.humanize.click_jitter // 2 + 1
                x += random.randint(-j, j)
                y += random.randint(-j, j)
            points.append((x, y))
        return points

    def _move_human(self, pyautogui, x: int, y: int, dur: float) -> None:
        """拟人移动：沿贝塞尔曲线 + 轻微过冲回拉。"""
        cur_x, cur_y = pyautogui.position()
        overshoot = self.humanize.overshoot

        target_x, target_y = x, y
        if overshoot > 0:
            dx, dy = target_x - cur_x, target_y - cur_y
            dist = (dx * dx + dy * dy) ** 0.5
            if dist > 10:
                os_amt = min(overshoot, int(dist * 0.08))
                os_x = int(os_amt * dx / dist) if dist > 0 else 0
                os_y = int(os_amt * dy / dist) if dist > 0 else 0
                target_x = x + os_x + random.randint(-2, 2)
                target_y = y + os_y + random.randint(-2, 2)

        curve = self._bezier_curve(cur_x, cur_y, target_x, target_y)
        n = len(curve)
        for i, (px, py) in enumerate(curve):
            self._checkpoint()
            seg_dur = dur * (0.5 + random.random()) / n
            pyautogui.moveTo(px, py, duration=seg_dur)

        if overshoot > 0 and target_x != x and target_y != y:
            curve2 = self._bezier_curve(target_x, target_y, x, y)
            n2 = len(curve2)
            for i, (px, py) in enumerate(curve2):
                self._checkpoint()
                seg_dur = dur * 0.3 / n2
                pyautogui.moveTo(px, py, duration=seg_dur)

    def _do_move(self, pyautogui, s):
        x, y = self._jit(int(s["x"]), int(s["y"]))
        dur = self._vary_dur(float(s.get("duration", 0.3)))
        self.log(f"移动到 ({x}, {y}) 耗时={dur:.2f}s")
        self._move_human(pyautogui, x, y, dur)

    def _do_click(self, pyautogui, s):
        x, y = self._jit(int(s["x"]), int(s["y"]))
        button = s.get("button", "left")
        clicks = int(s.get("clicks", 1))
        dur = self._vary_dur(float(s.get("duration", 0.25)))
        self.log(f"点击 ({x}, {y}) 按键={button} 次数={clicks}")
        self._move_human(pyautogui, x, y, dur)
        pyautogui.click(x, y, clicks=clicks, button=button)

    def _do_double_click(self, pyautogui, s):
        x, y = self._jit(int(s["x"]), int(s["y"]))
        dur = self._vary_dur(float(s.get("duration", 0.25)))
        self.log(f"双击 ({x}, {y})")
        self._move_human(pyautogui, x, y, dur)
        pyautogui.doubleClick(x, y)

    def _do_right_click(self, pyautogui, s):
        x, y = self._jit(int(s["x"]), int(s["y"]))
        dur = self._vary_dur(float(s.get("duration", 0.25)))
        self.log(f"右键 ({x}, {y})")
        self._move_human(pyautogui, x, y, dur)
        pyautogui.click(x, y, button="right")

    def _do_drag(self, pyautogui, s):
        x1, y1 = self._jit(int(s["x1"]), int(s["y1"]))
        x2, y2 = self._jit(int(s["x2"]), int(s["y2"]))
        dur = self._vary_dur(float(s.get("duration", 0.5)))
        self.log(f"拖拽 ({x1},{y1}) -> ({x2},{y2})")
        self._move_human(pyautogui, x1, y1, 0.15)
        pyautogui.dragTo(x2, y2, duration=dur, button="left")

    def _do_scroll(self, pyautogui, s):
        amount = self._vary_scroll(int(s.get("amount", -300)))
        self.log(f"滚轮 {amount}")
        pyautogui.scroll(amount)

    def _do_type(self, pyautogui, s):
        text = s.get("text", "")
        interval = float(s.get("interval", 0.02))
        self.log(f"输入文本：{text!r}")
        pyautogui.typewrite(text, interval=interval)

    def _do_key(self, pyautogui, s):
        key = s.get("key", "")
        self.log(f"按键 {key}")
        pyautogui.press(key)

    def _do_hotkey(self, pyautogui, s):
        keys = s.get("keys", [])
        self.log(f"组合键 {'+'.join(keys)}")
        pyautogui.hotkey(*keys)

    def _do_wait(self, pyautogui, s):
        seconds = float(s.get("seconds", 1.0))
        self.log(f"等待 {seconds}s")
        end = time.time() + seconds
        while time.time() < end:
            self._checkpoint()
            time.sleep(min(0.05, max(0.0, end - time.time())))

    def _do_screenshot(self, pyautogui, s):
        path = s.get("path") or f"screenshot_{int(time.time())}.png"
        region = s.get("region")
        image_match.save_region_screenshot(path, tuple(region) if region else None)
        self.log(f"截图已保存：{path}")

    def _do_find_image(self, pyautogui, s):
        template = s["template"]
        confidence = float(s.get("confidence", 0.8))
        region = s.get("region")
        do_click = bool(s.get("click", True))
        if not os.path.isfile(template):
            self.log(f"⚠ 模板不存在：{template}")
            return
        result = image_match.locate_on_screen(
            template, tuple(region) if region else None, confidence=confidence
        )
        if result.found:
            cx, cy = result.center
            self.log(f"找到图像（相似度 {result.confidence:.2f}）于 ({cx}, {cy})")
            if do_click:
                pyautogui.moveTo(cx, cy, duration=0.25, tween=pyautogui.easeInOutQuad)
                pyautogui.click(cx, cy)
        else:
            self.log(f"未找到图像（最高相似度 {result.confidence:.2f}）")

    def _do_window_find(self, pyautogui, s):
        title = s.get("title", "")
        focus = bool(s.get("focus", True))
        info = _win.find_window(title=title)
        if info:
            self._last_hwnd = info.hwnd
            self.log(f"找到窗口「{info.title}」 位置=({info.x},{info.y}) "
                     f"大小={info.width}x{info.height}")
            if focus:
                _win.focus_window(info.hwnd)
                self.log("窗口已置顶")
        else:
            self.log(f"⚠ 未找到包含「{title}」的窗口")

    def _do_window_move(self, pyautogui, s):
        hwnd = self._last_hwnd or _win.get_foreground_window()
        if not hwnd:
            self.log("⚠ 没有可操作的窗口，请先执行「找到窗口」步骤")
            return
        x = int(s.get("x", 0))
        y = int(s.get("y", 0))
        w = int(s.get("width", 0))
        h = int(s.get("height", 0))
        _win.move_window(hwnd, x, y, w, h)
        self.log(f"窗口已移到 ({x},{y})"
                 + (f" 大小 {w}x{h}" if w > 0 and h > 0 else ""))
