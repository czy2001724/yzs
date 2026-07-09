"""步骤编辑对话框：人话命名 + 去屏幕点一下取坐标。"""
from __future__ import annotations

import time
from typing import Optional

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (
    QApplication, QComboBox, QDialog, QDialogButtonBox, QDoubleSpinBox,
    QFormLayout, QHBoxLayout, QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSpinBox, QVBoxLayout, QWidget, QFileDialog,
)

from automation import pointer

# 人话显示名（type 键保持不变，兼容已有 JSON）
STEP_TYPES = [
    ("click", "点一下"),
    ("double_click", "连点两下"),
    ("right_click", "右键菜单"),
    ("move", "移动鼠标"),
    ("drag", "拖过去"),
    ("scroll", "滚轮"),
    ("type", "输入文字"),
    ("key", "按下按键"),
    ("hotkey", "快捷键（如 Ctrl+C）"),
    ("wait", "等一会儿"),
    ("screenshot", "截图存起来"),
    ("find_image", "找到图片再操作"),
    ("window_find", "找到窗口"),
    ("window_move", "移动/缩放窗口"),
]
TYPE_LABELS = dict(STEP_TYPES)


def describe_step(step: dict) -> str:
    """把步骤转成一句话人话描述。"""
    t = step.get("type", "?")
    if t == "click":
        return f"在 ({step.get('x')}, {step.get('y')}) 点{step.get('button', '左键')}"
    elif t == "double_click":
        return f"在 ({step.get('x')}, {step.get('y')}) 连点两下"
    elif t == "right_click":
        return f"在 ({step.get('x')}, {step.get('y')}) 按右键"
    elif t == "move":
        return f"鼠标移到 ({step.get('x')}, {step.get('y')})"
    elif t == "drag":
        return f"从 ({step.get('x1')},{step.get('y1')}) 拖到 ({step.get('x2')},{step.get('y2')})"
    elif t == "scroll":
        return f"滚轮 {step.get('amount')}"
    elif t == "type":
        return f"输入文字 {repr(step.get('text', ''))}"
    elif t == "key":
        return f"按下 {step.get('key', '')}"
    elif t == "hotkey":
        return f"快捷键 {'+'.join(step.get('keys', []))}"
    elif t == "wait":
        return f"等 {step.get('seconds')} 秒"
    elif t == "screenshot":
        return f"截图存到 {step.get('path', '')}"
    elif t == "find_image":
        tmpl = step.get("template", "")
        action = "找到就点" if step.get("click", True) else "找到不点"
        return f"找 {tmpl}，{action}"
    elif t == "window_find":
        return f"找窗口「{step.get('title', '')}」并{'置顶' if step.get('focus', True) else '不置顶'}"
    elif t == "window_move":
        return f"移到 ({step.get('x')},{step.get('y')}) 大小 {step.get('width',0)}x{step.get('height',0)}"
    return f"未知 ({t})"


class StepDialog(QDialog):
    """根据步骤类型动态生成表单。支持去屏幕点一下取坐标。"""

    def __init__(self, step_type: str, step: Optional[dict] = None, parent=None):
        super().__init__(parent)
        self.step_type = step_type
        self.step = dict(step or {})
        self.setWindowTitle(TYPE_LABELS.get(step_type, step_type))
        self.setMinimumWidth(380)
        self._widgets = {}
        self._pick_fields: list[str] = []  # 需要取坐标的字段名
        self._build()

    def _spin(self, key, default=0, minimum=-100000, maximum=100000):
        w = QSpinBox()
        w.setRange(minimum, maximum)
        w.setValue(int(self.step.get(key, default)))
        self._widgets[key] = w
        return w

    def _dspin(self, key, default=0.0, minimum=0.0, maximum=100000.0, step=0.1):
        w = QDoubleSpinBox()
        w.setRange(minimum, maximum)
        w.setSingleStep(step)
        w.setValue(float(self.step.get(key, default)))
        self._widgets[key] = w
        return w

    def _line(self, key, default=""):
        w = QLineEdit(str(self.step.get(key, default)))
        self._widgets[key] = w
        return w

    def _coord_pair(self, xkey: str, ykey: str) -> QWidget:
        """坐标输入行：X/Y 框 + '去屏幕上点一下' 按钮。"""
        row = QWidget()
        h = QHBoxLayout(row)
        h.setContentsMargins(0, 0, 0, 0)
        h.setSpacing(6)

        xspin = self._spin(xkey)
        yspin = self._spin(ykey)
        h.addWidget(QLabel("X"))
        h.addWidget(xspin)
        h.addWidget(QLabel("Y"))
        h.addWidget(yspin)

        btn = QPushButton("去屏幕上点一下")
        btn.clicked.connect(lambda: self._pick_from_screen(xkey, ykey))
        h.addWidget(btn)
        h.addStretch(1)
        return row

    def _pick_from_screen(self, xkey: str, ykey: str):
        """隐藏窗口，等用户在屏幕上任意位置点击，回填坐标。"""
        self.hide()
        QApplication.processEvents()
        time.sleep(0.3)

        import pyautogui
        pyautogui.FAILSAFE = True
        self._picking = True

        def poll():
            if not getattr(self, "_picking", False):
                return
            try:
                # 检测鼠标左键按下
                import ctypes
                if ctypes.windll.user32.GetAsyncKeyState(0x01) & 0x8000:
                    self._picking = False
                    x, y = pointer.get_cursor_pos()
                    if xkey in self._widgets:
                        self._widgets[xkey].setValue(x)
                    if ykey in self._widgets:
                        self._widgets[ykey].setValue(y)
                    self.show()
                    return
            except Exception:
                self._picking = False
                self.show()
                return
            QTimer.singleShot(50, poll)

        QTimer.singleShot(100, poll)

    def _build(self):
        layout = QVBoxLayout(self)
        form = QFormLayout()
        t = self.step_type

        if t in ("click", "double_click", "right_click", "move"):
            form.addRow("坐标", self._coord_pair("x", "y"))
            form.addRow("移动快慢 (秒)", self._dspin("duration", 0.25))
            if t == "click":
                btn = QComboBox()
                btn.addItems(["左键", "右键", "中键"])
                btn_map = {"左键": "left", "右键": "right", "中键": "middle"}
                cur = self.step.get("button", "left")
                for label, val in btn_map.items():
                    if val == cur:
                        btn.setCurrentText(label)
                self._widgets["button"] = btn
                self._button_map = btn_map
                form.addRow("按键", btn)
                form.addRow("连击", self._spin("clicks", 1, 1, 10))
        elif t == "drag":
            form.addRow("起点", self._coord_pair("x1", "y1"))
            form.addRow("终点", self._coord_pair("x2", "y2"))
            form.addRow("拖拽快慢 (秒)", self._dspin("duration", 0.5))
        elif t == "scroll":
            form.addRow("滚轮量（负=往下）", self._spin("amount", -300))
        elif t == "type":
            form.addRow("要输入的文字", self._line("text"))
            form.addRow("每个字间隔 (秒)", self._dspin("interval", 0.02, step=0.01))
        elif t == "key":
            form.addRow("按键名 (如 enter)", self._line("key", "enter"))
        elif t == "hotkey":
            form.addRow("快捷键 (逗号分隔)", self._line("_keys", "ctrl,c"))
        elif t == "wait":
            form.addRow("等多久 (秒)", self._dspin("seconds", 1.0))
        elif t == "screenshot":
            row, _ = self._file_row("path", save=True)
            form.addRow("存到哪里", row)
        elif t == "find_image":
            row, _ = self._file_row("template", save=False)
            form.addRow("目标图片", row)
            form.addRow("最低相似度", self._dspin("confidence", 0.8, 0.1, 1.0, 0.05))
            click = QComboBox()
            click.addItems(["找到就点击", "只找不点"])
            click.setCurrentIndex(0 if self.step.get("click", True) else 1)
            self._widgets["click"] = click
            form.addRow("找到后", click)
        elif t == "window_find":
            # 窗口标题行：输入框 + "从列表选"按钮
            title_row = QWidget()
            th = QHBoxLayout(title_row)
            th.setContentsMargins(0, 0, 0, 0)
            th.setSpacing(6)
            title_edit = self._line("title", "")
            th.addWidget(title_edit, 1)
            pick_btn = QPushButton("从列表选")
            pick_btn.clicked.connect(lambda: self._pick_window())
            th.addWidget(pick_btn)
            form.addRow("窗口标题含", title_row)

            focus = QComboBox()
            focus.addItems(["找到就置顶", "找到不置顶"])
            focus.setCurrentIndex(0 if self.step.get("focus", True) else 1)
            self._widgets["focus"] = focus
            form.addRow("行为", focus)
        elif t == "window_move":
            form.addRow("移到 X/Y", self._coord_pair("x", "y"))
            form.addRow("宽度 (0=不改)", self._spin("width", 0, 0, 10000))
            form.addRow("高度 (0=不改)", self._spin("height", 0, 0, 10000))

        layout.addLayout(form)
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def _pick_window(self):
        """弹出窗口选择器，列出所有有标题的窗口供用户点选。"""
        from automation.window import list_windows
        dlg = QDialog(self)
        dlg.setWindowTitle("选择窗口")
        dlg.setMinimumSize(400, 350)
        v = QVBoxLayout(dlg)
        v.addWidget(QLabel("当前打开的窗口（点选一个）："))
        lst = QListWidget()
        titles = list_windows()
        if not titles:
            lst.addItem("（没找到有标题的窗口，请打开游戏后再试）")
        for t in titles:
            item = QListWidgetItem(t)
            lst.addItem(item)
        v.addWidget(lst, 1)
        btns = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btns.accepted.connect(dlg.accept)
        btns.rejected.connect(dlg.reject)
        v.addWidget(btns)
        if dlg.exec_() == QDialog.Accepted and lst.currentItem() and titles:
            chosen = lst.currentItem().text()
            if "title" in self._widgets:
                self._widgets["title"].setText(chosen)

    def _file_row(self, key, save: bool):
        container = QWidget()
        h = QHBoxLayout(container)
        h.setContentsMargins(0, 0, 0, 0)
        edit = QLineEdit(str(self.step.get(key, "")))
        self._widgets[key] = edit
        btn = QPushButton("浏览…")

        def pick():
            if save:
                path, _ = QFileDialog.getSaveFileName(self, "选择保存位置", "", "PNG (*.png)")
            else:
                path, _ = QFileDialog.getOpenFileName(self, "选择图片", "", "图片 (*.png *.jpg *.bmp)")
            if path:
                edit.setText(path)

        btn.clicked.connect(pick)
        h.addWidget(edit)
        h.addWidget(btn)
        return container, btn

    def result_step(self) -> dict:
        """收集表单，返回步骤 dict。"""
        out = {"type": self.step_type}
        for key, w in self._widgets.items():
            if isinstance(w, QSpinBox):
                out[key] = w.value()
            elif isinstance(w, QDoubleSpinBox):
                out[key] = round(w.value(), 4)
            elif isinstance(w, QComboBox):
                if key == "click":
                    out[key] = w.currentIndex() == 0
                elif key == "focus":
                    out[key] = w.currentIndex() == 0
                elif key == "button":
                    btn_map = getattr(self, "_button_map", {})
                    out[key] = btn_map.get(w.currentText(), "left")
                else:
                    out[key] = w.currentText()
            elif isinstance(w, QLineEdit):
                out[key] = w.text()
        if "_keys" in out:
            out["keys"] = [k.strip() for k in out.pop("_keys").split(",") if k.strip()]
        return out
