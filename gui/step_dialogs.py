"""步骤编辑对话框：为每种动作类型提供参数录入界面。"""
from __future__ import annotations

from typing import Optional

from PyQt5.QtWidgets import (
    QComboBox, QDialog, QDialogButtonBox, QDoubleSpinBox, QFormLayout,
    QHBoxLayout, QLineEdit, QPushButton, QSpinBox, QVBoxLayout, QWidget,
    QFileDialog,
)

# 步骤类型 -> 中文名
STEP_TYPES = [
    ("click", "鼠标点击"),
    ("double_click", "鼠标双击"),
    ("right_click", "鼠标右键"),
    ("move", "移动鼠标"),
    ("drag", "拖拽"),
    ("scroll", "滚轮"),
    ("type", "输入文本"),
    ("key", "单个按键"),
    ("hotkey", "组合键"),
    ("wait", "等待"),
    ("screenshot", "截图"),
    ("find_image", "图像识别定位"),
]
TYPE_LABELS = dict(STEP_TYPES)


def describe_step(step: dict) -> str:
    """把步骤转成一行可读描述，用于列表显示。"""
    t = step.get("type", "?")
    label = TYPE_LABELS.get(t, t)
    if t in ("click", "double_click", "right_click", "move"):
        extra = f"({step.get('x')}, {step.get('y')})"
    elif t == "drag":
        extra = f"({step.get('x1')},{step.get('y1')})→({step.get('x2')},{step.get('y2')})"
    elif t == "scroll":
        extra = f"{step.get('amount')}"
    elif t == "type":
        extra = repr(step.get("text", ""))
    elif t == "key":
        extra = step.get("key", "")
    elif t == "hotkey":
        extra = "+".join(step.get("keys", []))
    elif t == "wait":
        extra = f"{step.get('seconds')}s"
    elif t == "screenshot":
        extra = step.get("path", "")
    elif t == "find_image":
        extra = f"{step.get('template', '')} · 相似度≥{step.get('confidence', 0.8)}"
    else:
        extra = ""
    return f"{label}  {extra}"


class StepDialog(QDialog):
    """根据步骤类型动态生成表单的编辑对话框。"""

    def __init__(self, step_type: str, step: Optional[dict] = None, parent=None):
        super().__init__(parent)
        self.step_type = step_type
        self.step = dict(step or {})
        self.setWindowTitle(f"编辑步骤 · {TYPE_LABELS.get(step_type, step_type)}")
        self.setMinimumWidth(360)
        self._widgets = {}
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

    def _build(self):
        layout = QVBoxLayout(self)
        form = QFormLayout()
        t = self.step_type

        if t in ("click", "double_click", "right_click", "move"):
            form.addRow("X", self._spin("x"))
            form.addRow("Y", self._spin("y"))
            form.addRow("移动耗时(s)", self._dspin("duration", 0.25))
            if t == "click":
                btn = QComboBox()
                btn.addItems(["left", "right", "middle"])
                btn.setCurrentText(self.step.get("button", "left"))
                self._widgets["button"] = btn
                form.addRow("按键", btn)
                form.addRow("点击次数", self._spin("clicks", 1, 1, 10))
        elif t == "drag":
            form.addRow("起点 X", self._spin("x1"))
            form.addRow("起点 Y", self._spin("y1"))
            form.addRow("终点 X", self._spin("x2"))
            form.addRow("终点 Y", self._spin("y2"))
            form.addRow("拖拽耗时(s)", self._dspin("duration", 0.5))
        elif t == "scroll":
            form.addRow("滚动量(负=下)", self._spin("amount", -300))
        elif t == "type":
            form.addRow("文本", self._line("text"))
            form.addRow("每字间隔(s)", self._dspin("interval", 0.02, step=0.01))
        elif t == "key":
            form.addRow("键名(如 enter)", self._line("key", "enter"))
        elif t == "hotkey":
            form.addRow("组合键(逗号分隔)", self._line("_keys", "ctrl,c"))
        elif t == "wait":
            form.addRow("等待秒数", self._dspin("seconds", 1.0))
        elif t == "screenshot":
            row, browse = self._file_row("path", save=True)
            form.addRow("保存路径", row)
        elif t == "find_image":
            row, _ = self._file_row("template", save=False)
            form.addRow("模板图片", row)
            form.addRow("相似度阈值", self._dspin("confidence", 0.8, 0.1, 1.0, 0.05))
            click = QComboBox()
            click.addItems(["找到后点击", "只定位不点击"])
            click.setCurrentIndex(0 if self.step.get("click", True) else 1)
            self._widgets["click"] = click
            form.addRow("动作", click)

        layout.addLayout(form)
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

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
                else:
                    out[key] = w.currentText()
            elif isinstance(w, QLineEdit):
                out[key] = w.text()
        # 处理组合键特殊字段
        if "_keys" in out:
            out["keys"] = [k.strip() for k in out.pop("_keys").split(",") if k.strip()]
        return out
