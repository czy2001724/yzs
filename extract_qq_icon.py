"""从 exe 中提取大图标，保存为标准 .ico 格式。"""
import ctypes
import struct
import sys
import os
from ctypes import wintypes

user32 = ctypes.windll.user32
shell32 = ctypes.windll.shell32
kernel32 = ctypes.windll.kernel32
gdi32 = ctypes.windll.gdi32


def extract_ico(exe_path: str, output_path: str) -> bool:
    if not os.path.isfile(exe_path):
        print(f"[!] 文件不存在: {exe_path}")
        return False

    large = wintypes.HICON()
    small = wintypes.HICON()
    count = shell32.ExtractIconExW(exe_path, 0,
                                   ctypes.byref(large),
                                   ctypes.byref(small), 1)
    if count == 0 or not large:
        print("[!] 未能提取图标")
        return False

    class ICONINFO(ctypes.Structure):
        _fields_ = [
            ("fIcon", wintypes.BOOL),
            ("xHotspot", wintypes.DWORD),
            ("yHotspot", wintypes.DWORD),
            ("hbmMask", wintypes.HBITMAP),
            ("hbmColor", wintypes.HBITMAP),
        ]

    info = ICONINFO()
    if not user32.GetIconInfo(large, ctypes.byref(info)):
        print("[!] GetIconInfo 失败")
        return False

    class BITMAP(ctypes.Structure):
        _fields_ = [
            ("bmType", wintypes.LONG),
            ("bmWidth", wintypes.LONG),
            ("bmHeight", wintypes.LONG),
            ("bmWidthBytes", wintypes.LONG),
            ("bmPlanes", wintypes.WORD),
            ("bmBitsPixel", wintypes.WORD),
            ("bmBits", wintypes.LPVOID),
        ]

    bm = BITMAP()
    gdi32.GetObjectW(info.hbmColor, ctypes.sizeof(bm), ctypes.byref(bm))
    w, h_raw = bm.bmWidth, bm.bmHeight
    h = h_raw // 2  # 图标位图高度 = 2x 实际（含 mask）
    bpp = bm.bmBitsPixel

    if w <= 0 or h <= 0 or w > 256 or h > 256:
        print(f"[!] 图标尺寸异常: {w}x{h}")
        return False

    print(f"[*] 图标尺寸: {w}x{h}, {bpp} bpp")

    hdc = user32.GetDC(0)
    hdc_mem = gdi32.CreateCompatibleDC(hdc)
    hbmp = gdi32.CreateCompatibleBitmap(hdc, w, h)
    old_bmp = gdi32.SelectObject(hdc_mem, hbmp)

    # 绘制图标到 DC
    DI_NORMAL = 3
    user32.DrawIconEx(hdc_mem, 0, 0, large, w, h, 0, None, DI_NORMAL)

    # BITMAPINFOHEADER + 像素数据 = DIB
    class BITMAPINFOHEADER(ctypes.Structure):
        _fields_ = [
            ("biSize", wintypes.DWORD),
            ("biWidth", wintypes.LONG),
            ("biHeight", wintypes.LONG),  # 正值 = 底部在上
            ("biPlanes", wintypes.WORD),
            ("biBitCount", wintypes.WORD),
            ("biCompression", wintypes.DWORD),
            ("biSizeImage", wintypes.DWORD),
            ("biXPelsPerMeter", wintypes.LONG),
            ("biYPelsPerMeter", wintypes.LONG),
            ("biClrUsed", wintypes.DWORD),
            ("biClrImportant", wintypes.DWORD),
        ]

    bih = BITMAPINFOHEADER()
    bih.biSize = ctypes.sizeof(bih)
    bih.biWidth = w
    bih.biHeight = h * 2  # 双倍高度：上半颜色 + 下半 mask
    bih.biPlanes = 1
    bih.biBitCount = 32
    bih.biSizeImage = w * h * 2 * 4

    buf = (ctypes.c_byte * bih.biSizeImage)()
    if not gdi32.GetDIBits(hdc_mem, hbmp, 0, h * 2, buf, ctypes.byref(bih), 0):
        gdi32.SelectObject(hdc_mem, old_bmp)
        gdi32.DeleteObject(hbmp)
        gdi32.DeleteDC(hdc_mem)
        user32.ReleaseDC(0, hdc)
        print("[!] GetDIBits 失败")
        return False

    # 组装 .ico: 文件头 + 目录项 + DIB 数据
    # ICO 的 AND mask 是 1bpp 反转的，直接用 GetDIBits 输出的即可
    img_size = len(buf)
    offset = 22  # 6 (header) + 16 (one dir entry)

    header = struct.pack("<HHH", 0, 1, 1)  # reserved, type=icon, count=1
    # ICO 目录项: w, h, colors, reserved, planes, bpp, size, offset
    # 注意：256 像素的宽/高在 ICO 中写为 0
    dir_w = w if w < 256 else 0
    dir_h = h if h < 256 else 0
    direntry = struct.pack("<BBBBHHII", dir_w, dir_h, 0, 0, 1, 32, img_size, offset)

    raw_bih = (ctypes.c_byte * ctypes.sizeof(bih))()
    ctypes.memmove(raw_bih, ctypes.addressof(bih), ctypes.sizeof(bih))
    # 修正 biHeight 为实际值
    bih_bytes = bytearray(raw_bih)
    struct.pack_into("<I", bih_bytes, 8, h * 2)

    with open(output_path, "wb") as f:
        f.write(header)
        f.write(direntry)
        f.write(bytes(bih_bytes))
        f.write(bytes(buf))

    gdi32.SelectObject(hdc_mem, old_bmp)
    gdi32.DeleteObject(hbmp)
    gdi32.DeleteDC(hdc_mem)
    user32.ReleaseDC(0, hdc)
    user32.DestroyIcon(large)
    if small:
        user32.DestroyIcon(small)
    if info.hbmMask:
        gdi32.DeleteObject(info.hbmMask)
    if info.hbmColor:
        gdi32.DeleteObject(info.hbmColor)

    print(f"[+] 图标已保存: {os.path.abspath(output_path)}  "
          f"({os.path.getsize(output_path)} bytes)")
    return True


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="从 exe 提取图标为 .ico")
    ap.add_argument("exe", help="exe 文件路径")
    ap.add_argument("-o", "--output", default="qq_icon.ico", help="输出路径")
    args = ap.parse_args()
    ok = extract_ico(args.exe, args.output)
    sys.exit(0 if ok else 1)
