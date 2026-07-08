"""
6号自动化助手 - automation.py
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
import hashlib
import io
import json
import math
import os
import random
import sys
import threading
import time

import PIL
import cv2
import keyboard
import pyautogui
import requests

class AutomationEngine:
    """
    """

    def _cleanup_old_screenshots(self, folder, prefix, max_count):
        """清理旧截图，保留最新的max_count张"""
        # References: os, listdir, startswith, endswith, path, join, append, getctime, sort, len
        # String: '.png'
        # String: '.jpg'
        # String: '🗑️ 已删除旧截图: '
        # [Logic reconstructed from API references]
        pass

    def _execute_action(self, action, ref_x, ref_y):
        """执行单个动作（用于变换识别的动作序列）"""
        # References: get, pyautogui, click, log, keyboard, press_and_release, time, sleep, Exception
        # String: 'type'
        # String: 'delay_after'
        # String: 'click'
        # [Logic reconstructed from API references]
        pass

    def _find_image_in_region(self, image_name, region, confidence, color_match):
        """在指定区域内识别图片（支持多尺度匹配，适应不同DPI/缩放）
    
    
    
    Args:
    
        image_name: 图片文件名
    
        region: 区域坐标 {x, y, width, height}
    
        confidence: 置信度
    
        color_match: 是否使用彩色匹配（区分颜色）"""
        # References: os, path, join, images_folder, exists, PIL, ImageGrab, grab, np, array
        # String: 'width'
        # String: 'height'
        # String: 'color'
        # [Logic reconstructed from API references]
        pass

    def _find_image_safe(self, image_name, confidence):
        """线程安全的图片识别（用于常驻任务）"""
        # References: os, path, join, images_folder, exists, PIL, ImageGrab, grab, np, array
        # [Logic reconstructed from API references]
        pass

    def _handle_image_result(self, step, success, action_name):
        """处理图片识别类步骤的成功/失败结果
    
    
    
    Args:
    
        step: 步骤配置
    
        success: 是否成功
    
        action_name: 操作名称（用于日志）
    
        
    
    Returns:
    
        bool: 是否成功（可能被修改）"""
        # References: get, log, is_running, jump_to_group
        # String: 'on_success'
        # String: 'continue'
        # String: 'stop'
        # [Logic reconstructed from API references]
        pass

    def _humanize_delay(self):
        """添加人类化随机延迟"""
        # References: humanize_enabled, random, uniform, humanize_delay_range, time, sleep
        # [Logic reconstructed from API references]
        pass

    def _humanize_position(self, x, y):
        """添加人类化位置偏移"""
        # References: humanize_enabled, humanize_position_range, random, randint
        # [Logic reconstructed from API references]
        pass

    def _load_fps_dpi_config(self):
        """加载FPS DPI配置"""
        # References: os, path, exists, fps_config_file, open, json, load, get, fps_standard_dpi
        # String: 'utf-8'
        # String: 'user_dpi'
        # [Logic reconstructed from API references]
        pass

    def _load_push_pack(self):
        """从加密包读取推送图片配置"""
        # References: hmac, hashlib, os, path, join, get_app_path, exists, hasattr, open, read
        # String: 'push_images.dat'
        # String: '_push_pack_cache'
        # String: 'rb'
        # [Logic reconstructed from API references]
        pass

    def _smooth_move_to(self, target_x, target_y, duration):
        """丝滑贝塞尔曲线鼠标移动
    
    
    
    使用二次贝塞尔曲线实现自然的鼠标移动轨迹"""
        # References: random, math, pyautogui, position, sqrt, moveTo, max, min, int, atan2
        # [Logic reconstructed from API references]
        pass

    def activate_window(self, process_name):
        """激活/切换到指定窗口"""
        # References: win32gui, win32con, get_window_by_process, log, IsIconic, ShowWindow, SW_RESTORE, SetForegroundWindow, Exception
        # String: '未找到程序窗口: '
        # String: '切换到窗口: '
        # String: '切换窗口失败: '
        # [Logic reconstructed from API references]
        pass

    def activate_window_v2(self, find_by, target):
        """激活/切换到指定窗口（支持多种查找方式）"""
        # References: win32gui, win32con, find_window, log, get, IsIconic, ShowWindow, SW_RESTORE, SetForegroundWindow, Exception
        # String: '进程名'
        # String: '窗口标题'
        # String: 'PID'
        # [Logic reconstructed from API references]
        pass

    def close_process(self, process_name):
        """强制关闭程序"""
        # References: close_process_v2
        # String: 'process_name'
        # [Logic reconstructed from API references]
        pass

    def close_process_v2(self, find_by, target):
        """强制关闭程序（支持多种查找方式）"""
        # References: find_process, kill, log, get, Exception
        # String: '进程名'
        # String: '窗口标题'
        # String: 'PID'
        # [Logic reconstructed from API references]
        pass

    def execute_change_detection(self, step):
        """执行变换识别（非常驻模式，在超时时间内检测多区域）
    
    
    
    按优先级检测多个区域，检测到就执行对应动作序列"""
        # References: get, log, join, len, time, is_running, jump_to_group, is_paused, sleep, append
        # String: 'regions'
        # String: '⚠️ 变换识别：未配置监控区域'
        # String: 'timeout'
        # [Logic reconstructed from API references]
        pass

    def execute_color_check(self, step):
        """执行颜色识别
    
    
    
    检测指定位置的颜色是否与目标颜色匹配（支持容差）
    
    支持循环检测模式：在超时时间内按间隔循环检测
    
    
    
    Args:
    
        step: 包含以下参数
    
            - x, y: 检测坐标
    
            - target_color: 目标颜色 [R, G, B]
    
            - tolerance: 颜色容差（默认30）
    
            - sample_size: 采样区域大小（默认3，取3x3像素平均值）
    
            - timeout: 超时时间（秒），0表示只检测一次（默认0）
    
            - interval: 检测间隔（秒），默认0.5
    
            - on_match: 匹配时动作 (continue/stop/jump)
    
            - on_mismatch: 不匹配时动作 (continue/stop/jump)
    
            - on_timeout: 超时时动作 (continue/stop/jump)"""
        # References: get, isinstance, str, startswith, int, PIL, ImageGrab, time, np, array
        # String: 'target_color'
        # String: 'tolerance'
        # String: 'sample_size'
        # [Logic reconstructed from API references]
        pass

    def execute_group(self, group, group_index):
        """执行单个组合
    
    
    
    Args:
    
        group: 组合配置
    
        group_index: 组合索引
    
        
    
    Returns:
    
        bool: 是否正常完成（非跳转）"""
        # References: stop_continuous_tasks, get, humanize_enabled, humanize_position_range, humanize_delay_range, log, int, current_group, jump_to_group, start_continuous_task
        # String: 'name'
        # String: '组合 '
        # String: 'steps'
        # [Logic reconstructed from API references]
        pass

    def execute_groups(self, workflow, start_group):
        """执行多组合工作流
    
    
    
    Args:
    
        workflow: 包含groups数组的工作流配置
    
        start_group: 起始组合索引（默认使用配置中的default_group）
    
    
    
    执行逻辑：
    
        - 从默认组合开始执行
    
        - 组合执行完后，如果有跳转配置则跳转，否则停止
    
        - 不会自动执行下一个组合"""
        # References: is_running, is_paused, jump_to_group, call_stack, return_from_call, get, log, len, execute_group, pop
        # String: 'groups'
        # String: 'steps'
        # String: 'name'
        # [Logic reconstructed from API references]
        pass

    def execute_pixel_position(self, step):
        """像素级定位 - 通过图片识别和WASD按键调整位置
    
    Args:
        step: 包含以下参数
            - image: 参考图片名
            - target_x, target_y: 目标坐标
            - tolerance: 误差范围（像素）
            - ms_per_pixel: 每像素对应的按键时长（毫秒）
            - confidence: 图片识别置信度
            - max_attempts: 最大调整次数
            - key_up, key_down, key_left, key_right: WASD按键"""
        # References: keyboard, get, log, is_running, find_image, time, sleep, abs, press, release
        # String: 'image'
        # String: 'target_x'
        # String: 'target_y'
        # [Logic reconstructed from API references]
        pass

    def execute_step(self, step):
        """执行单个步骤"""
        # References: wait_if_paused, get, is_running, is_paused, min, time, sleep, mouse_click_current, mouse_double_click_current, mouse_right_click_current
        # String: 'type'
        # String: 'delay'
        # String: 'click'
        # [Logic reconstructed from API references]
        pass

    def execute_workflow(self, workflow, loop_count):
        """执行工作流"""
        # References: is_running, is_paused, get, log, range, enumerate, time, sleep, current_step, execute_step
        # String: 'name'
        # String: '未命名流程'
        # String: 'steps'
        # [Logic reconstructed from API references]
        pass

    def find_all_images(self, image_name, confidence, region):
        """查找所有匹配的图片位置"""
        # References: get_image_path, os, path, exists, log, pyautogui, screenshot, np, array, cv2
        # String: '图片不存在: '
        # String: '找到 '
        # String: ' 个匹配: '
        # [Logic reconstructed from API references]
        pass

    def find_image(self, image_name, confidence, region):
        """查找图片位置"""
        # References: get_image_path, os, path, exists, log, pyautogui, screenshot, np, array, cv2
        # String: '图片不存在: '
        # String: '无法加载图片: '
        # String: '找到图片 '
        # [Logic reconstructed from API references]
        pass

    def find_process(self, find_by, target):
        """通用进程查找函数（用于关闭进程等）
    
    
    
    Args:
    
        find_by: 查找方式 - 'process_name'(进程名), 'window_title'(窗口标题), 'pid'(进程ID)
    
        target: 查找目标
    
        
    
    Returns:
    
        list: 匹配的进程列表"""
        # References: psutil, win32gui, win32process, Process, int, append, process_iter, info, lower, set
        # String: 'pid'
        # String: 'process_name'
        # String: 'name'
        # [Logic reconstructed from API references]
        pass

    def find_window(self, find_by, target):
        """通用窗口查找函数
    
    
    
    Args:
    
        find_by: 查找方式 - 'process_name'(进程名), 'window_title'(窗口标题), 'pid'(进程ID)
    
        target: 查找目标
    
        
    
    Returns:
    
        hwnd: 窗口句柄，未找到返回 None"""
        # References: win32gui, win32process, psutil, EnumWindows, Exception, log
        # String: '查找窗口失败: '
        # [Logic reconstructed from API references]
        pass

    def fps_move(self, dx, dy, duration, steps):
        """FPS视角移动 - 相对鼠标移动
    
    
    
    用于FPS游戏视角控制，通过相对移动实现视角转动
    
    配置值基于标准DPI(1000)编写，自动根据用户DPI换算
    
    
    
    Args:
    
        dx: 水平移动距离（像素），正值向右转，负值向左转
    
        dy: 垂直移动距离（像素），正值向下看，负值向上看
    
        duration: 移动持续时间（秒）
    
        steps: 移动分段数（越多越平滑）"""
        # References: ctypes, time, get_fps_dpi_multiplier, windll, user32, mouse_event, int, range, sleep, log
        # String: 'FPS视角移动: 水平'
        # String: 'px 垂直'
        # String: 'px (DPI倍率:'
        # [Logic reconstructed from API references]
        pass

    def get_fps_dpi_multiplier(self):
        """获取FPS DPI倍率（标准DPI / 用户DPI）"""
        # References: fps_standard_dpi, fps_user_dpi
        # [Logic reconstructed from API references]
        pass

    def get_image_path(self, image_name):
        """获取图片完整路径"""
        # References: os, path, isabs, join, images_folder
        # [Logic reconstructed from API references]
        pass

    def get_window_by_process(self, process_name):
        """根据进程名获取窗口句柄（兼容旧代码）"""
        # References: find_window
        # String: 'process_name'
        # [Logic reconstructed from API references]
        pass

    def image_click(self, image_name, confidence, offset_x, offset_y, wait_time, max_wait, button, click_delay):
        """图像识别并点击
    
    
    
    Args:
    
        click_delay: 鼠标移动到目标后等待多少秒再点击（默认1秒）"""
        # References: time, is_running, jump_to_group, find_image, mouse_move, log, sleep, mouse_click_current
        # String: '移动到目标位置 ('
        # String: ', '
        # String: ')，等待 '
        # [Logic reconstructed from API references]
        pass

    def image_click_ocr(self, image_name, ocr_text, confidence, offset_x, offset_y, max_wait, button, click_delay, ocr_expand):
        """图像识别 + OCR 验证后点击
    
    
    
    Args:
    
        image_name: 图片文件名
    
        ocr_text: 需要验证的文字（支持部分匹配）
    
        confidence: 图片匹配置信度
    
        offset_x, offset_y: 点击偏移
    
        max_wait: 最大等待时间
    
        button: 鼠标按键
    
        click_delay: 点击前延迟
    
        ocr_expand: OCR 识别区域扩展像素（向四周扩展）"""
        # References: time, os, path, join, images_folder, exists, log, load_image_cv2, cv2, IMREAD_COLOR
        # String: '[OCR] 图片不存在: '
        # String: '[OCR] 无法读取图片: '
        # String: '[OCR] 识别区域: ('
        # [Logic reconstructed from API references]
        pass

    def image_find_and_move(self, image_name, confidence, offset_x, offset_y, max_wait, move_duration):
        """图像识别并移动鼠标（不点击）"""
        # References: time, is_running, jump_to_group, find_image, log, mouse_move, sleep
        # String: '图片识别成功，移动鼠标到: ('
        # String: ', '
        # String: '图片识别超时: '
        # [Logic reconstructed from API references]
        pass

    def keyboard_hold(self, key, duration):
        """按住键:"""
        # References: time, perf_counter, pyautogui, keyDown, precise_sleep, keyUp, log, Exception
        # String: '按住键: '
        # String: ' (指定'
        # String: '秒-实际'
        # [Logic reconstructed from API references]
        pass

    def keyboard_hotkey(self, hold_time, keys):
        """组合键:"""
        # References: time, perf_counter, pyautogui, keyDown, precise_sleep, reversed, keyUp, log, join, hotkey
        # String: '组合键: '
        # String: ' (指定'
        # String: '秒-实际'
        # [Logic reconstructed from API references]
        pass

    def keyboard_press(self, key, hold_time):
        """按下单个键"""
        # References: time, perf_counter, pyautogui, keyDown, precise_sleep, keyUp, log, press, Exception
        # String: '按键: '
        # String: ' (指定'
        # String: '秒-实际'
        # [Logic reconstructed from API references]
        pass

    def keyboard_type(self, text, interval):
        """键盘输入文本 - 使用剪贴板粘贴方式"""
        # References: pyperclip, paste, copy, time, sleep, keyboard, press, release, len, log
        # String: 'ctrl'
        # String: '...'
        # String: '粘贴文本: '
        # [Logic reconstructed from API references]
        pass

    def load_image_cv2(self, image_path, flags):
        """加载图片（支持中文路径）"""
        # References: np, fromfile, uint8, cv2, imdecode, Exception, log
        # String: '加载图片失败: '
        # String: ', 错误: '
        # [Logic reconstructed from API references]
        pass

    def load_workflow(self, filepath):
        """加载工作流配置"""
        # References: open, json, load, Exception, log
        # String: 'utf-8'
        # String: '加载工作流失败: '
        # [Logic reconstructed from API references]
        pass

    def log(self, message):
        """记录日志"""
        # References: datetime, now, strftime, print, log_callback
        # String: '%H:%M:%S'
        # String: '] '
        # [Logic reconstructed from API references]
        pass

    def mouse_click(self, x, y, button, clicks):
        """鼠标点击（先丝滑移动再点击）"""
        # References: pyautogui, click, log, Exception
        # String: '鼠标点击: ('
        # String: ', '
        # String: ') '
        # [Logic reconstructed from API references]
        pass

    def mouse_click_current(self, button, clicks, hold_time):
        """在当前鼠标位置点击"""
        # References: time, perf_counter, pyautogui, mouseDown, precise_sleep, mouseUp, log, click, Exception
        # String: '鼠标按住: 当前位置 '
        # String: '键 (指定'
        # String: '秒-实际'
        # [Logic reconstructed from API references]
        pass

    def mouse_double_click(self, x, y):
        """鼠标双击"""
        # References: mouse_click
        # [Logic reconstructed from API references]
        pass

    def mouse_double_click_current(self):
        """在当前鼠标位置双击"""
        # References: mouse_click_current
        # [Logic reconstructed from API references]
        pass

    def mouse_drag(self, start_x, start_y, end_x, end_y, duration):
        """鼠标拖拽"""
        # References: pyautogui, moveTo, time, sleep, drag, log, Exception
        # String: '鼠标拖拽: ('
        # String: ', '
        # String: ') -> ('
        # [Logic reconstructed from API references]
        pass

    def mouse_move(self, x, y, duration):
        """移动鼠标（丝滑贝塞尔曲线移动）"""
        # References: humanize_enabled, random, uniform, log, Exception
        # String: '鼠标移动到: ('
        # String: ', '
        # String: '鼠标移动失败: '
        # [Logic reconstructed from API references]
        pass

    def mouse_right_click(self, x, y):
        """鼠标右键点击"""
        # References: mouse_click
        # String: 'right'
        # [Logic reconstructed from API references]
        pass

    def mouse_right_click_current(self):
        """在当前鼠标位置右键点击"""
        # References: mouse_click_current
        # String: 'right'
        # [Logic reconstructed from API references]
        pass

    def mouse_scroll(self, clicks, x, y):
        """鼠标滚轮"""
        # References: pyautogui, scroll, log, abs, Exception
        # String: '鼠标滚轮: 向'
        # String: '滚动 '
        # String: ' 格'
        # [Logic reconstructed from API references]
        pass

    def move_window(self, process_name, x, y, preset_pos):
        """移动窗口位置"""
        # References: win32gui, win32api, win32con, get_window_by_process, log, GetWindowRect, GetSystemMetrics, SM_CXSCREEN, SM_CYSCREEN, MoveWindow
        # String: '未找到程序窗口: '
        # String: '自定义'
        # String: '移动窗口: '
        # [Logic reconstructed from API references]
        pass

    def move_window_v2(self, find_by, target, x, y, preset_pos):
        """移动窗口位置（支持多种查找方式）"""
        # References: win32gui, win32con, win32api, find_window, log, get, GetWindowRect, GetSystemMetrics, SM_CXSCREEN, SM_CYSCREEN
        # String: '进程名'
        # String: '窗口标题'
        # String: 'PID'
        # [Logic reconstructed from API references]
        pass

    def multi_hold(self, keys):
        """同时按住多个按键（键盘或鼠标）"""
        # References: len, log, get, max, pyautogui, keyDown, append, mouseDown, time, perf_counter
        # String: '没有配置按键'
        # String: 'type'
        # String: 'keyboard'
        # [Logic reconstructed from API references]
        pass

    def ocr_read_region(self, x, y, width, height):
        """OCR 识别指定区域的文字"""
        # References: get_ocr_reader, log, pyautogui, screenshot, np, array, readtext, join, Exception
        # String: '[OCR] OCR 未初始化'
        # String: '[OCR] 识别结果: '
        # String: '[OCR] 识别失败: '
        # [Logic reconstructed from API references]
        pass

    def pause(self):
        """暂停执行"""
        # References: is_paused, log
        # String: '执行已暂停'
        # [Logic reconstructed from API references]
        pass

    def push_message(self, content, title):
        """推送消息到微信
    
    Args:
        content: 消息内容（物料名称，支持多个用顿号分隔）
        title: 消息标题（可选）
        
    Returns:
        bool: 是否推送成功"""
        # References: requests, os, path, join, get_app_path, exists, log, open, json, load
        # String: 'http://6hzs.nzwl.top'
        # String: 'screenshot_settings.json'
        # String: '❌ 未配置API密钥'
        # [Logic reconstructed from API references]
        pass

    def resize_window(self, process_name, width, height, preset_size):
        """调整窗口大小（客户区域大小）"""
        # References: win32gui, win32con, ctypes, get_window_by_process, log, GetWindowRect, GetWindowLong, GWL_STYLE, GWL_EXSTYLE, Structure
        # String: '自定义'
        # String: '未找到程序窗口: '
        # String: 'RECT'
        # [Logic reconstructed from API references]
        pass

    def resize_window_v2(self, find_by, target, width, height, preset_size):
        """调整窗口大小（支持多种查找方式）"""
        # References: win32gui, win32con, ctypes, find_window, log, get, GetWindowRect, GetWindowLong, GWL_STYLE, GWL_EXSTYLE
        # String: '进程名'
        # String: '窗口标题'
        # String: 'PID'
        # [Logic reconstructed from API references]
        pass

    def resume(self):
        """继续执行"""
        # References: is_paused, log
        # String: '执行继续'
        # [Logic reconstructed from API references]
        pass

    def save_fps_dpi_config(self, user_dpi):
        """保存FPS DPI配置"""
        # References: open, fps_config_file, json, dump, fps_standard_dpi, fps_user_dpi, log, Exception
        # String: 'utf-8'
        # String: 'FPS DPI已保存: '
        # String: '保存FPS DPI失败: '
        # [Logic reconstructed from API references]
        pass

    def save_workflow(self, workflow, filepath):
        """保存工作流配置"""
        # References: open, json, dump, log, Exception
        # String: 'utf-8'
        # String: '工作流已保存: '
        # String: '保存工作流失败: '
        # [Logic reconstructed from API references]
        pass

    def set_log_callback(self, callback):
        """设置日志回调函数"""
        # References: log_callback
        # [Logic reconstructed from API references]
        pass

    def set_status_callback(self, callback):
        """设置状态回调函数"""
        # References: status_callback
        # [Logic reconstructed from API references]
        pass

    def set_windowed_mode(self, process_name, width, height, preset_size):
        """将全屏/全屏窗口调整为窗口模式"""
        # References: win32gui, win32con, win32api, ctypes, get_window_by_process, log, GetSystemMetrics, SM_CXSCREEN, SM_CYSCREEN, GetWindowLong
        # String: '自定义'
        # String: '未找到程序窗口: '
        # String: 'RECT'
        # [Logic reconstructed from API references]
        pass

    def set_windowed_mode_v2(self, find_by, target, width, height, preset_size):
        """调整为窗口模式（支持多种查找方式）"""
        # References: win32gui, win32con, win32api, ctypes, find_window, log, get, GetWindowLong, GWL_STYLE, WS_OVERLAPPEDWINDOW
        # String: '进程名'
        # String: '窗口标题'
        # String: 'PID'
        # [Logic reconstructed from API references]
        pass

    def start_continuous_task(self, step, group_id):
        """启动常驻点击/按键任务（仅在当前组合执行时运行）"""
        # References: get, max, continuous_lock, continuous_tasks, append, threading, Thread, start, log
        # String: 'image'
        # String: 'confidence'
        # String: 'offset_x'
        # [Logic reconstructed from API references]
        pass

    def stop(self):
        """停止执行"""
        # References: is_running, is_paused, stop_continuous_tasks, log
        # String: '执行已停止'
        # [Logic reconstructed from API references]
        pass

    def stop_continuous_tasks(self):
        """停止所有常驻任务"""
        # References: continuous_lock, continuous_tasks, clear
        # String: 'should_stop'
        # [Logic reconstructed from API references]
        pass

    def stop_group_continuous_tasks(self, group_id):
        """停止指定组合的常驻任务"""
        # References: continuous_lock, continuous_tasks, get
        # String: 'group_id'
        # String: 'should_stop'
        # [Logic reconstructed from API references]
        pass

    def take_screenshot(self):
        """截图保存功能 - 从全局设置文件读取配置
        
    Returns:
        bool: 是否成功"""
        # References: os, path, join, get_app_path, exists, open, json, load, get, rstrip
        # String: 'screenshot_settings.json'
        # String: 'center'
        # String: '1080p'
        # [Logic reconstructed from API references]
        pass

    def toggle_pause(self):
        """切换暂停状态"""
        # References: is_paused, resume, pause
        # [Logic reconstructed from API references]
        pass

    def update_status(self, group_index, step_index, message):
        """更新执行状态"""
        # References: status_callback
        # [Logic reconstructed from API references]
        pass

    def wait_for_image(self, image_name, confidence, timeout):
        """等待图片出现"""
        # References: time, is_running, jump_to_group, find_image, sleep, log
        # String: '等待图片超时: '
        # [Logic reconstructed from API references]
        pass

    def wait_for_image_disappear(self, image_name, confidence, timeout):
        """等待图片消失"""
        # References: time, is_running, jump_to_group, find_image, log, sleep
        # String: '图片已消失: '
        # String: '等待图片消失超时: '
        # [Logic reconstructed from API references]
        pass

    def wait_if_paused(self):
        """如果暂停则等待，返回False表示已停止"""
        # References: is_paused, is_running, time, sleep
        # [Logic reconstructed from API references]
        pass

    def window_exists(self, window_title):
        """检测窗口是否存在（通过标题或进程名匹配）"""
        # References: win32gui, win32process, psutil, lower, endswith, EnumWindows, log, len, join, Exception
        # String: '.exe'
        # String: '✓ 检测到窗口: '
        # String: '✗ 未检测到窗口: '
        # [Logic reconstructed from API references]
        pass

    def window_exists_v2(self, find_by, target):
        """检测窗口是否存在（支持多种查找方式）"""
        # References: find_window, win32gui, GetWindowText, log, get, Exception
        # String: '进程名'
        # String: '窗口标题'
        # String: 'PID'
        # [Logic reconstructed from API references]
        pass

def get_app_path():
    """获取应用程序所在目录（兼容exe打包）"""
    # References: getattr, sys, os, path, dirname, executable, abspath
    pass

def precise_sleep(duration):
    """精确延时函数 - 使用忙等待实现高精度计时
    
    
    
    Windows 的 time.sleep() 精度通常只有 10-15ms，
    
    此函数通过忙等待实现更高精度的延时。
    
    
    
    Args:
    
        duration: 延时时间（秒）"""
    # References: time, perf_counter, sleep
    pass
