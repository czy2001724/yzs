"""现代深色主题（QSS）。"""
from __future__ import annotations

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication

DARK_QSS = """
* {
    font-family: "Segoe UI", "Microsoft YaHei UI", "PingFang SC", sans-serif;
    font-size: 13px;
    outline: none;
}
QMainWindow, QWidget { background: #0f1017; color: #e7e9f3; }

/* 卡片式面板 */
QFrame#panel {
    background: #171925;
    border: 1px solid #262a3d;
    border-radius: 14px;
}

/* 区块标题 */
QLabel#title {
    font-size: 13px;
    font-weight: 700;
    color: #aeb4cc;
    padding: 2px 2px 4px 2px;
}

/* 通用按钮 */
QPushButton {
    background: #222536;
    color: #e7e9f3;
    border: 1px solid #313650;
    border-radius: 9px;
    padding: 9px 12px;
    font-weight: 500;
}
QPushButton:hover   { background: #2a2f45; border-color: #4a5480; }
QPushButton:pressed { background: #1c2032; }
QPushButton:disabled { color: #5b6076; background: #1a1c28; border-color: #262a3d; }

/* 动作库按钮：左对齐、稍紧凑 */
QPushButton#toolBtn { text-align: left; padding: 9px 14px; }

/* 主/警告/危险按钮 */
QPushButton#primary {
    background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #6c8cff, stop:1 #5a78f0);
    border: none; color: #ffffff; font-weight: 700;
}
QPushButton#primary:hover    { background: #7d99ff; }
QPushButton#primary:disabled { background: #2a2f45; color: #6b7290; }
QPushButton#warn {
    background: #2a2536; border: 1px solid #6b5bd6; color: #cbbcff; font-weight: 600;
}
QPushButton#warn:hover { background: #342c48; }
QPushButton#danger {
    background: #2a1f27; border: 1px solid #ff6b6b; color: #ff9b9b; font-weight: 600;
}
QPushButton#danger:hover    { background: #3a2730; }
QPushButton#danger:disabled { color: #6b5057; border-color: #3a2730; background: #1a1c28; }

/* 录制按钮选中态 */
QPushButton:checked {
    background: #3a1f28; border: 1px solid #ff6b6b; color: #ffb3b3;
}

/* 列表 / 日志 / 输入框 */
QListWidget, QPlainTextEdit {
    background: #10121b;
    border: 1px solid #262a3d;
    border-radius: 11px;
    padding: 6px;
    selection-background-color: #3350a0;
}
QListWidget::item { padding: 9px 10px; border-radius: 7px; color: #d3d7e8; }
QListWidget::item:hover    { background: #1b1f30; }
QListWidget::item:selected { background: #2b3663; color: #ffffff; }

QLineEdit, QSpinBox, QDoubleSpinBox, QComboBox {
    background: #10121b;
    border: 1px solid #2a2f45;
    border-radius: 8px;
    padding: 6px 8px;
    color: #e7e9f3;
    selection-background-color: #3350a0;
}
QLineEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus, QComboBox:focus {
    border-color: #6c8cff;
}
QComboBox::drop-down { border: none; width: 20px; }
QComboBox QAbstractItemView {
    background: #171925; border: 1px solid #313650;
    selection-background-color: #2b3663; border-radius: 8px;
}

/* 实时状态数值 */
QLabel#coordValue {
    font-family: "Consolas", "SF Mono", monospace;
    font-size: 26px; font-weight: 700; color: #ffffff;
    letter-spacing: 1px;
}
QLabel#colorValue {
    font-family: "Consolas", monospace; font-size: 14px; color: #aeb4cc;
}
QFrame#swatch { border: 1px solid #313650; border-radius: 8px; background: #10121b; }

QLabel#progress { color: #8b93b0; font-weight: 600; }
QLabel#hint { color: #6b7290; font-size: 11px; }

/* 分割线 */
QFrame[frameShape="4"] { color: #262a3d; max-height: 1px; }

/* 滚动条 */
QScrollBar:vertical   { background: transparent; width: 10px; margin: 2px; }
QScrollBar::handle:vertical { background: #2f3550; border-radius: 5px; min-height: 30px; }
QScrollBar::handle:vertical:hover { background: #414a72; }
QScrollBar::add-line, QScrollBar::sub-line { height: 0; }
QScrollBar:horizontal { background: transparent; height: 10px; margin: 2px; }
QScrollBar::handle:horizontal { background: #2f3550; border-radius: 5px; min-width: 30px; }

/* 对话框 */
QDialog { background: #12141d; }
QMessageBox { background: #12141d; }
"""


def apply_theme(app: QApplication) -> None:
    """应用 Fusion 基底 + 深色 QSS。"""
    try:
        app.setStyle("Fusion")
    except Exception:
        pass
    app.setFont(QFont("Segoe UI", 10))
    app.setStyleSheet(DARK_QSS)
