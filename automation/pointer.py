"""实时鼠标坐标 + 像素取色（低延迟）。

关键点：`pyautogui.pixel()` 每次调用都会**截屏**，实时轮询时会明显卡顿。
这里在 Windows 上直接用 Win32 `GetCursorPos` / `GetPixel`（GDI 直接读一个像素），
是即时的、几乎零开销；非 Windows 回退到 pyautogui。

⚠️  反作弊警告：GDI GetPixel 读屏是外挂常见特征，部分反作弊会检测。
通过 `set_pixel_reading(False)` 可关闭取色，只保留坐标读取（GetCursorPos 安全）。
"""
from __future__ import annotations

import platform
from typing import Optional, Tuple

IS_WINDOWS = platform.system() == "Windows"

# 模块级开关：是否启用像素取色（关闭后在反作弊环境下更安全）
_pixel_reading_enabled = True


def set_pixel_reading(enabled: bool) -> None:
    """全局开关：是否启用实时像素取色。关闭后 get_pixel_color 始终返回 None。"""
    global _pixel_reading_enabled
    _pixel_reading_enabled = enabled

if IS_WINDOWS:
    import ctypes
    from ctypes import wintypes

    _user32 = ctypes.windll.user32
    _gdi32 = ctypes.windll.gdi32

    _user32.GetDC.restype = wintypes.HDC
    _user32.GetDC.argtypes = [wintypes.HWND]
    _user32.ReleaseDC.argtypes = [wintypes.HWND, wintypes.HDC]
    _gdi32.GetPixel.restype = wintypes.COLORREF
    _gdi32.GetPixel.argtypes = [wintypes.HDC, ctypes.c_int, ctypes.c_int]

    _CLR_INVALID = 0xFFFFFFFF

    def get_cursor_pos() -> Tuple[int, int]:
        pt = wintypes.POINT()
        _user32.GetCursorPos(ctypes.byref(pt))
        return int(pt.x), int(pt.y)

    def get_pixel_color(x: int, y: int) -> Optional[Tuple[int, int, int]]:
        if not _pixel_reading_enabled:
            return None
        hdc = _user32.GetDC(0)
        try:
            c = _gdi32.GetPixel(hdc, int(x), int(y))
        finally:
            _user32.ReleaseDC(0, hdc)
        if c == _CLR_INVALID:
            return None
        return (c & 0xFF, (c >> 8) & 0xFF, (c >> 16) & 0xFF)  # COLORREF = 0x00BBGGRR

else:  # 非 Windows 回退
    def get_cursor_pos() -> Tuple[int, int]:
        try:
            import pyautogui
            x, y = pyautogui.position()
            return int(x), int(y)
        except Exception:
            return (0, 0)

    def get_pixel_color(x: int, y: int) -> Optional[Tuple[int, int, int]]:
        return None
