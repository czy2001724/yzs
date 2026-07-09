# QQ · 桌面自动化面板

一个基于 **PyQt5** 的桌面自动化小程序：用可视化面板搭建「鼠标 / 键盘 / 图像识别」工作流，
由 **PyAutoGUI** 引擎执行，支持全局热键和全局输入录制。

> 面向 Windows 使用（全局钩子、抓屏、坐标取色体验最佳）；在 Linux/macOS 上界面可正常打开，部分底层功能依赖平台。

## ✨ 功能

| 模块 | 技术 | 说明 |
|------|------|------|
| GUI 本地面板 | PyQt5 | 动作库、步骤列表、日志、实时坐标/取色、运行控制 |
| 自动化引擎 | PyAutoGUI | 鼠标移动/点击/拖拽/滚轮、键盘输入/组合键、**贝塞尔曲线拟人轨迹** |
| 拟人化引擎 | HumanizeConfig | 贝塞尔曲线移动、随机间隔、坐标抖动、过冲回拉、速度变化 |
| 屏幕截图 | Pillow (ImageGrab) | 全屏 / 区域截图，保存模板图 |
| 图像识别定位 | NumPy / OpenCV(可选) | 纯 NumPy NCC 模板匹配，找到即可点击/执行后续操作，支持循环等待 |
| 全局热键 | RegisterHotKey (Win32 API) | F9 运行 · F10 停止 · F11 暂停，**无低级钩子，反作弊安全** |
| 全局输入录制 | pywin32 / Win32 底层钩子 | `WH_MOUSE_LL` / `WH_KEYBOARD_LL` 录制全局点击与按键为步骤（⚠ 含反作弊风险） |

## 🛡️ 反作弊安全

本工具针对**逆战未来**等有反作弊保护的游戏测试场景进行了专项改造：

| 功能 | 原理 | 反作弊风险 |
|------|------|------------|
| 全局热键 (F9/F10/F11) | Win32 `RegisterHotKey` API，无钩子 | 安全 |
| 拟人化鼠标轨迹 | 三次贝塞尔曲线 + 过冲回拉 + 坐标抖动 | 中等（最终仍是 SendInput） |
| 步骤间随机延时 | 50~250ms 随机间隔 | 降低风险 |
| 像素取色 | GDI `GetPixel`，面板可一键关闭 | 关闭后安全 |
| 全局输入录制 | `WH_MOUSE_LL` / `WH_KEYBOARD_LL` 低级钩子 | **高危，使用时弹窗警告** |
| 全屏截图 | `ImageGrab.grab()` | 中等 |

> **拟人化设置**位于右侧面板 → 「👤 拟人化 · 反作弊」区块：
> - 坐标抖动：点击位置 ±N px 随机偏移
> - 轨迹偏移：贝塞尔曲线偏离直线最大像素距离（0 = 走直线）
> - 过冲幅度：到达终点略微超过再回拉，模拟手抖矫正
> - 像素取色：可关闭 `GetPixel` 避免触发反作弊

## 📦 安装

```bash
pip install -r requirements.txt
```

## 🚀 运行

```bash
python main.py
```

任务栏显示 QQ 图标（需先运行 `python extract_qq_icon.py` 提取图标）：

```bash
python extract_qq_icon.py "你的QQ安装路径\Bin\QQ.exe"
```

## 🧩 使用流程

1. 左侧「动作库」点选动作类型，在弹窗里填参数，加入中间的步骤列表。
2. 用「上移 / 下移 / 编辑 / 删除」整理步骤，或「💾 保存 / 📂 加载」把工作流存成 JSON。
3. 右侧设置循环次数，点 **▶ 运行**（或按 **F9**）。运行中可 **F11 暂停 / F10 停止**。
4. 需要图像识别时，先用 **📷 抓取模板图** 存一张模板 PNG，再添加「图像识别定位」步骤引用它。
5. **● 开始录制**（仅 Windows）可把你真实的点击 / 按键记录成步骤。
6. 循环次数设为 **0**（无限循环），配合 `find_image` 可实现"等待识别到图标后执行操作"。

> ⚠️ 安全：把鼠标快速甩到屏幕**左上角**可触发 PyAutoGUI 紧急停止。

## 步骤格式（workflow.json）

```json
{
  "steps": [
    {"type": "click", "x": 100, "y": 200, "button": "left", "clicks": 1},
    {"type": "type", "text": "hello", "interval": 0.02},
    {"type": "wait", "seconds": 1.0},
    {"type": "find_image", "template": "btn.png", "confidence": 0.85, "click": true}
  ]
}
```

支持的 `type`：`move` `click` `double_click` `right_click` `drag` `scroll`
`type` `key` `hotkey` `wait` `screenshot` `find_image`。

## HumanizeConfig 参数

在代码中可自定义拟人化行为：

```python
from automation import HumanizeConfig

config = HumanizeConfig(
    enabled=True,              # 启用拟人化
    inter_step_min=0.05,       # 步骤间最短延时(s)
    inter_step_max=0.25,       # 步骤间最长延时(s)
    click_jitter=2,            # 点击位置随机偏移(±px)
    speed_vary_pct=0.15,       # 移动速度随机变化(±15%)
    scroll_vary_pct=0.1,       # 滚轮量随机变化(±10%)
    bezier_deviation=30,       # 贝塞尔曲线偏离直线距离(px)
    bezier_points=40,          # 曲线采样点数
    overshoot=4,               # 终点过冲回拉幅度(px)
)
```

## 📁 项目结构

```
main.py                 入口，启动 GUI
extract_qq_icon.py      从 QQ.exe 提取任务栏图标
automation/
  engine.py             PyAutoGUI 执行引擎 + 贝塞尔曲线拟人化
  image_match.py        Pillow 抓屏 + NumPy NCC 模板匹配
  hooks.py              Win32 底层输入录制
  pointer.py            实时坐标/取色（取色可全局关闭）
gui/
  main_window.py        PyQt5 主窗口
  step_dialogs.py       各动作类型的参数编辑对话框
  hotkeys.py            RegisterHotKey 热键管理器（无钩子）
  theme.py              深色主题 QSS
requirements.txt
```
