"""亮色/暗色双主题（QSS）。

默认暖白纸面 + 钴蓝品牌色，支持一键切暗色。
色值来自 UI 设计规范 token。
"""
from __future__ import annotations

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication


# ── Token 定义 ──────────────────────────────────────────────
LIGHT = {
    "paper": "#FBF9F5", "surface": "#FFFFFF", "sunk": "#F4F1EA",
    "ink": "#1D2230", "muted": "#6E7385", "faint": "#9A9EAE",
    "line": "#EAE5DC", "line2": "#DED8CC",
    "brand": "#2E6BFF", "brand_ink": "#204fd0", "brand_wash": "#EAF0FF",
    "go": "#12A870", "go_wash": "#E4F6EE",
    "warn": "#E68A00", "warn_wash": "#FBEEDA",
    "stop": "#E4553F", "stop_wash": "#FBE7E2",
    "swatch_bg": "#F4F1EA",
}

DARK = {
    "paper": "#13151B", "surface": "#1A1D25", "sunk": "#14161C",
    "ink": "#ECEEF5", "muted": "#9AA0B4", "faint": "#71768A",
    "line": "#282C38", "line2": "#333846",
    "brand": "#6E8DFF", "brand_ink": "#8aa2ff", "brand_wash": "#1c2740",
    "go": "#33C48C", "go_wash": "#16281f",
    "warn": "#F0A73A", "warn_wash": "#2a2113",
    "stop": "#F0715B", "stop_wash": "#2c1a16",
    "swatch_bg": "#10121b",
}

FONT_FAMILY = (
    '"Microsoft YaHei UI", "PingFang SC", "Segoe UI", '
    'system-ui, -apple-system, "Hiragino Sans GB", sans-serif'
)
MONO_FAMILY = (
    '"Consolas", "SF Mono", "Cascadia Code", '
    'ui-monospace, "Menlo", monospace'
)


def _make_qss(t: dict) -> str:
    return f"""
* {{
    font-family: {FONT_FAMILY};
    font-size: 13px;
    outline: none;
}}
QMainWindow, QWidget {{ background: {t["paper"]}; color: {t["ink"]}; }}

/* ── 卡片面板 ── */
QFrame#panel {{
    background: {t["surface"]};
    border: 1px solid {t["line"]};
    border-radius: 18px;
}}

/* ── 区块标题 ── */
QLabel#title {{
    font-size: 13px; font-weight: 700; color: {t["muted"]};
    padding: 2px 2px 6px 2px;
}}

/* ── 通用按钮 ── */
QPushButton {{
    background: {t["surface"]};
    color: {t["ink"]};
    border: 1px solid {t["line"]};
    border-radius: 10px;
    padding: 9px 14px; font-weight: 500;
}}
QPushButton:hover   {{ background: {t["line"]}; }}
QPushButton:pressed {{ background: {t["line2"]}; }}
QPushButton:disabled {{ color: {t["faint"]}; background: {t["sunk"]}; border-color: {t["line"]}; }}

/* 动作库按钮 */
QPushButton#toolBtn {{ text-align: left; padding: 10px 16px; font-size: 13px; border-radius: 14px; }}

/* ── 主按钮（运行） ── */
QPushButton#primary {{
    background: {t["go"]};
    border: none; color: #ffffff; font-weight: 700;
    border-radius: 12px; padding: 12px 16px; font-size: 14px;
}}
QPushButton#primary:hover    {{ background: {t["go"]}; opacity: 0.9; }}
QPushButton#primary:disabled {{ background: {t["line"]}; color: {t["faint"]}; }}

/* ── 警告/暂停 ── */
QPushButton#warn {{
    background: {t["warn_wash"]}; border: 1px solid {t["warn"]};
    color: {t["warn"]}; font-weight: 600; border-radius: 12px; padding: 12px 16px;
}}
QPushButton#warn:hover {{ background: {t["warn"]}; color: #fff; }}

/* ── 危险/停止 ── */
QPushButton#danger {{
    background: {t["stop_wash"]}; border: 1px solid {t["stop"]};
    color: {t["stop"]}; font-weight: 600; border-radius: 12px; padding: 12px 16px;
}}
QPushButton#danger:hover {{ background: {t["stop"]}; color: #fff; }}
QPushButton#danger:disabled {{ color: {t["faint"]}; border-color: {t["line"]}; background: {t["sunk"]}; }}

/* 录制按钮选中态 */
QPushButton:checked {{
    background: {t["stop_wash"]}; border: 1px solid {t["stop"]}; color: {t["stop"]};
}}

/* ── 风险标签 ── */
QLabel#riskTag {{
    color: {t["stop"]}; font-size: 10px; font-weight: 700;
    padding: 2px 8px; border: 1px solid {t["stop"]};
    border-radius: 6px; background: {t["stop_wash"]};
}}

/* ── 列表 / 日志 / 输入框 ── */
QListWidget, QPlainTextEdit {{
    background: {t["sunk"]};
    border: 1px solid {t["line"]};
    border-radius: 12px; padding: 8px;
    selection-background-color: {t["brand_wash"]};
}}
QListWidget::item {{ padding: 10px 12px; border-radius: 8px; color: {t["ink"]}; }}
QListWidget::item:hover    {{ background: {t["line"]}; }}
QListWidget::item:selected {{ background: {t["brand_wash"]}; color: {t["brand_ink"]}; }}

QLineEdit, QSpinBox, QDoubleSpinBox, QComboBox {{
    background: {t["sunk"]};
    border: 1px solid {t["line"]};
    border-radius: 9px; padding: 7px 10px;
    color: {t["ink"]};
    selection-background-color: {t["brand_wash"]};
}}
QLineEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus, QComboBox:focus {{
    border-color: {t["brand"]};
}}
QComboBox::drop-down {{ border: none; width: 20px; }}
QComboBox QAbstractItemView {{
    background: {t["surface"]}; border: 1px solid {t["line"]};
    selection-background-color: {t["brand_wash"]}; border-radius: 8px;
}}

/* ── 实时坐标/颜色 ── */
QLabel#coordValue {{
    font-family: {MONO_FAMILY}; tabular-nums: 1;
    font-size: 26px; font-weight: 700; color: {t["ink"]};
}}
QLabel#colorValue {{
    font-family: {MONO_FAMILY}; font-size: 14px; color: {t["muted"]};
}}
QFrame#swatch {{
    border: 1px solid {t["line"]}; border-radius: 10px; background: {t["swatch_bg"]};
}}

/* ── 进度 / 提示 ── */
QLabel#progress {{ color: {t["muted"]}; font-weight: 600; }}
QLabel#hint {{ color: {t["faint"]}; font-size: 11px; }}

/* ── 空状态引导 ── */
QLabel#emptyGuide {{
    color: {t["faint"]}; font-size: 13px; padding: 20px;
}}

/* ── 序列号 ── */
QLabel#stepNum {{
    font-size: 16px; font-weight: 800; color: {t["brand"]};
    padding: 0 8px 0 0;
}}

/* ── 折叠区域标题 ── */
QPushButton#foldBtn {{
    text-align: left; font-size: 12px; font-weight: 600;
    color: {t["muted"]}; border: none; background: transparent; padding: 6px 0;
}}
QPushButton#foldBtn:hover {{ color: {t["ink"]}; }}

/* ── 分割线 ── */
QFrame[frameShape="4"] {{ color: {t["line"]}; max-height: 1px; }}

/* ── 滚动条 ── */
QScrollBar:vertical   {{ background: transparent; width: 10px; margin: 2px; }}
QScrollBar::handle:vertical {{ background: {t["line2"]}; border-radius: 5px; min-height: 30px; }}
QScrollBar::handle:vertical:hover {{ background: {t["muted"]}; }}
QScrollBar::add-line, QScrollBar::sub-line {{ height: 0; }}
QScrollBar:horizontal {{ background: transparent; height: 10px; margin: 2px; }}
QScrollBar::handle:horizontal {{ background: {t["line2"]}; border-radius: 5px; min-width: 30px; }}

/* ── 对话框 ── */
QDialog {{ background: {t["surface"]}; }}
QMessageBox {{ background: {t["surface"]}; }}

/* ── 进度条 ── */
QProgressBar {{
    border: 1px solid {t["line"]}; border-radius: 8px;
    background: {t["sunk"]}; height: 8px; text-align: center;
}}
QProgressBar::chunk {{
    background: {t["go"]}; border-radius: 7px;
}}

/* ── 复选框 ── */
QCheckBox {{ color: {t["ink"]}; spacing: 8px; }}
QCheckBox::indicator {{
    width: 18px; height: 18px; border-radius: 5px;
    border: 1px solid {t["line"]}; background: {t["sunk"]};
}}
QCheckBox::indicator:checked {{ background: {t["brand"]}; border-color: {t["brand"]}; }}
"""


LIGHT_QSS = _make_qss(LIGHT)
DARK_QSS = _make_qss(DARK)

_current_dark = False


def apply_theme(app: QApplication, dark: bool = False) -> None:
    """应用 Fusion 基底 + 主题 QSS。dark=False 使用亮色（默认）。"""
    global _current_dark
    _current_dark = dark
    try:
        app.setStyle("Fusion")
    except Exception:
        pass
    app.setFont(QFont("Microsoft YaHei UI", 10))
    app.setStyleSheet(DARK_QSS if dark else LIGHT_QSS)


def toggle_theme(app: QApplication) -> bool:
    """切换亮/暗主题，返回切换后的暗色状态。"""
    global _current_dark
    _current_dark = not _current_dark
    app.setStyleSheet(DARK_QSS if _current_dark else LIGHT_QSS)
    return _current_dark
