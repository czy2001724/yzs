#!/usr/bin/env python3
"""6号自动化助手 —— 本地面板入口。

启动 PyQt5 GUI。桌面自动化（鼠标/键盘/图像识别/全局热键）在 Windows 上体验最佳，
在 Linux/macOS 上界面可正常打开，但部分底层功能（全局钩子、抓屏）依赖平台。
"""
import sys


def main() -> int:
    from PyQt5.QtWidgets import QApplication
    from gui import MainWindow
    from gui.theme import apply_theme

    app = QApplication(sys.argv)
    app.setApplicationName("6号自动化助手")
    apply_theme(app)
    win = MainWindow()
    win.show()
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())
