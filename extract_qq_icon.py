"""从 QQ.exe 提取图标并保存为 .ico 文件。

用法：python extract_qq_icon.py
    如果 QQ 装在默认路径，自动找到并提取。
    否则可以 python extract_qq_icon.py "D:\QQ\Bin\QQ.exe"
"""
import ctypes
import sys
import os
from ctypes import wintypes

# QQ 常见安装路径
_DEFAULT_PATHS = [
    r"C:\Program Files (x86)\Tencent\QQ\Bin\QQ.exe",
    r"C:\Program Files\Tencent\QQ\Bin\QQ.exe",
    r"C:\Program Files (x86)\Tencent\QQNT\QQ.exe",
    r"C:\Program Files\Tencent\QQNT\QQ.exe",
]


def extract_icon(exe_path: str, output_path: str) -> bool:
    """用 Win32 ExtractIconExW 从 exe 提取图标，保存为 .ico 文件。"""
    if not os.path.isfile(exe_path):
        print(f"文件不存在: {exe_path}")
        return False

    user32 = ctypes.windll.user32
    shell32 = ctypes.windll.shell32

    # 获取大图标数量
    count = int(shell32.ExtractIconExW(exe_path, -1, None, None, 0))
    if count == 0:
        print(f"{exe_path} 中无图标")
        return False

    # 提取第一个大图标
    hicon = wintypes.HICON()
    shell32.ExtractIconExW(exe_path, 0, ctypes.byref(hicon), None, 1)
    if not hicon:
        print("提取图标句柄失败")
        return False

    # 保存为 .ico（用 shell32 写文件）
    # 简单方式：直接用 ctypes 写临时 bmp 然后转
    # 更可靠：利用 BCX 的 .ico 写，但这里走直接的文件格式
    #
    # 实际上最简单且跨 PyInstaller 兼容的方式：走 PIL
    
    try:
        from PIL import Image
        from PyQt5.QtGui import QPixmap
        from PyQt5.QtWidgets import QApplication
        
        _app = QApplication.instance()
        if _app is None:
            _app = QApplication(sys.argv)
        
        pixmap = QPixmap.fromWinHICON(int(hicon))
        if pixmap.isNull():
            print("QPixmap 转换失败")
            return False
        
        pixmap.save(output_path, "ICO")
        print(f"图标已保存: {os.path.abspath(output_path)}")
        return True
    except ImportError:
        pass

    # 回退：用 Win32 Save Icon
    return _save_icon_win32(hicon, output_path)


def _save_icon_win32(hicon, path: str) -> bool:
    """用 Win32 API 保存 HICON 到 .ico 文件。"""
    import struct
    
    user32 = ctypes.windll.user32
    gdi32 = ctypes.windll.gdi32
    kernel32 = ctypes.windll.kernel32

    # 获取图标信息
    class ICONINFO(ctypes.Structure):
        _fields_ = [
            ("fIcon", wintypes.BOOL),
            ("xHotspot", wintypes.DWORD),
            ("yHotspot", wintypes.DWORD),
            ("hbmMask", wintypes.HBITMAP),
            ("hbmColor", wintypes.HBITMAP),
        ]

    info = ICONINFO()
    if not user32.GetIconInfo(hicon, ctypes.byref(info)):
        print("GetIconInfo 失败")
        return False

    # 获取位图尺寸
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

    w = bm.bmWidth
    h = bm.bmHeight // 2  # 图标位图高度 = 2x 实际图标高度（含 mask）

    # 用 GDI+ 方式更简单：直接把 HICON 画到 Bitmap，再保存
    # 简化：走 DrawIconEx + GetDIBits
    
    hdc = user32.GetDC(0)
    hdc_mem = gdi32.CreateCompatibleDC(hdc)
    hbmp = gdi32.CreateCompatibleBitmap(hdc, w, h)
    old_bmp = gdi32.SelectObject(hdc_mem, hbmp)
    user32.DrawIconEx(hdc_mem, 0, 0, hicon, w, h, 0, None, 3)  # DI_NORMAL=3

    # 获取像素数据
    class BITMAPINFOHEADER(ctypes.Structure):
        _fields_ = [
            ("biSize", wintypes.DWORD),
            ("biWidth", wintypes.LONG),
            ("biHeight", wintypes.LONG),
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
    bih.biHeight = h  # 正值 = 底部在上
    bih.biPlanes = 1
    bih.biBitCount = 32
    bih.biCompression = 0  # BI_RGB
    bih.biSizeImage = w * h * 4

    buf = (ctypes.c_byte * bih.biSizeImage)()
    gdi32.GetDIBits(hdc_mem, hbmp, 0, h, buf, ctypes.byref(bih), 0)

    # 组装 .ico 文件
    # ICO 格式: ICO header + ICO directory entry + BMP data (without BITMAPFILEHEADER)
    ico_header = struct.pack("<HHH", 0, 1, 1)  # reserved, type=1(icon), count=1
    
    # BMP 像素数据 (去掉 BITMAPFILEHEADER，保留 BITMAPINFOHEADER + 像素)
    bmp_data = bytearray(ctypes.sizeof(bih))
    ctypes.memmove(bmp_data, ctypes.addressof(bih), ctypes.sizeof(bih))
    bmp_data += bytes(buf[:bih.biSizeImage])

    offset = len(ico_header) + 16  # header + one dir entry (16 bytes)
    dir_entry = struct.pack("<BBBBHHII", w if w < 256 else 0, h if h < 256 else 0,
                            0, 0, 1, 32, len(bmp_data), offset)

    with open(path, "wb") as f:
        f.write(ico_header)
        f.write(dir_entry)
        f.write(bmp_data)

    gdi32.SelectObject(hdc_mem, old_bmp)
    gdi32.DeleteObject(hbmp)
    gdi32.DeleteDC(hdc_mem)
    user32.ReleaseDC(0, hdc)
    user32.DestroyIcon(hicon)

    print(f"图标已保存: {os.path.abspath(path)}  ({w}x{h})")
    return True


def main():
    qq_exe = None
    if len(sys.argv) > 1:
        qq_exe = sys.argv[1]
    else:
        for p in _DEFAULT_PATHS:
            if os.path.isfile(p):
                qq_exe = p
                break
    
    if qq_exe is None:
        print("未找到 QQ.exe。请手动指定路径：")
        print("  python extract_qq_icon.py \"你的QQ安装路径\\QQ.exe\"")
        return 1

    print(f"找到 QQ.exe: {qq_exe}")
    output = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "qq_icon.ico")
    if extract_icon(qq_exe, output):
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
