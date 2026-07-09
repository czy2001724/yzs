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
"""
from __future__ import annotations

import os
import time
from typing import Callable, List, Optional

from . import image_match


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
    ) -> None:
        self.log_cb = log_cb or (lambda msg: None)
        self.step_cb = step_cb or (lambda i, total: None)
        self._paused = False
        self._stopped = False

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

    def _do_move(self, pyautogui, s):
        x, y = int(s["x"]), int(s["y"])
        dur = float(s.get("duration", 0.3))
        self.log(f"移动到 ({x}, {y})")
        pyautogui.moveTo(x, y, duration=dur, tween=pyautogui.easeInOutQuad)

    def _do_click(self, pyautogui, s):
        x, y = int(s["x"]), int(s["y"])
        button = s.get("button", "left")
        clicks = int(s.get("clicks", 1))
        dur = float(s.get("duration", 0.25))
        self.log(f"点击 ({x}, {y}) 按键={button} 次数={clicks}")
        pyautogui.moveTo(x, y, duration=dur, tween=pyautogui.easeInOutQuad)
        pyautogui.click(x, y, clicks=clicks, button=button)

    def _do_double_click(self, pyautogui, s):
        x, y = int(s["x"]), int(s["y"])
        self.log(f"双击 ({x}, {y})")
        pyautogui.moveTo(x, y, duration=float(s.get("duration", 0.25)),
                         tween=pyautogui.easeInOutQuad)
        pyautogui.doubleClick(x, y)

    def _do_right_click(self, pyautogui, s):
        x, y = int(s["x"]), int(s["y"])
        self.log(f"右键 ({x}, {y})")
        pyautogui.moveTo(x, y, duration=float(s.get("duration", 0.25)),
                         tween=pyautogui.easeInOutQuad)
        pyautogui.click(x, y, button="right")

    def _do_drag(self, pyautogui, s):
        x1, y1 = int(s["x1"]), int(s["y1"])
        x2, y2 = int(s["x2"]), int(s["y2"])
        dur = float(s.get("duration", 0.5))
        self.log(f"拖拽 ({x1},{y1}) -> ({x2},{y2})")
        pyautogui.moveTo(x1, y1, duration=0.2)
        pyautogui.dragTo(x2, y2, duration=dur, button="left")

    def _do_scroll(self, pyautogui, s):
        amount = int(s.get("amount", -300))
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
