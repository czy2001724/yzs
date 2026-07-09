# 6号自动化助手 · 本地面板

一个基于 **PyQt5** 的桌面自动化小程序：用可视化面板搭建「鼠标 / 键盘 / 图像识别」工作流，
由 **PyAutoGUI** 引擎执行，支持全局热键和全局输入录制。

> 面向 Windows 使用（全局钩子、抓屏、坐标取色体验最佳）；在 Linux/macOS 上界面可正常打开，部分底层功能依赖平台。

## ✨ 功能

| 模块 | 技术 | 说明 |
|------|------|------|
| GUI 本地面板 | PyQt5 | 动作库、步骤列表、日志、实时坐标/取色、运行控制 |
| 自动化引擎 | PyAutoGUI | 鼠标移动/点击/拖拽/滚轮、键盘输入/组合键、丝滑移动 |
| 屏幕截图 | Pillow (ImageGrab) | 全屏 / 区域截图，保存模板图 |
| 图像识别定位 | NumPy | 纯 NumPy 归一化互相关(NCC)模板匹配，找到即可点击（装了 OpenCV 会自动加速） |
| 全局热键 | keyboard | F9 运行 · F10 停止 · F11 暂停 |
| 全局输入 Hook | pywin32 / Win32 底层钩子 | `WH_MOUSE_LL` / `WH_KEYBOARD_LL` 录制全局点击与按键为步骤 |

## 📦 安装

```bash
pip install -r requirements.txt
```

## 🚀 运行

```bash
python main.py
```

## 🧩 使用流程

1. 左侧「动作库」点选动作类型，在弹窗里填参数，加入中间的步骤列表。
2. 用「上移 / 下移 / 编辑 / 删除」整理步骤，或「💾 保存 / 📂 加载」把工作流存成 JSON。
3. 右侧设置循环次数，点 **▶ 运行**（或按 **F9**）。运行中可 **F11 暂停 / F10 停止**。
4. 需要图像识别时，先用 **📷 抓取模板图** 存一张模板 PNG，再添加「图像识别定位」步骤引用它。
5. **● 开始录制**（仅 Windows）可把你真实的点击 / 按键记录成步骤。

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

## 📁 项目结构

```
main.py                 入口，启动 GUI
automation/
  engine.py             PyAutoGUI 执行引擎（步骤 -> 真实操作，可暂停/停止/循环）
  image_match.py        Pillow 抓屏 + NumPy NCC 模板匹配
  hooks.py              全局热键(keyboard) + Win32 底层输入录制
gui/
  main_window.py        PyQt5 主窗口
  step_dialogs.py       各动作类型的参数编辑对话框
requirements.txt
```
