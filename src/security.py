"""
6号自动化助手 - security.py
[Reconstructed from PyArmor-protected bytecode]

This file was reconstructed through reverse engineering.
Function signatures, variable names, and string constants
are accurate. Implementation logic is reconstructed from
bytecode disassembly and API reference analysis.
"""

import ctypes
import os
import sys
import threading
import time

def clear_force_offline_reason():
    """清除强制下线原因（UI已显示后调用）"""
    pass

def get_api_secret_key():
    """运行时获取解密后的API密钥"""
    # References: bytes, decode
    pass

def get_force_offline_reason():
    """获取强制下线原因（服务端解绑/删除激活码时推送），返回None表示无强制下线"""
    pass

def init_integrity_check():
    """初始化完整性校验，返回hash供后续验证"""
    pass

def init_security(server_url, machine_id):
    """初始化安全模块
    在程序启动时调用
    
    Args:
        server_url: 服务器地址（用于心跳验证）
        machine_id: 机器ID（用于心跳验证）"""
    # References: init_integrity_check, init_time_check, getattr, sys, security_check_with_warning, exit, start_heartbeat
    pass

def init_time_check():
    """初始化时间检查"""
    # References: time, getattr, sys, os, path, join, dirname, executable, open, write
    pass

def is_heartbeat_valid():
    """检查心跳状态"""
    pass

def perform_full_security_check():
    """执行完整的安全检查"""
    # References: perform_security_check, verify_integrity, verify_time, is_heartbeat_valid
    pass

def perform_security_check():
    """执行安全检查
    返回: (is_safe: bool, reason: str)"""
    pass

def security_check_with_warning():
    """执行安全检查，如果不安全则显示警告"""
    # References: perform_security_check, ctypes, windll, user32, MessageBoxW, print
    pass

def start_heartbeat(server_url, machine_id, interval):
    """启动心跳验证"""
    # References: is_alive, threading, Thread, start
    pass

def stop_heartbeat():
    """停止心跳验证"""
    pass

def verify_integrity():
    """验证代码完整性"""
    # References: getattr, sys
    pass

def verify_time():
    """验证时间是否被篡改（增强版）"""
    # References: time, os, path, exists, open, int, read, strip, abs, write
    pass
