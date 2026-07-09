"""
6号自动化助手 - 本地验证版启动器
服务器指向 localhost:5000
"""
import sys, os

# Qt DLL 路径 (PyInstaller 冻结环境)
if getattr(sys, 'frozen', False):
    base = sys._MEIPASS if hasattr(sys, '_MEIPASS') else os.path.dirname(sys.executable)
    qt_plugin = os.path.join(base, 'PyQt5', 'Qt5', 'plugins')
    if os.path.exists(qt_plugin):
        os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(qt_plugin, 'platforms')
        os.environ['QT_PLUGIN_PATH'] = qt_plugin
    os.add_dll_directory(os.path.join(base, 'PyQt5', 'Qt5', 'bin'))
    os.add_dll_directory(os.path.join(base, 'pywin32_system32'))
    os.add_dll_directory(base)

APP_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, APP_DIR)
import ctypes, hashlib, base64, time, threading, subprocess, platform, json, struct
import pyarmor_runtime_011372

# 读取本地公钥
with open(os.path.join(APP_DIR, 'local_server_public.pem'), 'r') as f:
    NEW_PUBLIC_KEY = f.read()

# ===== 激活模块 =====
import activation
activation.SERVER_PUBLIC_KEY_PEM = NEW_PUBLIC_KEY

_orig_am_init = activation.ActivationManager.__init__
def _wrapped_am_init(self, *a, **kw):
    _orig_am_init(self, *a, **kw)
    self.server_url = 'http://127.0.0.1:5000/api'
    self._pin_verified = True
activation.ActivationManager.__init__ = _wrapped_am_init

activation.ActivationManager.verify_signature = lambda *a, **kw: True
activation.verify_signature = lambda *a, **kw: True
activation.ActivationManager._verify_cert_pin = lambda *a, **kw: True

# ===== 安全模块 =====
import security
security._is_debugger_present = lambda: False
security._check_suspicious_processes = lambda: (False, '')
security._check_loaded_dlls = lambda: (False, '')
security.start_heartbeat = lambda *a, **kw: None
security.stop_heartbeat = lambda: None
security.is_heartbeat_valid = lambda: True
security.init_security = lambda *a, **kw: None

# ===== 主程序 =====
import main_pyqt_v3
main_pyqt_v3.VERSION_CHECK_URL = 'http://127.0.0.1:5000/6hao.html'
main_pyqt_v3.MainWindow._verify_activation_integrity = lambda self: True
main_pyqt_v3.MainWindow.check_activation_required = lambda self: True
main_pyqt_v3.MainWindow.check_activation = lambda self: None
main_pyqt_v3.MainWindow.show_activation_dialog = lambda self: None
main_pyqt_v3.MainWindow.update_activation_display = lambda self: None
main_pyqt_v3.MainWindow.perform_full_security_check = lambda self: (True, '')

# ===== 启动 =====
print("=" * 50)
print("  6号自动化助手 v2.23 - 本地验证版")
print("  服务器: http://127.0.0.1:5000")
print("  激活码: INTERNAL-001 / ADMIN-KEY / 6HZS-FREE")
print("=" * 50)
main_pyqt_v3.main()
