"""Windows 窗口操作（pywin32）。

支持的窗口操作：按标题查找、移动、调整大小、置顶。
仅在 Windows 上可用，非 Windows 优雅降级。
"""
from __future__ import annotations

import platform
from dataclasses import dataclass
from typing import Optional, Tuple

IS_WINDOWS = platform.system() == "Windows"

if IS_WINDOWS:
    import win32gui
    import win32con
else:
    win32gui = None  # type: ignore
    win32con = None  # type: ignore


@dataclass
class WindowInfo:
    """窗口信息。"""
    hwnd: int
    title: str
    x: int = 0
    y: int = 0
    width: int = 0
    height: int = 0


def find_window(title: str = "", class_name: str = "") -> Optional[WindowInfo]:
    """按标题（模糊匹配）或类名查找窗口，返回第一个匹配的。

    不要求窗口可见（全屏游戏的窗口可能 IsWindowVisible=False）。
    """
    if not IS_WINDOWS:
        return None

    result = []

    def _callback(hwnd, _):
        w_title = win32gui.GetWindowText(hwnd)
        w_class = win32gui.GetClassName(hwnd)
        if title and title.lower() in w_title.lower():
            rect = win32gui.GetWindowRect(hwnd)
            result.append(WindowInfo(
                hwnd=hwnd, title=w_title,
                x=rect[0], y=rect[1],
                width=rect[2] - rect[0], height=rect[3] - rect[1],
            ))
            return False
        if class_name and class_name.lower() in w_class.lower():
            rect = win32gui.GetWindowRect(hwnd)
            result.append(WindowInfo(
                hwnd=hwnd, title=w_title,
                x=rect[0], y=rect[1],
                width=rect[2] - rect[0], height=rect[3] - rect[1],
            ))
            return False
        return True

    win32gui.EnumWindows(_callback, None)
    return result[0] if result else None


def move_window(hwnd: int, x: int, y: int, width: int = 0, height: int = 0) -> bool:
    """移动窗口到 (x,y)，可选同时调整大小。"""
    if not IS_WINDOWS:
        return False
    flags = win32con.SWP_NOZORDER
    w = width if width > 0 else None
    h = height if height > 0 else None
    if w is None or h is None:
        rect = win32gui.GetWindowRect(hwnd)
        if w is None:
            w = rect[2] - rect[0]
        if h is None:
            h = rect[3] - rect[1]
    win32gui.SetWindowPos(hwnd, 0, x, y, w, h, flags)
    return True


def focus_window(hwnd: int) -> bool:
    """将窗口置顶并设为前台焦点。"""
    if not IS_WINDOWS:
        return False
    try:
        win32gui.SetForegroundWindow(hwnd)
        return True
    except Exception:
        return False


def get_foreground_window() -> Optional[int]:
    """获取当前前台窗口句柄。"""
    if not IS_WINDOWS:
        return None
    return win32gui.GetForegroundWindow()


def list_windows(keyword: str = "") -> list:
    """列出所有窗口标题（含全屏游戏），可选按关键字过滤。"""
    if not IS_WINDOWS:
        return []
    result = []

    def _callback(hwnd, _):
        w_title = win32gui.GetWindowText(hwnd)
        if w_title and (not keyword or keyword.lower() in w_title.lower()):
            result.append(w_title)
        return True

    win32gui.EnumWindows(_callback, None)
    return result
