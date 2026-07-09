"""屏幕截图 + 图像识别定位（NumPy + Pillow）。

核心是一个纯 NumPy 实现的归一化互相关（NCC）模板匹配，配合 Pillow 抓屏，
无需 OpenCV 即可在屏幕上定位模板图片。如果安装了 OpenCV，会自动使用它加速。
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional, Tuple

import numpy as np

try:  # Pillow 抓屏
    from PIL import Image, ImageGrab
except Exception:  # pragma: no cover - Pillow 一定会装，这里只是兜底
    Image = None
    ImageGrab = None

try:  # 可选加速
    import cv2  # type: ignore
    _HAS_CV2 = True
except Exception:
    cv2 = None
    _HAS_CV2 = False


Region = Tuple[int, int, int, int]  # (left, top, width, height)


@dataclass
class MatchResult:
    """一次匹配结果。"""
    found: bool
    confidence: float
    left: int = 0
    top: int = 0
    width: int = 0
    height: int = 0

    @property
    def center(self) -> Tuple[int, int]:
        return (self.left + self.width // 2, self.top + self.height // 2)


# --------------------------------------------------------------------------- #
# 抓屏
# --------------------------------------------------------------------------- #
def grab_screen(region: Optional[Region] = None) -> "Image.Image":
    """用 Pillow 抓取屏幕（或指定区域），返回 RGB PIL.Image。

    region 为 (left, top, width, height)；None 表示全屏。
    """
    if ImageGrab is None:
        raise RuntimeError("Pillow 未安装，无法抓屏")
    if region is not None:
        left, top, w, h = region
        bbox = (left, top, left + w, top + h)
        img = ImageGrab.grab(bbox=bbox)
    else:
        img = ImageGrab.grab()
    return img.convert("RGB")


def to_gray_array(img: "Image.Image") -> np.ndarray:
    """PIL 图像 -> 灰度 float32 NumPy 数组。"""
    return np.asarray(img.convert("L"), dtype=np.float32)


# --------------------------------------------------------------------------- #
# NumPy 归一化互相关模板匹配
# --------------------------------------------------------------------------- #
def _window_sums(a: np.ndarray, h: int, w: int) -> np.ndarray:
    """滑动窗口求和：返回每个 (h, w) 窗口内元素之和的数组。"""
    s = np.cumsum(np.cumsum(a, axis=0), axis=1)
    s = np.pad(s, ((1, 0), (1, 0)), mode="constant")
    return s[h:, w:] - s[:-h, w:] - s[h:, :-w] + s[:-h, :-w]


def _fft_correlate_valid(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """image 与 kernel 的互相关，只保留完全重叠（valid）区域。"""
    ih, iw = image.shape
    kh, kw = kernel.shape
    fh, fw = ih + kh - 1, iw + kw - 1
    fi = np.fft.rfft2(image, (fh, fw))
    # 互相关 = 与翻转核的卷积
    fk = np.fft.rfft2(kernel[::-1, ::-1], (fh, fw))
    full = np.fft.irfft2(fi * fk, (fh, fw))
    return full[kh - 1:kh - 1 + (ih - kh + 1), kw - 1:kw - 1 + (iw - kw + 1)]


def match_template_ncc(scene_gray: np.ndarray, template_gray: np.ndarray) -> Tuple[float, Tuple[int, int]]:
    """纯 NumPy 归一化互相关。

    返回 (最高相似度[-1,1], (最佳位置左上角 x, y))。
    """
    ih, iw = scene_gray.shape
    th, tw = template_gray.shape
    if th > ih or tw > iw:
        return -1.0, (0, 0)

    t0 = template_gray - template_gray.mean()
    t_energy = float((t0 * t0).sum())
    if t_energy <= 1e-9:  # 模板是纯色，无法匹配
        return -1.0, (0, 0)

    numerator = _fft_correlate_valid(scene_gray, t0)

    n = th * tw
    win_sum = _window_sums(scene_gray, th, tw)
    win_sqsum = _window_sums(scene_gray * scene_gray, th, tw)
    win_var = win_sqsum - (win_sum * win_sum) / n  # 窗口内平方偏差之和

    denom = np.sqrt(np.maximum(win_var, 0.0) * t_energy)
    with np.errstate(divide="ignore", invalid="ignore"):
        ncc = np.where(denom > 1e-9, numerator / denom, 0.0)

    idx = int(np.argmax(ncc))
    y, x = np.unravel_index(idx, ncc.shape)
    return float(ncc[y, x]), (int(x), int(y))


def _match_cv2(scene_gray: np.ndarray, template_gray: np.ndarray) -> Tuple[float, Tuple[int, int]]:
    res = cv2.matchTemplate(scene_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    _min_v, max_v, _min_l, max_l = cv2.minMaxLoc(res)
    return float(max_v), (int(max_l[0]), int(max_l[1]))


# --------------------------------------------------------------------------- #
# 对外接口：在屏幕上找模板
# --------------------------------------------------------------------------- #
def locate_on_screen(
    template_path: str,
    region: Optional[Region] = None,
    confidence: float = 0.8,
    grayscale: bool = True,
    scene_image: "Optional[Image.Image]" = None,
) -> MatchResult:
    """在屏幕（或 region）上定位模板图片。

    template_path : 模板 PNG/JPG 路径
    region        : (left, top, width, height)，None 为全屏
    confidence    : 相似度阈值 [0,1]
    scene_image   : 可传入已抓好的场景图（复用截图，避免重复抓屏）
    """
    if Image is None:
        raise RuntimeError("Pillow 未安装")
    if not os.path.isfile(template_path):
        raise FileNotFoundError(template_path)

    if scene_image is None:
        scene_image = grab_screen(region)
    scene = to_gray_array(scene_image)
    tmpl = to_gray_array(Image.open(template_path))

    if _HAS_CV2:
        score, (x, y) = _match_cv2(scene, tmpl)
    else:
        score, (x, y) = match_template_ncc(scene, tmpl)

    th, tw = tmpl.shape
    off_x = region[0] if region else 0
    off_y = region[1] if region else 0

    if score >= confidence:
        return MatchResult(True, score, off_x + x, off_y + y, tw, th)
    return MatchResult(False, score, off_x + x, off_y + y, tw, th)


def save_region_screenshot(path: str, region: Optional[Region] = None) -> str:
    """抓取区域并保存为 PNG，返回保存路径。"""
    img = grab_screen(region)
    img.save(path)
    return path
