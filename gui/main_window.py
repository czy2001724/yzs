"""PyQt5 主窗口：本地自动化控制面板。"""
from __future__ import annotations

import json
import os
import time
from typing import List, Optional

from PyQt5.QtCore import Qt, QThread, QTimer, pyqtSignal
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import (
    QApplication, QCheckBox, QComboBox, QFileDialog, QFrame, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMessageBox, QPlainTextEdit,
    QPushButton, QSpinBox, QVBoxLayout, QWidget,
)

from automation import AutomationEngine, GlobalInputRecorder, HumanizeConfig
from automation import pointer
from .hotkeys import NativeHotkeyManager
from .step_dialogs import STEP_TYPES, StepDialog, describe_step


# --------------------------------------------------------------------------- #
# 后台执行线程
# --------------------------------------------------------------------------- #
class RunnerThread(QThread):
    log = pyqtSignal(str)
    progress = pyqtSignal(int, int)
    finished_run = pyqtSignal(bool)

    def __init__(self, steps: List[dict], loops: int, humanize: HumanizeConfig):
        super().__init__()
        self.steps = steps
        self.loops = loops
        self.engine = AutomationEngine(
            log_cb=self.log.emit,
            step_cb=lambda i, t: self.progress.emit(i, t),
            humanize=humanize,
        )

    def run(self):
        ok = self.engine.run(self.steps, self.loops)
        self.finished_run.emit(ok)

    def request_pause(self):
        self.engine.pause()

    def request_resume(self):
        self.engine.resume()

    def request_stop(self):
        self.engine.stop()


# --------------------------------------------------------------------------- #
# 主窗口
# --------------------------------------------------------------------------- #
class MainWindow(QMainWindow):
    _recorder_event = pyqtSignal(dict)
    _hotkey_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QQ")
        self.resize(1040, 640)

        self.steps: List[dict] = []
        self.runner: Optional[RunnerThread] = None
        self.recorder = GlobalInputRecorder(on_event=self._recorder_event.emit)
        self.hotkeys = NativeHotkeyManager()
        self.humanize = HumanizeConfig()

        self._build_ui()
        self._setup_signals()
        self._setup_hotkeys()

        # RegisterHotKey 需要 Qt nativeEventFilter（无低级钩子，反作弊安全）
        QApplication.instance().installNativeEventFilter(self.hotkeys)

        # 实时坐标 / 颜色显示（Win32 直读，~30fps 无延迟）
        self._coord_timer = QTimer(self)
        self._coord_timer.timeout.connect(self._update_coord)
        self._coord_timer.start(33)

    # ------------------------------ UI ---------------------------------- #
    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        root = QHBoxLayout(central)
        root.setContentsMargins(14, 14, 14, 14)
        root.setSpacing(12)

        root.addWidget(self._build_toolbox(), 0)
        root.addWidget(self._build_center(), 1)
        root.addWidget(self._build_right(), 0)

    def _build_toolbox(self) -> QWidget:
        panel = QFrame()
        panel.setObjectName("panel")
        panel.setFixedWidth(196)
        v = QVBoxLayout(panel)
        v.setContentsMargins(12, 14, 12, 14)
        v.setSpacing(8)
        v.addWidget(self._title("⚡  动作库"))
        for step_type, label in STEP_TYPES:
            btn = QPushButton(label)
            btn.setObjectName("toolBtn")
            btn.clicked.connect(lambda _=False, t=step_type: self._add_step(t))
            v.addWidget(btn)
        v.addStretch(1)
        return panel

    def _build_center(self) -> QWidget:
        panel = QWidget()
        v = QVBoxLayout(panel)
        v.setContentsMargins(0, 0, 0, 0)
        v.setSpacing(10)
        v.addWidget(self._title("🧩  工作流步骤"))

        self.step_list = QListWidget()
        self.step_list.itemDoubleClicked.connect(lambda _: self._edit_step())
        v.addWidget(self.step_list, 1)

        # 步骤操作行
        ops = QHBoxLayout()
        for text, slot in [
            ("上移", self._move_up), ("下移", self._move_down),
            ("编辑", self._edit_step), ("删除", self._delete_step),
            ("清空", self._clear_steps),
        ]:
            b = QPushButton(text)
            b.clicked.connect(slot)
            ops.addWidget(b)
        v.addLayout(ops)

        # 文件行
        files = QHBoxLayout()
        for text, slot in [("💾 保存", self._save_workflow), ("📂 加载", self._load_workflow)]:
            b = QPushButton(text)
            b.clicked.connect(slot)
            files.addWidget(b)
        files.addStretch(1)
        v.addLayout(files)

        v.addWidget(self._title("📜  运行日志"))
        self.log_view = QPlainTextEdit()
        self.log_view.setReadOnly(True)
        self.log_view.setMaximumBlockCount(2000)
        self.log_view.setFont(QFont("Consolas", 9))
        v.addWidget(self.log_view, 1)
        return panel

    def _build_right(self) -> QWidget:
        panel = QFrame()
        panel.setObjectName("panel")
        panel.setFixedWidth(258)
        v = QVBoxLayout(panel)
        v.setContentsMargins(16, 16, 16, 16)
        v.setSpacing(9)

        v.addWidget(self._title("🎯  实时状态"))
        self.coord_label = QLabel("–, –")
        self.coord_label.setObjectName("coordValue")
        v.addWidget(self.coord_label)
        self.color_label = QLabel("#——————")
        self.color_label.setObjectName("colorValue")
        v.addWidget(self.color_label)
        self.color_swatch = QFrame()
        self.color_swatch.setObjectName("swatch")
        self.color_swatch.setFixedHeight(30)
        v.addWidget(self.color_swatch)

        v.addWidget(self._hline())
        v.addWidget(self._title("🚀  运行控制"))
        loop_row = QHBoxLayout()
        loop_row.addWidget(QLabel("循环次数"))
        self.loop_spin = QSpinBox()
        self.loop_spin.setRange(0, 999999)
        self.loop_spin.setValue(1)
        self.loop_spin.setToolTip("0 = 无限循环")
        loop_row.addWidget(self.loop_spin)
        v.addLayout(loop_row)

        self.btn_run = QPushButton("▶  运行  ·  F9")
        self.btn_run.setObjectName("primary")
        self.btn_run.clicked.connect(self._start_run)
        self.btn_pause = QPushButton("⏸  暂停  ·  F11")
        self.btn_pause.setObjectName("warn")
        self.btn_pause.clicked.connect(self._toggle_pause)
        self.btn_pause.setEnabled(False)
        self.btn_stop = QPushButton("⏹  停止  ·  F10")
        self.btn_stop.setObjectName("danger")
        self.btn_stop.clicked.connect(self._stop_run)
        self.btn_stop.setEnabled(False)
        for b in (self.btn_run, self.btn_pause, self.btn_stop):
            v.addWidget(b)
        self.progress_label = QLabel("进度  0 / 0")
        self.progress_label.setObjectName("progress")
        v.addWidget(self.progress_label)

        v.addWidget(self._hline())
        v.addWidget(self._title("👤  拟人化 · 反作弊"))
        self.chk_humanize = QCheckBox("启用拟人化（降低检测风险）")
        self.chk_humanize.setChecked(self.humanize.enabled)
        self.chk_humanize.toggled.connect(self._on_humanize_toggle)
        v.addWidget(self.chk_humanize)
        jitter_row = QHBoxLayout()
        jitter_row.addWidget(QLabel("坐标抖动(px)"))
        self.spin_jitter = QSpinBox()
        self.spin_jitter.setRange(0, 20)
        self.spin_jitter.setValue(self.humanize.click_jitter)
        self.spin_jitter.valueChanged.connect(lambda v: setattr(self.humanize, "click_jitter", v))
        jitter_row.addWidget(self.spin_jitter)
        v.addLayout(jitter_row)
        bez_row = QHBoxLayout()
        bez_row.addWidget(QLabel("轨迹偏移(px)"))
        self.spin_bezier = QSpinBox()
        self.spin_bezier.setRange(0, 200)
        self.spin_bezier.setValue(self.humanize.bezier_deviation)
        self.spin_bezier.setToolTip("贝塞尔曲线偏离直线的最大像素距离，0=走直线")
        self.spin_bezier.valueChanged.connect(lambda v: setattr(self.humanize, "bezier_deviation", v))
        bez_row.addWidget(self.spin_bezier)
        v.addLayout(bez_row)
        os_row = QHBoxLayout()
        os_row.addWidget(QLabel("过冲幅度(px)"))
        self.spin_overshoot = QSpinBox()
        self.spin_overshoot.setRange(0, 30)
        self.spin_overshoot.setValue(self.humanize.overshoot)
        self.spin_overshoot.setToolTip("到达终点后略微超过再拉回，模拟手抖矫正，0=不过冲")
        self.spin_overshoot.valueChanged.connect(lambda v: setattr(self.humanize, "overshoot", v))
        os_row.addWidget(self.spin_overshoot)
        v.addLayout(os_row)
        chk_pixel = QCheckBox("实时像素取色（GDI读屏，触发反作弊）")
        chk_pixel.setChecked(True)
        chk_pixel.toggled.connect(pointer.set_pixel_reading)
        v.addWidget(chk_pixel)

        v.addWidget(self._hline())
        v.addWidget(self._title("🎬  录制与捕获"))
        self.btn_record = QPushButton("●  开始录制  ⚠️非反作弊安全")
        self.btn_record.setCheckable(True)
        self.btn_record.clicked.connect(self._toggle_record)
        v.addWidget(self.btn_record)
        b_shot = QPushButton("📷  抓取模板图")
        b_shot.clicked.connect(self._capture_template)
        v.addWidget(b_shot)

        v.addStretch(1)
        hint = QLabel("全局热键  F9 运行 · F10 停止 · F11 暂停\n"
                      "鼠标甩到屏幕左上角可紧急停止")
        hint.setObjectName("hint")
        hint.setWordWrap(True)
        v.addWidget(hint)
        return panel

    def _title(self, text: str) -> QLabel:
        lbl = QLabel(text)
        lbl.setObjectName("title")
        return lbl

    def _hline(self) -> QFrame:
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        return line

    # ---------------------------- 信号 ---------------------------------- #
    def _setup_signals(self):
        self._recorder_event.connect(self._on_recorded_event)
        self._hotkey_signal.connect(self._on_hotkey)

    def _setup_hotkeys(self):
        if not self.hotkeys.available:
            self.append_log("⚠ 全局热键不可用")
            return
        self.hotkeys.register("f9", lambda: self._hotkey_signal.emit("run"))
        self.hotkeys.register("f10", lambda: self._hotkey_signal.emit("stop"))
        self.hotkeys.register("f11", lambda: self._hotkey_signal.emit("pause"))

    def _on_hotkey(self, action: str):
        if action == "run":
            if self.runner is None:
                self._start_run()
        elif action == "stop":
            self._stop_run()
        elif action == "pause":
            if self.runner is not None:
                self._toggle_pause()

    # ---------------------------- 步骤管理 ------------------------------ #
    def _add_step(self, step_type: str):
        dlg = StepDialog(step_type, parent=self)
        if dlg.exec_() == StepDialog.Accepted:
            self.steps.append(dlg.result_step())
            self._refresh_steps()

    def _edit_step(self):
        row = self.step_list.currentRow()
        if row < 0:
            return
        step = self.steps[row]
        dlg = StepDialog(step["type"], step, parent=self)
        if dlg.exec_() == StepDialog.Accepted:
            self.steps[row] = dlg.result_step()
            self._refresh_steps()
            self.step_list.setCurrentRow(row)

    def _delete_step(self):
        row = self.step_list.currentRow()
        if row >= 0:
            self.steps.pop(row)
            self._refresh_steps()

    def _clear_steps(self):
        if self.steps and QMessageBox.question(
            self, "确认", "清空所有步骤？"
        ) == QMessageBox.Yes:
            self.steps.clear()
            self._refresh_steps()

    def _move_up(self):
        row = self.step_list.currentRow()
        if row > 0:
            self.steps[row - 1], self.steps[row] = self.steps[row], self.steps[row - 1]
            self._refresh_steps()
            self.step_list.setCurrentRow(row - 1)

    def _move_down(self):
        row = self.step_list.currentRow()
        if 0 <= row < len(self.steps) - 1:
            self.steps[row + 1], self.steps[row] = self.steps[row], self.steps[row + 1]
            self._refresh_steps()
            self.step_list.setCurrentRow(row + 1)

    def _refresh_steps(self):
        self.step_list.clear()
        for i, step in enumerate(self.steps, 1):
            item = QListWidgetItem(f"{i:>2}. {describe_step(step)}")
            self.step_list.addItem(item)

    # ---------------------------- 存 / 取 ------------------------------- #
    def _save_workflow(self):
        path, _ = QFileDialog.getSaveFileName(self, "保存工作流", "workflow.json", "JSON (*.json)")
        if not path:
            return
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"steps": self.steps}, f, ensure_ascii=False, indent=2)
        self.append_log(f"已保存工作流：{path}")

    def _load_workflow(self):
        path, _ = QFileDialog.getOpenFileName(self, "加载工作流", "", "JSON (*.json)")
        if not path:
            return
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.steps = data.get("steps", [])
        self._refresh_steps()
        self.append_log(f"已加载工作流：{path}（{len(self.steps)} 步）")

    # ---------------------------- 运行控制 ------------------------------ #
    def _start_run(self):
        if self.runner is not None:
            return
        if not self.steps:
            QMessageBox.information(self, "提示", "还没有任何步骤")
            return
        loops = self.loop_spin.value()
        self.runner = RunnerThread(self.steps, loops, self.humanize)
        self.runner.log.connect(self.append_log)
        self.runner.progress.connect(self._on_progress)
        self.runner.finished_run.connect(self._on_finished)
        self.runner.start()
        self.btn_run.setEnabled(False)
        self.btn_pause.setEnabled(True)
        self.btn_stop.setEnabled(True)
        self.btn_pause.setText("⏸ 暂停 (F11)")
        self.append_log("=== 开始运行 ===")

    def _toggle_pause(self):
        if self.runner is None:
            return
        if self.btn_pause.text().startswith("⏸"):
            self.runner.request_pause()
            self.btn_pause.setText("▶ 继续 (F11)")
        else:
            self.runner.request_resume()
            self.btn_pause.setText("⏸ 暂停 (F11)")

    def _stop_run(self):
        if self.runner is not None:
            self.runner.request_stop()

    def _on_progress(self, i: int, total: int):
        self.progress_label.setText(f"进度：{i} / {total}")

    def _on_finished(self, ok: bool):
        self.runner = None
        self.btn_run.setEnabled(True)
        self.btn_pause.setEnabled(False)
        self.btn_stop.setEnabled(False)
        self.append_log("=== 运行结束 ===")

    # ---------------------------- 录制 ---------------------------------- #
    def _toggle_record(self, checked: bool):
        if checked:
            if not self.recorder.available:
                self.btn_record.setChecked(False)
                QMessageBox.warning(self, "不支持", "全局录制仅在 Windows 上可用")
                return
            reply = QMessageBox.warning(
                self,
                "⚠ 反作弊警告",
                "全局录制使用了 Windows 低级钩子 (WH_MOUSE_LL / WH_KEYBOARD_LL)，\n"
                "这是外挂/键盘记录器的经典特征，ACE、EAC 等反作弊系统会检测到。\n\n"
                "在运行有反作弊保护的游戏时请勿使用录制功能。\n\n"
                "确定要开始录制吗？",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No,
            )
            if reply != QMessageBox.Yes:
                self.btn_record.setChecked(False)
                return
            self.recorder.start()
            self.btn_record.setText("■ 停止录制")
            self.append_log("● 录制中…（全局点击 / 按键将记录为步骤）")
        else:
            events = self.recorder.stop()
            self.btn_record.setText("● 开始录制")
            for ev in events:
                self.steps.append(ev)
            self._refresh_steps()
            self.append_log(f"■ 录制结束，新增 {len(events)} 步")

    def _on_recorded_event(self, ev: dict):
        # 边录边显示（步骤在 stop 时统一并入，这里只提示）
        self.append_log(f"录制 · {describe_step(ev)}")

    def _on_humanize_toggle(self, enabled: bool):
        self.humanize.enabled = enabled
        self.append_log(f"拟人化模式 {'✓ 已启用' if enabled else '✗ 已关闭'}")

    # ---------------------------- 捕获模板 ------------------------------ #
    def _capture_template(self):
        """把当前全屏抓一张，让用户保存为模板；简单实现（不做框选裁剪）。"""
        from automation import save_region_screenshot
        path, _ = QFileDialog.getSaveFileName(self, "保存模板图", "template.png", "PNG (*.png)")
        if not path:
            return
        self.showMinimized()
        QApplication.processEvents()
        time.sleep(0.4)
        try:
            save_region_screenshot(path, None)
            self.append_log(f"已保存全屏截图作为模板：{path}")
        except Exception as exc:
            self.append_log(f"❌ 截图失败：{exc}")
        finally:
            self.showNormal()

    # ---------------------------- 实时坐标 ------------------------------ #
    def _update_coord(self):
        # Win32 直读，无截屏、无延迟
        x, y = pointer.get_cursor_pos()
        self.coord_label.setText(f"{x}, {y}")
        rgb = pointer.get_pixel_color(x, y)
        if rgb:
            r, g, b = rgb
            self.color_label.setText(f"#{r:02X}{g:02X}{b:02X}")
            self.color_swatch.setStyleSheet(
                f"background:{QColor(r, g, b).name()}; border:1px solid #313650; border-radius:8px;"
            )

    # ---------------------------- 日志 ---------------------------------- #
    def append_log(self, msg: str):
        stamp = time.strftime("%H:%M:%S")
        self.log_view.appendPlainText(f"[{stamp}] {msg}")

    def closeEvent(self, event):
        self._stop_run()
        self.hotkeys.clear()
        QApplication.instance().removeNativeEventFilter(self.hotkeys)
        if self.recorder.available:
            self.recorder.stop()
        super().closeEvent(event)
