"""全局热键管理：Windows 使用 RegisterHotKey API，非 Windows 回退 keyboard 库。

RegisterHotKey 是标准 Win32 API，不安装低级钩子（WH_KEYBOARD_LL），不会被反作弊系统检测。
"""
from __future__ import annotations

import ctypes
import platform
from ctypes import wintypes
from typing import Callable, Dict, Optional

from PyQt5.QtCore import QAbstractNativeEventFilter

IS_WINDOWS = platform.system() == "Windows"

# Modifier constants for RegisterHotKey
MOD_ALT = 0x0001
MOD_CONTROL = 0x0002
MOD_SHIFT = 0x0004
MOD_WIN = 0x0008
MOD_NOREPEAT = 0x4000

# Virtual-Key Codes for common keys used as hotkeys
_VK: Dict[str, int] = {
    "f1": 0x70, "f2": 0x71, "f3": 0x72, "f4": 0x73,
    "f5": 0x74, "f6": 0x75, "f7": 0x76, "f8": 0x77,
    "f9": 0x78, "f10": 0x79, "f11": 0x7A, "f12": 0x7B,
    "backspace": 0x08, "tab": 0x09, "enter": 0x0D, "esc": 0x1B,
    "space": 0x20, "pageup": 0x21, "pagedown": 0x22,
    "end": 0x23, "home": 0x24, "insert": 0x2D, "delete": 0x2E,
    "left": 0x25, "up": 0x26, "right": 0x27, "down": 0x28,
    "0": 0x30, "1": 0x31, "2": 0x32, "3": 0x33, "4": 0x34,
    "5": 0x35, "6": 0x36, "7": 0x37, "8": 0x38, "9": 0x39,
    "a": 0x41, "b": 0x42, "c": 0x43, "d": 0x44, "e": 0x45,
    "f": 0x46, "g": 0x47, "h": 0x48, "i": 0x49, "j": 0x4A,
    "k": 0x4B, "l": 0x4C, "m": 0x4D, "n": 0x4E, "o": 0x4F,
    "p": 0x50, "q": 0x51, "r": 0x52, "s": 0x53, "t": 0x54,
    "u": 0x55, "v": 0x56, "w": 0x57, "x": 0x58, "y": 0x59, "z": 0x5A,
}


def _parse_hotkey(s: str) -> tuple:
    """解析 'f9' / 'ctrl+shift+s' -> (modifiers, vk_code). 失败返回 (0, 0)."""
    parts = [p.strip().lower() for p in s.split("+")]
    vk_part = parts[-1]
    vk = _VK.get(vk_part)
    if vk is None and len(vk_part) == 1 and vk_part.isascii():
        vk = ord(vk_part.upper())
    if vk is None:
        return 0, 0
    mod = MOD_NOREPEAT
    for m in parts[:-1]:
        if m in ("ctrl", "control"):
            mod |= MOD_CONTROL
        elif m == "alt":
            mod |= MOD_ALT
        elif m == "shift":
            mod |= MOD_SHIFT
        elif m in ("win", "windows"):
            mod |= MOD_WIN
    return mod, vk


class NativeHotkeyManager(QAbstractNativeEventFilter):
    """热键管理器。

    - Windows: RegisterHotKey API（标准 Win32，不触发反作弊）
    - 其他平台: keyboard 库回退

    使用方式:
        mgr = NativeHotkeyManager()
        app.installNativeEventFilter(mgr)
        mgr.register("f9", lambda: print("F9 pressed"))
    """

    def __init__(self) -> None:
        super().__init__()
        self._id_cb: Dict[int, Callable[[], None]] = {}
        self._hk_id: Dict[str, int] = {}
        self._next_id = 1
        self._kb_handles: Dict[str, object] = {}

    @property
    def available(self) -> bool:
        return IS_WINDOWS or _keyboard_available()

    def register(self, hotkey: str, callback: Callable[[], None]) -> bool:
        self.unregister(hotkey)
        if IS_WINDOWS:
            mod, vk = _parse_hotkey(hotkey)
            if vk == 0:
                return False
            id_ = self._next_id
            self._next_id += 1
            user32 = ctypes.windll.user32
            if user32.RegisterHotKey(None, id_, mod, vk):
                self._id_cb[id_] = callback
                self._hk_id[hotkey] = id_
                return True
            return False
        else:
            if not _keyboard_available():
                return False
            import keyboard as _kb
            try:
                handle = _kb.add_hotkey(hotkey, callback, suppress=False)
                self._kb_handles[hotkey] = handle
                return True
            except Exception:
                return False

    def unregister(self, hotkey: str) -> None:
        if IS_WINDOWS:
            id_ = self._hk_id.pop(hotkey, None)
            if id_ is not None:
                self._id_cb.pop(id_, None)
                ctypes.windll.user32.UnregisterHotKey(None, id_)
        else:
            handle = self._kb_handles.pop(hotkey, None)
            if handle is not None and _keyboard_available():
                import keyboard as _kb
                try:
                    _kb.remove_hotkey(handle)
                except Exception:
                    pass

    def clear(self) -> None:
        if IS_WINDOWS:
            user32 = ctypes.windll.user32
            for id_ in list(self._id_cb):
                user32.UnregisterHotKey(None, id_)
            self._id_cb.clear()
            self._hk_id.clear()
        else:
            for hk in list(self._kb_handles):
                self.unregister(hk)

    def nativeEventFilter(self, event_type: bytes, message: int) -> tuple:
        if IS_WINDOWS:
            msg = wintypes.MSG.from_address(int(message))
            if msg.message == 0x0312:  # WM_HOTKEY
                cb = self._id_cb.get(msg.wParam)
                if cb:
                    try:
                        cb()
                    except Exception:
                        pass
        return False, 0


def _keyboard_available() -> bool:
    try:
        import keyboard  # noqa: F401
        return True
    except Exception:
        return False
