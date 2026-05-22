import time
import pyautogui
import ctypes
import ctypes.wintypes


# ==============================================
# 原有找图功能
# ==============================================
def _find_image_on_screen(target_img_path, confidence=0.8):
    try:
        match_pos = pyautogui.locateOnScreen(
            target_img_path,
            confidence=confidence,
            grayscale=True
        )
        if match_pos:
            center_x, center_y = pyautogui.center(match_pos)
            print(f"找到目标 位置：{match_pos}，中点：({center_x}, {center_y})")
            return match_pos, (center_x, center_y)
        else:
            print("未找到")
            return None, None
    except Exception as e:
        print(f"失败：{e}")
        return None, None



def find_photo(target):
    """
    | 检查特定图像是否存在
    | param -------> 任何图片 123.png
    :return:
    """
    match_region, match_center = _find_image_on_screen(target, confidence=0.7)
    if match_center:      # NOQA
        return None, None



# ==============================================
# 取色 + 颜色校验（严格按你要求的格式返回）
# ==============================================
user32 = ctypes.WinDLL('user32', use_last_error=True)
gdi32 = ctypes.WinDLL('gdi32', use_last_error=True)


def get_pixel(x, y):
    """
    | 获取特定坐标的16进制色号
    | param -------> x, y
    | 返回格式---------------------------> [C] x y #FFFFF
    """
    hdc = user32.GetDC(None)
    color = gdi32.GetPixel(hdc, x, y)
    user32.ReleaseDC(None, hdc)

    r = color & 0xFF
    g = (color >> 8) & 0xFF
    b = (color >> 16) & 0xFF
    hex_color = f"#{r:02X}{g:02X}{b:02X}"

    return f"[C] {x} {y} {hex_color}"


def check_color(x, y, hex_color):
    """
    | 检查特定坐标像素的色号
    | param -------> x, y, "#FFFFF"
    | 返回格式---------------------------> True / False
    """
    res = get_pixel(x, y)
    current_color = res.split()[-1]
    match = current_color.lower() == hex_color.lower()

    return match



# ==============================================
# 测试
# ==============================================
if __name__ == '__main__':
    time.sleep(2)

    # 获取颜色
    print(get_pixel(500, 500))

    # 检查颜色
    print(check_color(500, 500, "#FFFFFF"))