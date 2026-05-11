import ctypes
from ctypes import wintypes
import time

user32 = ctypes.WinDLL("user32", use_last_error=True)

# ==========================
# 定义 POINT 结构
# ==========================
class POINT(ctypes.Structure):
    _fields_ = [("x", wintypes.LONG), ("y", wintypes.LONG)]

# ==========================
# 两个开关
# ==========================
_enable_fast_relative = False
_enable_digital_conversion = False

def enable_fast_relative():
    """
    打开 enable_fast_relative 功能
     | 在屏幕上生成 30*30 像素网格,只有鼠标经过时才返回信息,以节省性能
    """
    global _enable_fast_relative
    _enable_fast_relative = True

def disable_fast_relative():
    """
    关掉 enable_fast_relative 功能
    """
    global _enable_fast_relative
    _enable_fast_relative = False

# ==========================
# 数字转换装饰器
# ==========================
def digital_convert(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if _enable_digital_conversion and result is not None:
            convert_map = {
                "down": 1, "up": 0,
                "forward": 1, "backward": -1, "stop": 0
            }
            return convert_map.get(result, result)
        return result
    return wrapper

# ==========================
# 全局状态
# ==========================
_key_state = {}
_mouse_l = False
_mouse_r = False
_mouse_m = False
_wheel_prev = 0

_last_x = _last_y = None
GRID = 30

# ==========================
# 键盘
# ==========================
@digital_convert
def _check_key(vk=None):
    if vk is not None:
        if vk >= 0x08:
            current = (user32.GetAsyncKeyState(vk) & 0x8000) != 0
            prev = _key_state.get(vk, False)
            _key_state[vk] = current
            if current and not prev:
                return f"[按键] 0x{vk:02X} down"
            elif not current and prev:
                return f"[按键] 0x{vk:02X} up"
    else:
        for vk_code in range(0x08, 256):
            current = (user32.GetAsyncKeyState(vk_code) & 0x8000) != 0
            prev = _key_state.get(vk_code, False)
            _key_state[vk_code] = current
            if current and not prev:
                return f"[按键] 0x{vk_code:02X} down"
            elif not current and prev:
                return f"[按键] 0x{vk_code:02X} up"
    return None

def check_key(vk=None):
    res = _check_key(vk)
    if res is not None:
        return res

# ==========================
# 鼠标左键
# ==========================
@digital_convert
def _check_mouse_left_change():
    global _mouse_l
    current = (user32.GetAsyncKeyState(0x01) & 0x8000) != 0
    prev = _mouse_l
    _mouse_l = current
    if current and not prev:
        return "[鼠标] mouse_left down"
    if not current and prev:
        return "[鼠标] mouse_left up"
    return None

def check_mouse_left_change():
    res = _check_mouse_left_change()
    if res is not None:
        return res

# ==========================
# 鼠标右键
# ==========================
@digital_convert
def _check_mouse_right_change():
    global _mouse_r
    current = (user32.GetAsyncKeyState(0x02) & 0x8000) != 0
    prev = _mouse_r
    _mouse_r = current
    if current and not prev:
        return "[鼠标] mouse_right down"
    if not current and prev:
        return "[鼠标] mouse_right up"
    return None

def check_mouse_right_change():
    res = _check_mouse_right_change()
    if res is not None:
        return res

# ==========================
# 鼠标中键
# ==========================
@digital_convert
def _check_mouse_middle_change():
    global _mouse_m
    current = (user32.GetAsyncKeyState(0x04) & 0x8000) != 0
    prev = _mouse_m
    _mouse_m = current
    if current and not prev:
        return "[鼠标] mouse_middle down"
    if not current and prev:
        return "[鼠标] mouse_middle up"
    return None

def check_mouse_middle_change():
    res = _check_mouse_middle_change()
    if res is not None:
        return res

# ==========================
# ✅ 鼠标滚轮 - 零错误终极版（只使用 GetAsyncKeyState，永不报错）
# ==========================
@digital_convert
def _check_wheel_change():
    global _wheel_prev
    # 鼠标滚轮 标准键码：上 0xA0  下 0xA1
    wheel_up = user32.GetAsyncKeyState(0xA0) & 0x8000
    wheel_down = user32.GetAsyncKeyState(0xA1) & 0x8000

    if wheel_up:
        return "forward"
    if wheel_down:
        return "backward"
    return None

def check_wheel_change():
    res = _check_wheel_change()
    if res is not None:
        return res

# ==========================
# 鼠标移动
# ==========================
def _get_mouse_delta():
    global _last_x, _last_y
    pt = POINT()
    user32.GetCursorPos(ctypes.byref(pt))
    x, y = pt.x, pt.y

    if _last_x is None:
        _last_x = x
        _last_y = y
        return 0, 0

    dx = x - _last_x
    dy = y - _last_y
    _last_x = x
    _last_y = y
    return dx, dy

def get_mouse_delta():
    return _get_mouse_delta()

# ==========================
# 鼠标坐标
# ==========================
def _get_mouse_point():
    pt = POINT()
    user32.GetCursorPos(ctypes.byref(pt))
    return f"[鼠标] x {pt.x} y {pt.y}"

def get_mouse_point():
    return _get_mouse_point()

# ==========================
# 主循环
# ==========================
if __name__ == '__main__':
    while True:
        print(check_wheel_change())
        time.sleep(.01)