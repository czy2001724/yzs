"""自动化核心包：引擎、图像识别、全局 Hook。"""
from .engine import AutomationEngine, StopRequested
from .image_match import MatchResult, locate_on_screen, grab_screen, save_region_screenshot
from .hooks import HotkeyManager, GlobalInputRecorder

__all__ = [
    "AutomationEngine",
    "StopRequested",
    "MatchResult",
    "locate_on_screen",
    "grab_screen",
    "save_region_screenshot",
    "HotkeyManager",
    "GlobalInputRecorder",
]
