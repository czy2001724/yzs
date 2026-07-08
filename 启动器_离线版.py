"""
6号自动化助手 - 去验证/离线启动器
完全移除联网验证、激活检查、安全检测、心跳验证
公司内部使用，直接加载JSON流程文件即可自动化
"""
import sys, os

# 添加解包后的代码路径
EXTRACT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "6hzsv2.23.exe_extracted")
if not os.path.exists(EXTRACT_DIR):
    # 如果在 exe 同目录找不到，尝试常见路径
    EXTRACT_DIR = r"C:\Users\1\Downloads\Telegram Desktop\6hzsv2.23.exe_extracted"

sys.path.insert(0, EXTRACT_DIR)
os.chdir(EXTRACT_DIR)

import pyarmor_runtime_011372

# ========== PATCH: 安全模块 - 全部变 no-op ==========
import security
security.init_security              = lambda *a, **kw: None
security.perform_security_check     = lambda: (True, '')
security.perform_full_security_check = lambda: (True, '')
security.security_check_with_warning = lambda: None
security.start_heartbeat            = lambda *a, **kw: None
security.stop_heartbeat             = lambda: None
security.verify_integrity           = lambda: True
security.verify_time                = lambda: True
security.is_heartbeat_valid         = lambda: True
security.init_integrity_check       = lambda: None
security.init_time_check            = lambda: None
security._is_debugger_present       = lambda: False
security._check_suspicious_processes = lambda: (False, '')
security._check_loaded_dlls         = lambda: (False, '')
security._calculate_exe_hash        = lambda: '0'*64
security.clear_force_offline_reason = lambda: None
security.get_force_offline_reason   = lambda: None
security.get_api_secret_key         = lambda: 'OFFLINE_MODE'
security._SUSPICIOUS_PROCESSES      = []
security._SUSPICIOUS_DLLS           = []
security._VM_PROCESSES              = []

# ========== PATCH: 激活模块 - 永久激活 ==========
import activation
class FakeActivation:
    """模拟永久激活状态"""
    is_activated = True
    activation_code = "OFFLINE-INTERNAL-USE"
    activation_expiry = "2099-12-31T23:59:59"
    OFFLINE_MAX_MINUTES = 999999
    
    @staticmethod
    def check_activation_required(): return False
    @staticmethod
    def _verify_activation_integrity(): return True
    @staticmethod
    def get_remaining_time(): return "永久有效 (内部版)"
    @staticmethod
    def get_remaining_seconds(): return 999999999
    @staticmethod
    def is_heartbeat_valid(): return True
    @staticmethod
    def perform_security_check(): return (True, '')
    @staticmethod
    def start_heartbeat(*a, **kw): pass
    @staticmethod
    def get_api_secret_key(): return 'OFFLINE_MODE'
    @staticmethod
    def get_work_folder(): return os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else EXTRACT_DIR
    @staticmethod
    def get_machine_id(): return 'INTERNAL-USE'
    @staticmethod
    def get_dynamic_api_path(*a, **kw): return ('', '', '')
    @staticmethod
    def get_config_key(): return (False, None, '离线模式')
    @staticmethod
    def get_exec_token(): return (False, None, '离线模式')
    @staticmethod
    def verify_signature(*a, **kw): return True
    @staticmethod
    def _generate_local_hmac(*a, **kw): return b''
    @staticmethod
    def _verify_local_hmac(*a, **kw): return True

# 替换 ActivationManager 类的关键方法
for name in dir(FakeActivation):
    if not name.startswith('_'):
        setattr(activation.ActivationManager, name, getattr(FakeActivation, name))

activation.is_heartbeat_valid = lambda: True
activation.perform_security_check = lambda: (True, '')
activation.start_heartbeat = lambda *a, **kw: None
activation.verify_signature = lambda *a, **kw: True

# ========== PATCH: 主程序 - 禁用版本检查 ==========
import main_pyqt_v3
main_pyqt_v3.VERSION_CHECK_URL = 'http://127.0.0.1:1/nonexistent'

# ========== 启动 ==========
print("=" * 50)
print("6号自动化助手 - 内部离线版")
print("已移除: 激活验证 / 安全检测 / 网络心跳 / 版本检查")
print("=" * 50)

main_pyqt_v3.main()
