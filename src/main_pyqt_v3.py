"""
6号自动化助手 - main_pyqt_v3.py
[Reconstructed from PyArmor-protected bytecode]

This file was reconstructed through reverse engineering.
Function signatures, variable names, and string constants
are accurate. Implementation logic is reconstructed from
bytecode disassembly and API reference analysis.
"""

import base64
import copy
import ctypes
import datetime
import glob
import hashlib
import json
import os
import random
import string
import sys
import threading
import traceback
import webbrowser

import keyboard
import pyautogui
import requests

from PyQt5.QtWidgets import QApplication, QCheckBox, QColor, QComboBox, QCursor, QDialog, QFileDialog, QFont, QFormLayout, QFrame
# ... more Qt imports

class CoordOverlay:
    """
    """

    def closeEvent(self, event):
        # References: timer, stop, super, closeEvent
        # [Logic reconstructed from API references]
        pass

    def update_position(self):
        # References: CoordOverlay, pyautogui, position, label, setText, move
        # [Logic reconstructed from API references]
        pass

class MainWindow:
    """
    """

    def _append_log(self, text):
        # References: log_text, append, verticalScrollBar, setValue, maximum
        # [Logic reconstructed from API references]
        pass

    def _apply_countdown_style(self, remaining_secs):
        """根据剩余秒数设置倒计时样式颜色"""
        # References: activation_label, setStyleSheet
        # String: 'rgba(34, 197, 94, 0.3)'
        # String: '#86efac'
        # String: 'rgba(245, 158, 11, 0.3)'
        # [Logic reconstructed from API references]
        pass

    def _check_editable_updates(self):
        """检查可编辑配置是否有更新"""
        # References: web_server, get_updated_workflow, current_workflow, add_log, stop
        # String: '✅ 自定义配置已同步更新并保存'
        # [Logic reconstructed from API references]
        pass

    def _check_force_offline(self):
        """快速检查服务端强制下线通知（每5秒，配合10秒心跳实现近实时下线）"""
        # References: hasattr, activation, is_activated, get_force_offline_reason, clear_force_offline_reason, add_log, engine, is_running, stop_execution, update_activation_display
        # String: 'activation'
        # String: '⚠️ '
        # [Logic reconstructed from API references]
        pass

    def _copy_images_from_folder(self, folder):
        """从文件夹复制所有图片"""
        # References: shutil, os, listdir, _is_image_file, path, join, isfile, copy2, images_folder
        # [Logic reconstructed from API references]
        pass

    def _copy_workflows_from_folder(self, folder):
        """从文件夹复制所有配置文件（JSON 和加密 ENC）"""
        # References: shutil, os, listdir, lower, endswith, path, join, isfile, copy2, workflows_folder
        # [Logic reconstructed from API references]
        pass

    def _decrypt_config_file(self, filepath):
        """解密加密配置文件，返回 (配置数据, 是否可编辑)"""
        # References: base64, hashlib, cryptography.hazmat.primitives.ciphers, Cipher, algorithms, modes, cryptography.hazmat.backends, default_backend, bytes, sha256
        # String: 'rb'
        # String: '无效的加密文件格式'
        # String: '解密数据为空'
        # [Logic reconstructed from API references]
        pass

    def _do_detect_window(self):
        """实际执行窗口检测"""
        # References: ctypes, ctypes.wintypes, win32gui, win32process, psutil, wintypes, POINT, windll, user32, GetCursorPos
        # String: '(无标题)'
        # String: '✅ 检测成功！点击复制按钮可复制对应内容'
        # String: 'color: #10b981; font-size: 13px;'
        # [Logic reconstructed from API references]
        pass

    def _encrypt_and_save_config(self, data, filepath, is_editable):
        """加密并保存配置文件"""
        # References: base64, hashlib, cryptography.hazmat.primitives.ciphers, Cipher, algorithms, modes, cryptography.hazmat.backends, default_backend, current_workflow, get
        # String: '_enc_editable'
        # String: 'utf-8'
        # String: 'wb'
        # [Logic reconstructed from API references]
        pass

    def _extract_archive(self, archive_path, extract_to):
        """解压压缩包到指定目录"""
        # References: tempfile, os, path, basename, lower, endswith, zipfile, ZipFile, namelist, realpath
        # String: '.zip'
        # String: '⚠️ 检测到不安全的压缩包路径: '
        # String: '.rar'
        # [Logic reconstructed from API references]
        pass

    def _is_archive_file(self, filename):
        """判断是否是压缩包文件"""
        # References: lower, endswith
        # [Logic reconstructed from API references]
        pass

    def _is_image_file(self, filename):
        """判断是否是图片文件"""
        # References: lower, endswith
        # [Logic reconstructed from API references]
        pass

    def _on_screenshot_cancelled(self):
        """截图取消"""
        # References: show, screenshot_window
        # [Logic reconstructed from API references]
        pass

    def _on_screenshot_done(self, filepath):
        """截图完成"""
        # References: show, add_log, os, path, basename, screenshot_window
        # String: '截图已保存: '
        # [Logic reconstructed from API references]
        pass

    def _periodic_security_check(self):
        """定期安全检查（带容错+反Hook检测）"""
        # References: id, perform_full_security_check, add_log, engine, is_running, stop_execution, is_heartbeat_valid, getattr, start_heartbeat, requests
        # String: '⚠️ 检测到安全模块异常'
        # String: '__code__'
        # String: 'verify_signature'
        # [Logic reconstructed from API references]
        pass

    def _process_extracted_folder(self, folder):
        """处理解压后的文件夹，返回 (图片数, 配置数)"""
        # References: shutil, os, walk, path, basename, lower, join, _is_image_file, copy2, images_folder
        # String: 'images'
        # String: 'workflows'
        # String: '.json'
        # [Logic reconstructed from API references]
        pass

    def _refresh_hotkeys(self):
        """定时刷新快捷键，防止失效"""
        # References: register_hotkeys, Exception, print
        # String: '刷新快捷键失败: '
        # [Logic reconstructed from API references]
        pass

    def _save_current_workflow(self):
        """保存当前workflow到文件"""
        # References: current_workflow, hasattr, current_workflow_path, items, startswith, endswith, open, json, dump, Exception
        # String: 'current_workflow_path'
        # String: '.enc'
        # String: 'utf-8'
        # [Logic reconstructed from API references]
        pass

    def _show_import_result(self, images, workflows, errors):
        """显示导入结果"""
        # References: show_message, len, refresh_workflow_list
        # String: '导入失败'
        # String: '未找到可导入的文件\n\n支持的格式：\n• 图片：png, jpg, jpeg, bmp\n• 配置：json'
        # String: 'warning'
        # [Logic reconstructed from API references]
        pass

    def _start_editable_update_checker(self):
        """启动定时检查可编辑配置更新"""
        # References: hasattr, PyQt5.QtCore, QTimer, timeout, connect, _check_editable_updates, start
        # String: '_editable_check_timer'
        # [Logic reconstructed from API references]
        pass

    def _start_screenshot(self):
        """启动截图窗口"""
        # References: ScreenshotWindow, images_folder, screenshot_window, screenshot_taken, connect, screenshot_cancelled
        # [Logic reconstructed from API references]
        pass

    def _update_countdown(self):
        """更新倒计时"""
        # References: detect_countdown, detect_status_label, setText, countdown_timer, stop
        # String: '⏱️ '
        # String: ' 秒后检测，请将鼠标移到目标窗口...'
        # String: '🔍 正在检测...'
        # [Logic reconstructed from API references]
        pass

    def _update_expiry_countdown(self):
        """每秒更新到期倒计时显示"""
        # References: hasattr, activation, is_activated, stop, get_remaining_seconds, activation_label, setText, setStyleSheet, add_log, engine
        # String: 'activation'
        # String: '❌ 已过期'
        # [Logic reconstructed from API references]
        pass

    def _update_workflow_display(self):
        """更新工作流显示"""
        # References: current_workflow, get, sum, hasattr, len, config_stats_label, setText
        # String: 'groups'
        # String: 'config_stats_label'
        # String: 'default_group'
        # [Logic reconstructed from API references]
        pass

    def _verify_activation_integrity(self):
        """验证激活完整性（内联HMAC验证，防止函数Hook和属性篡改）"""
        # References: json, hmac, hashlib, os, path, exists, activation, activation_file, open, load
        # String: 'utf-8'
        # String: 'hmac'
        # String: 'machine_id'
        # [Logic reconstructed from API references]
        pass

    def add_log(self, message):
        """log_enabled"""
        # References: hasattr, log_enabled, datetime, now, strftime, log_signal, emit
        # String: '%H:%M:%S'
        # String: '] '
        # [Logic reconstructed from API references]
        pass

    def auto_clear_log(self):
        """自动清理日志"""
        # References: log_text, clear, add_log
        # String: '日志已自动清理（每6小时）'
        # [Logic reconstructed from API references]
        pass

    def check_activation(self):
        # References: activation, check_activation_status, update_activation_display, show_activation_dialog
        # [Logic reconstructed from API references]
        pass

    def check_activation_required(self):
        """检查激活状态（增强版：多重验证）"""
        # References: activation, is_activated, show_activation_dialog, perform_full_security_check, is_heartbeat_valid, add_log
        # String: '⚠️ 网络验证失败'
        # [Logic reconstructed from API references]
        pass

    def check_version(self):
        """检测软件版本更新"""
        # References: threading, Thread, start
        # [Logic reconstructed from API references]
        pass

    def clear_log(self):
        # References: log_text, clear
        # [Logic reconstructed from API references]
        pass

    def closeEvent(self, event):
        """coord_overlay"""
        # References: getattr, stop, hasattr, coord_overlay, close, mini_window, engine, web_server, hotkey_hooks, keyboard
        # String: 'mini_window'
        # [Logic reconstructed from API references]
        pass

    def copy_to_clipboard(self, text):
        """复制到剪贴板"""
        # References: PyQt5.QtWidgets, QApplication, clipboard, setText, detect_status_label, setStyleSheet
        # String: '📋 已复制: '
        # String: 'color: #6366f1; font-size: 13px;'
        # [Logic reconstructed from API references]
        pass

    def delete_selected_workflow(self):
        """删除选中的配置文件"""
        # References: config_combo, currentData, show_message, os, path, basename, PyQt5.QtWidgets, QMessageBox, setWindowTitle, setText
        # String: '提示'
        # String: '请先选择要删除的配置文件'
        # String: 'warning'
        # [Logic reconstructed from API references]
        pass

    def detect_window_info(self):
        """检测窗口信息"""
        # References: detect_countdown, detect_status_label, setText, setStyleSheet, window_info_frame, setVisible, PyQt5.QtCore, QTimer, countdown_timer, timeout
        # String: '⏱️ 3 秒后检测，请将鼠标移到目标窗口...'
        # String: 'color: #f59e0b; font-size: 13px;'
        # [Logic reconstructed from API references]
        pass

    def import_drag_enter(self, event):
        """拖拽进入事件"""
        # References: mimeData, hasUrls, acceptProposedAction
        # [Logic reconstructed from API references]
        pass

    def import_drop(self, event):
        """拖拽放下事件"""
        # References: mimeData, urls, toLocalFile, process_import_paths
        # [Logic reconstructed from API references]
        pass

    def load_hotkey_settings(self):
        """utf-8"""
        # References: os, path, exists, settings_file, open, json, load, hotkeys, update, Exception
        # String: 'hotkeys'
        # String: '加载快捷键设置失败: '
        # [Logic reconstructed from API references]
        pass

    def load_last_workflow(self):
        """加载上次的配置"""
        # References: os, path, exists, settings_file, open, json, load, get, load_workflow_file, Exception
        # String: 'utf-8'
        # String: 'last_workflow'
        # String: '加载上次配置失败: '
        # [Logic reconstructed from API references]
        pass

    def load_screenshot_settings(self):
        """加载截图设置"""
        # References: os, path, join, get_app_path, exists, open, json, load, screenshot_local_mode, setChecked
        # String: 'screenshot_settings.json'
        # String: 'utf-8'
        # String: 'local_mode'
        # [Logic reconstructed from API references]
        pass

    def load_selected_workflow(self):
        """加载选中的配置"""
        # References: check_activation_required, config_combo, currentData, show_message, load_workflow_file
        # String: '提示'
        # String: '请先选择配置文件'
        # String: 'warning'
        # [Logic reconstructed from API references]
        pass

    def load_workflow_file(self, filepath):
        """加载配置文件（支持加密 .enc 文件）"""
        # References: endswith, Exception, show_message, engine, load_workflow, current_workflow, current_workflow_path, get, os, path
        # String: '.enc'
        # String: '_encrypted'
        # String: '_enc_editable'
        # [Logic reconstructed from API references]
        pass

    def mouseMoveEvent(self, event):
        # References: buttons, Qt, LeftButton, move, globalPos
        # [Logic reconstructed from API references]
        pass

    def mousePressEvent(self, event):
        # References: button, Qt, LeftButton, globalPos, frameGeometry, topLeft
        # [Logic reconstructed from API references]
        pass

    def mouseReleaseEvent(self, event):
        # [Logic reconstructed from API references]
        pass

    def on_execution_complete(self):
        """暂停 (F11)"""
        # References: start_btn, setEnabled, stop_btn, pause_btn, setText, setToolTip
        # [Logic reconstructed from API references]
        pass

    def open_config_encryptor(self):
        """打开配置文件加密工具"""
        # References: PyQt5.QtWidgets, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog, QTextEdit, QGroupBox, PyQt5.QtCore
        # String: 'EncryptorDialog'
        # [Logic reconstructed from API references]
        pass

    def open_custom_config_editor(self):
        """打开自定义配置编辑器（仅用于enc加密配置）"""
        # References: check_activation_required, current_workflow, show_message, get, web_server, set_editable_config, get_url, webbrowser, open, add_log
        # String: '提示'
        # String: '请先加载配置文件'
        # String: 'warning'
        # [Logic reconstructed from API references]
        pass

    def open_editor(self):
        """_encrypted"""
        # References: check_activation_required, web_server, get_url, current_workflow_path, os, path, basename, current_workflow, get, set_current_workflow
        # String: '_enc_editable'
        # String: '提示'
        # String: '正式版加密配置不能在编辑器中打开'
        # [Logic reconstructed from API references]
        pass

    def open_screenshot_folder(self):
        """打开截图文件夹"""
        # References: os, path, join, get_app_path, exists, makedirs, startfile
        # String: 'jt'
        # [Logic reconstructed from API references]
        pass

    def process_import_paths(self, paths):
        """处理导入的路径列表"""
        # References: shutil, os, path, exists, isdir, basename, lower, join, listdir, isfile
        # String: 'images'
        # String: 'workflows'
        # String: ': '
        # [Logic reconstructed from API references]
        pass

    def refresh_workflow_list(self):
        """刷新配置文件列表"""
        # References: config_combo, clear, addItem, glob, os, path, join, workflows_folder, sorted, basename
        # String: '-- 请选择配置文件 --'
        # String: '*.json'
        # String: '*.enc'
        # [Logic reconstructed from API references]
        pass

    def register_hotkeys(self, silent):
        """screenshot"""
        # References: hotkey_hooks, keyboard, remove_hotkey, clear, hotkeys, get, add_hotkey, append, add_log, join
        # String: '截图='
        # String: 'start'
        # String: '开始='
        # [Logic reconstructed from API references]
        pass

    def save_log(self):
        """保存日志"""
        # References: QFileDialog, getSaveFileName, open, write, log_text, toPlainText, add_log
        # String: '文本文件 (*.txt)'
        # String: 'utf-8'
        # String: '日志已保存: '
        # [Logic reconstructed from API references]
        pass

    def save_screenshot_settings(self, dialog):
        """保存截图设置"""
        # References: screenshot_local_mode, isChecked, get, screenshot_position, currentIndex, screenshot_resolution, screenshot_max_count, value, screenshot_prefix, text
        # String: 'center'
        # String: 'top_left'
        # String: 'top_right'
        # [Logic reconstructed from API references]
        pass

    def save_settings(self, settings):
        """utf-8"""
        # References: os, path, exists, settings_file, open, json, load, update, dump, Exception
        # String: '保存设置失败: '
        # [Logic reconstructed from API references]
        pass

    def select_import_files(self):
        """点击选择文件导入"""
        # References: QFileDialog, setFileMode, ExistingFiles, setNameFilter, setWindowTitle, exec_, selectedFiles, process_import_paths
        # String: '选择要导入的文件或压缩包'
        # [Logic reconstructed from API references]
        pass

    def setup_home_page(self):
        """主页 - 配置选择和信息"""
        # References: QWidget, QVBoxLayout, setContentsMargins, setSpacing, QLabel, setObjectName, addWidget, QFrame, QHBoxLayout, QComboBox
        # String: '主页'
        # String: 'pageTitle'
        # String: 'configSelector'
        # [Logic reconstructed from API references]
        pass

    def setup_log_page(self):
        """日志页面"""
        # References: QWidget, QVBoxLayout, setContentsMargins, setSpacing, QLabel, setObjectName, addWidget, QFrame, QHBoxLayout, addStretch
        # String: '执行日志'
        # String: 'pageTitle'
        # String: 'logPanel'
        # [Logic reconstructed from API references]
        pass

    def setup_main_content(self, parent_layout):
        """mainContent"""
        # References: QFrame, setObjectName, QVBoxLayout, setContentsMargins, setSpacing, setup_window_controls, QStackedWidget, pages, setup_home_page, setup_log_page
        # [Logic reconstructed from API references]
        pass

    def setup_sidebar(self, parent_layout):
        """sidebar"""
        # References: QFrame, setObjectName, QVBoxLayout, setContentsMargins, setSpacing, QWidget, QHBoxLayout, QLabel, os, path
        # String: '006.ico'
        # String: '6号助手'
        # String: 'sidebarTitle'
        # [Logic reconstructed from API references]
        pass

    def setup_tools_page(self):
        """工具页面"""
        # References: QWidget, QVBoxLayout, setContentsMargins, setSpacing, QLabel, setObjectName, addWidget, QHBoxLayout, QPushButton, setFixedSize
        # String: '工具箱'
        # String: 'pageTitle'
        # String: '📷 截图'
        # [Logic reconstructed from API references]
        pass

    def setup_ui(self):
        # References: QWidget, setCentralWidget, QHBoxLayout, setContentsMargins, setSpacing, setup_sidebar, setup_main_content
        # [Logic reconstructed from API references]
        pass

    def setup_window_controls(self, parent_layout):
        """windowControls"""
        # References: QFrame, setObjectName, setFixedHeight, QHBoxLayout, setContentsMargins, addStretch, QPushButton, clicked, connect, showMinimized
        # String: 'closeBtn'
        # [Logic reconstructed from API references]
        pass

    def show_activation_dialog(self):
        """软件激活"""
        # References: QDialog, setWindowTitle, setWindowFlags, windowFlags, Qt, FramelessWindowHint, setFixedSize, setStyleSheet, QVBoxLayout, setContentsMargins
        # String: 'background: transparent; font-size: 14px;'
        # String: '🔐 软件激活'
        # [Logic reconstructed from API references]
        pass

    def show_dpi_setting(self):
        """显示DPI设置对话框"""
        # References: PyQt5.QtWidgets, QInputDialog, engine, fps_user_dpi, fps_standard_dpi, getInt, save_fps_dpi_config, QMessageBox, information, int
        # String: '设置鼠标DPI'
        # String: '请输入你的鼠标DPI值:\n\n当前DPI: '
        # String: '\n标准DPI: '
        # [Logic reconstructed from API references]
        pass

    def show_hotkey_settings(self):
        """快捷键设置"""
        # References: QDialog, setWindowTitle, setWindowFlags, windowFlags, Qt, FramelessWindowHint, setFixedSize, setStyleSheet, QVBoxLayout, setContentsMargins
        # String: 'background: transparent; font-size: 12px;'
        # String: '⌨️ 快捷键设置'
        # [Logic reconstructed from API references]
        pass

    def show_screenshot_settings(self):
        """显示截图设置对话框"""
        # References: PyQt5.QtWidgets, QGroupBox, QFormLayout, QSpinBox, QDialog, QCheckBox, setWindowTitle, setFixedSize, setStyleSheet, QVBoxLayout
        # String: '截图设置'
        # String: '📁 本地保存截图'
        # [Logic reconstructed from API references]
        pass

    def show_update_notice(self, latest_version):
        """显示更新提示"""
        # References: show_message, CURRENT_VERSION
        # String: '🆕 版本更新提示'
        # String: '发现新版本！\n\n当前版本: '
        # String: '\n最新版本: '
        # [Logic reconstructed from API references]
        pass

    def show_workflow_detail(self):
        """查看配置详情"""
        # References: current_workflow, get, webbrowser, open
        # String: 'detail_url'
        # [Logic reconstructed from API references]
        pass

    def start_execution(self):
        """⚠️ 激活验证失败"""
        # References: engine, is_running, check_activation_required, add_log, hasattr, security_timer, isActive, id, perform_full_security_check, requests
        # String: 'security_timer'
        # String: '⚠️ 安全检查异常'
        # String: '⚠️ 安全模块异常'
        # [Logic reconstructed from API references]
        pass

    def start_log_cleanup_timer(self):
        """启动日志定时清理（每6小时）"""
        # References: QTimer, log_cleanup_timer, timeout, connect, auto_clear_log, start
        # [Logic reconstructed from API references]
        pass

    def stop_execution(self):
        """已停止执行"""
        # References: engine, stop, add_log, on_execution_complete
        # [Logic reconstructed from API references]
        pass

    def switch_page(self, index):
        """active"""
        # References: pages, setCurrentIndex, enumerate, nav_buttons, setProperty, setStyle, style
        # [Logic reconstructed from API references]
        pass

    def switch_to_mini_mode(self):
        """切换到迷你模式"""
        # References: geometry, main_geometry, hide, MiniWindow, mini_window, show
        # [Logic reconstructed from API references]
        pass

    def switch_to_normal_mode(self):
        """从迷你模式切换回正常模式"""
        # References: hasattr, mini_window, close, setGeometry, main_geometry, show
        # String: 'mini_window'
        # String: 'main_geometry'
        # [Logic reconstructed from API references]
        pass

    def take_screenshot(self):
        """截图 - 使用PyQt5实现"""
        # References: check_activation_required, hide, QTimer, singleShot
        # [Logic reconstructed from API references]
        pass

    def toggle_coord_display(self):
        """切换实时坐标显示"""
        # References: hasattr, coord_overlay, CoordOverlay, show, coord_btn, setText, setStyleSheet, close
        # String: 'coord_overlay'
        # String: '📍 关闭坐标'
        # String: 'background-color: #ef4444; color: white;'
        # [Logic reconstructed from API references]
        pass

    def toggle_log_enabled(self):
        """切换日志开关"""
        # References: log_enabled, toggle_log_btn, setText, setStyleSheet
        # String: '🔔 开启'
        # String: '🔕 关闭'
        # String: 'background: #dc2626;'
        # [Logic reconstructed from API references]
        pass

    def toggle_maximize(self):
        # References: isMaximized, showNormal, max_btn, setText, showMaximized
        # [Logic reconstructed from API references]
        pass

    def toggle_pause(self):
        """切换暂停状态"""
        # References: engine, is_running, toggle_pause, pause_btn, setText, setToolTip
        # String: '继续 (F11)'
        # String: '暂停 (F11)'
        # [Logic reconstructed from API references]
        pass

    def toggle_topmost(self):
        """切换窗口置顶"""
        # References: topmost_btn, isChecked, setWindowFlags, windowFlags, Qt, WindowStaysOnTopHint, add_log, show
        # String: '窗口已置顶'
        # String: '已取消置顶'
        # [Logic reconstructed from API references]
        pass

    def update_activation_display(self):
        """✅ 已激活
    ⏳"""
        # References: activation, is_activated, get_remaining_time, activation_label, setText, get_remaining_seconds, isActive, start, stop, setStyleSheet
        # String: '❌ 未激活'
        # [Logic reconstructed from API references]
        pass

class MiniWindow:
    """
    """

    def closeEvent(self, event):
        # References: status_timer, stop, accept
        # [Logic reconstructed from API references]
        pass

    def eventFilter(self, obj, event):
        """事件过滤器 - 处理拖拽调整大小"""
        # References: resize_handle, type, MouseButtonPress, button, Qt, LeftButton, resizing, globalPos, y, resize_start_y
        # [Logic reconstructed from API references]
        pass

    def mouseMoveEvent(self, event):
        """鼠标移动事件 - 拖动窗口"""
        # References: drag_position, buttons, Qt, LeftButton, resizing, move, globalPos, accept
        # [Logic reconstructed from API references]
        pass

    def mousePressEvent(self, event):
        """鼠标按下事件 - 拖动窗口"""
        # References: button, Qt, LeftButton, resizing, globalPos, frameGeometry, topLeft, drag_position, accept
        # [Logic reconstructed from API references]
        pass

    def mouseReleaseEvent(self, event):
        """鼠标释放事件"""
        # References: drag_position, accept
        # [Logic reconstructed from API references]
        pass

    def on_expand(self):
        """展开到正常模式"""
        # References: status_timer, stop, main_window, switch_to_normal_mode
        # [Logic reconstructed from API references]
        pass

    def on_pause(self):
        """暂停/恢复执行"""
        # References: main_window, toggle_pause, sync_status
        # [Logic reconstructed from API references]
        pass

    def on_start(self):
        """开始执行"""
        # References: main_window, start_execution, sync_status
        # [Logic reconstructed from API references]
        pass

    def on_stop(self):
        """停止执行"""
        # References: main_window, stop_execution, sync_status
        # [Logic reconstructed from API references]
        pass

    def setup_ui(self):
        """QFrame#mainContainer {
    
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
    
                        stop:0 #1a1a2e, stop:1 #2a2a4e);
    
                    border-radius: 12px;
    
                    border: 1px solid #3a3a5a;
    
                }"""
        # References: QVBoxLayout, setContentsMargins, setSpacing, QFrame, main_container, setStyleSheet, setObjectName, QHBoxLayout, QLabel, setCursor
        # String: 'mainContainer'
        # String: 'color: #ef4444; font-size: 14px;'
        # [Logic reconstructed from API references]
        pass

    def sync_log(self):
        """同步主窗口日志"""
        # References: hasattr, main_window, log_text, toPlainText, split, len, mini_log_text, setText, join, verticalScrollBar
        # String: 'log_text'
        # [Logic reconstructed from API references]
        pass

    def sync_status(self):
        """同步主窗口状态"""
        # References: main_window, engine, is_running, is_paused, status_indicator, setStyleSheet, start_btn, setEnabled, stop_btn, pause_btn
        # String: 'color: #f59e0b; font-size: 14px;'
        # String: 'color: #22c55e; font-size: 14px;'
        # String: 'color: #ef4444; font-size: 14px;'
        # [Logic reconstructed from API references]
        pass

    def toggle_log_panel(self):
        """切换日志面板显示"""
        # References: log_panel, isVisible, setVisible, setFixedHeight, log_panel_height, setFixedSize, sync_log
        # [Logic reconstructed from API references]
        pass

    def toggle_topmost(self):
        """切换置顶"""
        # References: is_topmost, setWindowFlags, windowFlags, Qt, WindowStaysOnTopHint, topmost_btn, setStyleSheet, show
        # [Logic reconstructed from API references]
        pass

class ScreenshotWindow:
    """
    """

    def cancel(self):
        # References: close, screenshot_cancelled, emit
        # [Logic reconstructed from API references]
        pass

    def do_save(self, copy_to_clipboard):
        """保存截图
    
    
    
    Args:
    
        copy_to_clipboard: 是否同时复制图片名和坐标到剪贴板"""
        # References: selected_rect, cancel, screenshot, copy, datetime, now, strftime, os, path, join
        # String: '%Y%m%d_%H%M%S'
        # String: 'screenshot_'
        # String: '.png'
        # [Logic reconstructed from API references]
        pass

    def do_save_and_copy(self):
        """保存截图并复制图片名和坐标到剪贴板"""
        # References: do_save
        # [Logic reconstructed from API references]
        pass

    def keyPressEvent(self, event):
        # References: key, Qt, Key_Escape, cancel, Key_Return, Key_Enter, selection_done, do_save
        # [Logic reconstructed from API references]
        pass

    def mouseMoveEvent(self, event):
        # References: is_selecting, start_pos, rubber_band, setGeometry, QRect, pos, normalized
        # [Logic reconstructed from API references]
        pass

    def mousePressEvent(self, event):
        # References: selection_done, button, Qt, LeftButton, pos, start_pos, rubber_band, setGeometry, QRect, QSize
        # [Logic reconstructed from API references]
        pass

    def mouseReleaseEvent(self, event):
        # References: button, Qt, LeftButton, is_selecting, pos, end_pos, show_confirm
        # [Logic reconstructed from API references]
        pass

    def paintEvent(self, event):
        """Microsoft YaHei UI"""
        # References: QPainter, drawPixmap, screenshot, fillRect, rect, QColor, selection_done, selected_rect, setPen, drawRect
        # String: '🖱️ 按住拖动选择区域 | ESC 取消 | 右键 取消'
        # [Logic reconstructed from API references]
        pass

    def show_confirm(self):
        """显示确认按钮"""
        # References: start_pos, end_pos, cancel, QRect, normalized, width, height, selected_rect, selection_done, rubber_band
        # String: '选区尺寸: '
        # String: ' x '
        # String: ' 像素'
        # [Logic reconstructed from API references]
        pass

def generate_random_title():
    """每次启动生成随机窗口标题"""
    # References: random, choice, join, choices, string, digits, randint
    pass

def get_app_path():
    """获取应用程序所在目录（兼容exe打包）"""
    # References: getattr, sys, os, path, dirname, executable, abspath
    pass

def get_crash_log_path():
    """获取崩溃日志路径"""
    # References: getattr, sys, os, path, join, dirname, executable, abspath
    pass

def main():
    """frozen"""
    # References: security, init_security, ImportError, getattr, sys, RuntimeError, QApplication, setAttribute, Qt, AA_EnableHighDpiScaling
    pass

def show_error_msgbox(title, message):
    """显示错误消息框（不依赖PyQt）"""
    # References: ctypes, windll, user32, MessageBoxW
    pass

def show_message(parent, title, text, msg_type):
    """显示自定义样式的消息框"""
    # References: QMessageBox, setWindowTitle, setText, setStyleSheet, MSG_BOX_STYLE, setIcon, Information, Warning, Critical, Question
    pass

def write_crash_log(error_msg):
    """写入崩溃日志"""
    # References: get_crash_log_path, open, write, datetime, now, strftime
    pass
