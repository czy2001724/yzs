"""全局键盘 / 鼠标 Hook。

包含两部分：
1. HotkeyManager —— 基于 keyboard 库注册全局热键（启动/停止/暂停）。
2. GlobalInputRecorder —— 基于 Windows 底层钩子（WH_MOUSE_LL / WH_KEYBOARD_LL，
   通过 pywin32 提供的常量 + ctypes 回调实现）录制全局鼠标点击和按键，
   用来把手动操作转成自动化步骤。

在非 Windows 平台上，录制器会优雅降级为不可用状态，热键仍可通过 keyboard 库工作。
"""
from __future__ import annotations

import platform
import threading
from typing import Callable, Dict, List, Optional

IS_WINDOWS = platform.system() == "Windows"

try:
    import keyboard as _keyboard  # 跨平台全局热键
except Exception:  # pragma: no cover
    _keyboard = None


# --------------------------------------------------------------------------- #
# 全局热键
# --------------------------------------------------------------------------- #
class HotkeyManager:
    """注册/注销全局热键。回调在 keyboard 库的后台线程里触发。"""

    def __init__(self) -> None:
        self._handles: Dict[str, object] = {}

    @property
    def available(self) -> bool:
        return _keyboard is not None

    def register(self, hotkey: str, callback: Callable[[], None]) -> bool:
        """注册一个热键，例如 'f9'、'ctrl+shift+s'。重复注册会先注销旧的。"""
        if _keyboard is None:
            return False
        self.unregister(hotkey)
        try:
            handle = _keyboard.add_hotkey(hotkey, callback, suppress=False)
            self._handles[hotkey] = handle
            return True
        except Exception:
            return False

    def unregister(self, hotkey: str) -> None:
        if _keyboard is None:
            return
        handle = self._handles.pop(hotkey, None)
        if handle is not None:
            try:
                _keyboard.remove_hotkey(handle)
            except Exception:
                pass

    def clear(self) -> None:
        for hk in list(self._handles):
            self.unregister(hk)


# --------------------------------------------------------------------------- #
# 全局输入录制（Windows 底层钩子）
# --------------------------------------------------------------------------- #
class GlobalInputRecorder:
    """录制全局鼠标点击 / 按键，产出可回放的步骤列表。

    每条记录形如：
        {"type": "click", "x": 100, "y": 200, "button": "left"}
        {"type": "key",   "key": "enter"}

    通过 SetWindowsHookEx 安装 WH_MOUSE_LL / WH_KEYBOARD_LL 低级钩子，
    在独立线程里跑消息循环。停止时卸载钩子。
    """

    def __init__(self, on_event: Optional[Callable[[dict], None]] = None) -> None:
        self.on_event = on_event
        self.events: List[dict] = []
        self._thread: Optional[threading.Thread] = None
        self._running = False
        self._mouse_hook = None
        self._kbd_hook = None
        self._user32 = None
        self._kernel32 = None
        # 防止回调对象被 GC 回收
        self._mouse_proc = None
        self._kbd_proc = None

    @property
    def available(self) -> bool:
        return IS_WINDOWS

    def start(self) -> bool:
        if not IS_WINDOWS:
            return False
        if self._running:
            return True
        self.events = []
        self._running = True
        self._thread = threading.Thread(target=self._run, name="input-hook", daemon=True)
        self._thread.start()
        return True

    def stop(self) -> List[dict]:
        self._running = False
        if IS_WINDOWS and self._user32 is not None:
            # 往钩子线程发退出消息，唤醒 GetMessage
            try:
                import ctypes
                if self._thread is not None:
                    tid = getattr(self._thread, "ident", None)
                    if tid:
                        WM_QUIT = 0x0012
                        self._user32.PostThreadMessageW(tid, WM_QUIT, 0, 0)
            except Exception:
                pass
        if self._thread is not None:
            self._thread.join(timeout=1.0)
            self._thread = None
        return list(self.events)

    def _emit(self, ev: dict) -> None:
        self.events.append(ev)
        if self.on_event:
            try:
                self.on_event(ev)
            except Exception:
                pass

    def _run(self) -> None:  # pragma: no cover - 需要 Windows GUI 环境
        import ctypes
        from ctypes import wintypes

        self._user32 = ctypes.windll.user32
        self._kernel32 = ctypes.windll.kernel32
        user32 = self._user32

        WH_KEYBOARD_LL = 13
        WH_MOUSE_LL = 14
        WM_KEYDOWN = 0x0100
        WM_SYSKEYDOWN = 0x0104
        WM_LBUTTONDOWN = 0x0201
        WM_RBUTTONDOWN = 0x0204
        WM_MBUTTONDOWN = 0x0207

        LRESULT = ctypes.c_ssize_t
        ULONG_PTR = ctypes.c_ulonglong if ctypes.sizeof(ctypes.c_void_p) == 8 else ctypes.c_ulong

        class POINT(ctypes.Structure):
            _fields_ = [("x", wintypes.LONG), ("y", wintypes.LONG)]

        class MSLLHOOKSTRUCT(ctypes.Structure):
            _fields_ = [
                ("pt", POINT),
                ("mouseData", wintypes.DWORD),
                ("flags", wintypes.DWORD),
                ("time", wintypes.DWORD),
                ("dwExtraInfo", ULONG_PTR),
            ]

        class KBDLLHOOKSTRUCT(ctypes.Structure):
            _fields_ = [
                ("vkCode", wintypes.DWORD),
                ("scanCode", wintypes.DWORD),
                ("flags", wintypes.DWORD),
                ("time", wintypes.DWORD),
                ("dwExtraInfo", ULONG_PTR),
            ]

        HOOKPROC = ctypes.CFUNCTYPE(LRESULT, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM)

        def low_level_mouse(nCode, wParam, lParam):
            if nCode == 0 and self._running:
                info = ctypes.cast(lParam, ctypes.POINTER(MSLLHOOKSTRUCT)).contents
                btn = None
                if wParam == WM_LBUTTONDOWN:
                    btn = "left"
                elif wParam == WM_RBUTTONDOWN:
                    btn = "right"
                elif wParam == WM_MBUTTONDOWN:
                    btn = "middle"
                if btn:
                    self._emit({"type": "click", "x": int(info.pt.x),
                                "y": int(info.pt.y), "button": btn})
            return user32.CallNextHookEx(None, nCode, wParam, lParam)

        def low_level_kbd(nCode, wParam, lParam):
            if nCode == 0 and self._running and wParam in (WM_KEYDOWN, WM_SYSKEYDOWN):
                info = ctypes.cast(lParam, ctypes.POINTER(KBDLLHOOKSTRUCT)).contents
                name = _vk_to_name(info.vkCode)
                if name:
                    self._emit({"type": "key", "key": name})
            return user32.CallNextHookEx(None, nCode, wParam, lParam)

        self._mouse_proc = HOOKPROC(low_level_mouse)
        self._kbd_proc = HOOKPROC(low_level_kbd)

        # 安装两个全局低级钩子；hmod 传本模块句柄，最后一个 0 表示挂到所有线程
        hmod = self._kernel32.GetModuleHandleW(None)
        self._mouse_hook = user32.SetWindowsHookExW(WH_MOUSE_LL, self._mouse_proc, hmod, 0)
        self._kbd_hook = user32.SetWindowsHookExW(WH_KEYBOARD_LL, self._kbd_proc, hmod, 0)

        # 低级钩子必须有消息循环才会回调，所以本线程要一直泵消息；
        # stop() 时通过 PostThreadMessage(WM_QUIT) 让 GetMessage 返回 0 从而退出。
        msg = wintypes.MSG()
        while self._running:
            r = user32.GetMessageW(ctypes.byref(msg), None, 0, 0)
            if r == 0 or r == -1:        # WM_QUIT 或出错
                break
            user32.TranslateMessage(ctypes.byref(msg))
            user32.DispatchMessageW(ctypes.byref(msg))

        if self._mouse_hook:
            user32.UnhookWindowsHookEx(self._mouse_hook)
        if self._kbd_hook:
            user32.UnhookWindowsHookEx(self._kbd_hook)
        self._mouse_hook = self._kbd_hook = None


# 常用虚拟键码 -> pyautogui 键名
_VK_NAMES = {
    0x08: "backspace", 0x09: "tab", 0x0D: "enter", 0x1B: "esc",
    0x20: "space", 0x25: "left", 0x26: "up", 0x27: "right", 0x28: "down",
    0x2E: "delete", 0x2D: "insert", 0x24: "home", 0x23: "end",
    0x21: "pageup", 0x22: "pagedown",
    0x10: "shift", 0x11: "ctrl", 0x12: "alt",
    0x70: "f1", 0x71: "f2", 0x72: "f3", 0x73: "f4", 0x74: "f5", 0x75: "f6",
    0x76: "f7", 0x77: "f8", 0x78: "f9", 0x79: "f10", 0x7A: "f11", 0x7B: "f12",
}


def _vk_to_name(vk: int) -> Optional[str]:
    if vk in _VK_NAMES:
        return _VK_NAMES[vk]
    if 0x30 <= vk <= 0x39:  # 0-9
        return chr(vk)
    if 0x41 <= vk <= 0x5A:  # A-Z
        return chr(vk).lower()
    return None
