"""yzs —— 本地面板入口。

启动 PyQt5 GUI。桌面自动化（鼠标/键盘/图像识别/全局热键）在 Windows 上体验最佳，
在 Linux/macOS 上界面可正常打开，但部分底层功能（全局钩子、抓屏）依赖平台。
"""
import os
import sys


def _app_icon_path() -> str:
    """查找图标文件路径，兼容开发模式和 PyInstaller 打包后。"""
    candidates = [
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "qq_icon.ico"),
        os.path.join(getattr(sys, "_MEIPASS", ""), "qq_icon.ico"),
    ]
    for p in candidates:
        if os.path.isfile(p):
            return p
    return ""


def main() -> int:
    from PyQt5.QtGui import QIcon
    from PyQt5.QtWidgets import QApplication
    from gui import MainWindow
    from gui.theme import apply_theme

    app = QApplication(sys.argv)
    app.setApplicationName("QQ")

    icon_path = _app_icon_path()
    if icon_path:
        app.setWindowIcon(QIcon(icon_path))

    apply_theme(app)
    win = MainWindow()
    win.show()
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())
