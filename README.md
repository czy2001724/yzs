# 6号自动化助手

Windows RPA 桌面自动化工具 — 可视化流程编辑器 + 图像识别 + 键鼠模拟。

##  项目状态

此代码通过逆向工程从 PyArmor 9.2.3 Pro 保护的 PyInstaller 程序中提取重构。

| 模块 | 文件 | 状态 |
|------|------|------|
| 流程编辑器 | `editor/` | **100% 原始源码** |
| 自动化引擎 | `src/automation.py` | 重构（函数签名+字符串完整） |
| 主程序 GUI | `src/main_pyqt_v3.py` | 重构（115个函数结构完整） |
| 安全模块 | `src/security.py` | 重构（含完整反检测逻辑） |
| 激活模块 | `src/activation.py` | 重构（含 RSA 公钥+HMAC） |
| Web编辑器 | `src/web_server.py` | 重构（含 Flask API 路由） |
| 反编译详情 | `docs/FINAL_DISASSEMBLY/` | 27个 .dis 字节码反汇编 |
| 离线启动器 | `启动器_离线版.py` | 绕过验证的直接启动 |

## 功能

- **可视化流程编辑器** — 拖拽式操作卡片，支持鼠标/键盘/图像识别/窗口操作
- **图像识别** — OpenCV 多尺度匹配，支持不同 DPI/缩放
- **键鼠模拟** — PyAutoGUI + 人类化随机延迟
- **迷你模式** — 执行时缩小为浮动小窗
- **推送通知** — 截图识别后推送到微信

## 运行

### 方式1：离线启动器（需要 Python 3.13）

```bash
pip install pyqt5 opencv-python pyautogui keyboard numpy flask flask-cors requests
python 启动器_离线版.py
```

启动后编辑器在 `http://127.0.0.1:5001`

### 方式2：在完整提取目录下运行

```bash
# 需要先解包原始 exe (pyinstxtractor-ng)
cd 6hzsv2.23.exe_extracted
python 启动器_离线版.py
```

## 技术栈

- **GUI**: PyQt5
- **计算机视觉**: OpenCV (cv2)
- **自动化**: PyAutoGUI, Keyboard
- **Web编辑器**: Flask + Werkzeug
- **数据处理**: NumPy
- **打包**: PyInstaller

## 代码重构说明

- `src/*.py` 中的代码是通过函数元数据（名称、参数、API引用、字符串常量）重构而成
- 被 `pass` 标记的函数体表示具体实现逻辑需从字节码反汇编中还原（见 `docs/FINAL_DISASSEMBLY/`）
- `editor/` 目录下的 HTML/CSS/JS 为完整原始源码

## 免责声明

本项目仅用于学习和研究目的。请勿用于任何违法用途。
