import ctypes
from ctypes import wintypes
import time
from pynput import *

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
# ==========================
# 新增：精简返回模式开关 默认关闭
# ==========================
_enable_streamline_return = False

def enable_streamline_return():
    """
    开启精简传回模式，只返回最基础 up/down、纯坐标数字
    """
    global _enable_streamline_return
    _enable_streamline_return = True
    print("[Streamline] 精简返回模式 启用")

def disable_streamline_return():
    """
    关闭精简传回模式，恢复原带标签格式输出
    """
    global _enable_streamline_return
    _enable_streamline_return = False
    print("[Streamline] 精简返回模式 关闭")

def enable_fast_relative():
    """
     | 打开 enable_fast_relative 功能
     | 在屏幕上生成 30*30 像素网格, 只有鼠标经过时才返回信息, 牺牲精度以节省性能
     | 只要不是 micropython 就没有必要打开这个东西, 只要不是1G运存就没有必要开这个东西
    """
    global _enable_fast_relative
    _enable_fast_relative = True
    print("[Fast] 鼠标快速模式 启用")

def disable_fast_relative():
    """
    关掉 enable_fast_relative 功能
    """
    global _enable_fast_relative
    _enable_fast_relative = False
    print("[Fast] 鼠标快速模式 关闭")

# def enable_digital_conversion():
#     """
#     暂时无效果
#     :return:
#     """
#     global _enable_digital_conversion
#     _enable_digital_conversion = True
#     print("[Digital] 数字转换 启用：1=按下 0=抬起 -1=滚轮下")
#
# def disable_digital_conversion():
#     """
#     暂时无效果
#     :return:
#     """
#     global _enable_digital_conversion
#     _enable_digital_conversion = False
#     print("[Digital] 数字转换 关闭")

# ==========================
# 全局状态
# ==========================
_key_state = {}
_mouse_l = False
_mouse_r = False
_mouse_m = False
_wheel_state = None
_total_delta = 0
_last_scroll_time = time.time()
_has_scrolled = False  #-------------- 标记是否滚动

# 鼠标移动
_last_x = _last_y = None
_last_gx = _last_gy = None
GRID = 30

# ==========================
# 键盘检测
# ==========================
def obstructs_check_key(vk=None):
    """
    | 检查键盘状态
    | 阻断型-检查到动作前阻塞当前线程-直到出现变化
    | 返回格式---------------------------> [K] 0X** up/down
    | :param vk/none:
    | :return:
    """
    while True:
        # 单个按键检测
        if vk is not None:
            if vk < 0x08:
                continue

            current = (user32.GetAsyncKeyState(vk) & 0x8000) != 0
            prev = _key_state.get(vk, False)
            _key_state[vk] = current

            if current and not prev:
                if _enable_streamline_return:
                    return "down"
                return f"[K] 0x{vk:02X} down"
            if not current and prev:
                if _enable_streamline_return:
                    return "up"
                return f"[K] 0x{vk:02X} up"

        # 全键盘检测
        else:
            for vk_code in range(0x08, 256):
                current = (user32.GetAsyncKeyState(vk_code) & 0x8000) != 0
                prev = _key_state.get(vk_code, False)
                _key_state[vk_code] = current

                if current and not prev:
                    if _enable_streamline_return:
                        return "down"
                    return f"[K] 0x{vk_code:02X} down"
                if not current and prev:
                    if _enable_streamline_return:
                        return "up"
                    return f"[K] 0x{vk_code:02X} up"

# ==========================
# 【新增】非阻塞键盘监听 无动作返回None
# ==========================
def check_key(vk=None):
    if vk is not None:
        if vk < 0x08:
            return None
        current = (user32.GetAsyncKeyState(vk) & 0x8000) != 0
        prev = _key_state.get(vk, False)
        _key_state[vk] = current
        if current and not prev:
            if _enable_streamline_return:
                return "down"
            return f"[K] 0x{vk:02X} down"
        if not current and prev:
            if _enable_streamline_return:
                return "up"
            return f"[K] 0x{vk:02X} up"
        return None
    for vk_code in range(0x08, 256):
        current = (user32.GetAsyncKeyState(vk_code) & 0x8000) != 0
        prev = _key_state.get(vk_code, False)
        _key_state[vk_code] = current
        if current and not prev:
            if _enable_streamline_return:
                return "down"
            return f"[K] 0x{vk_code:02X} down"
        if not current and prev:
            if _enable_streamline_return:
                return "up"
            return f"[K] 0x{vk_code:02X} up"
    return None

# ==========================
# 鼠标位置 返回格式---------------------------> [鼠标] x 100 y 100
# ==========================
def get_mouse_point():
    """
     | 获取鼠标当前坐标
     | 绝对坐标
     | 返回格式---------------------------> [M] absolute ** **
    """
    pt = POINT()
    user32.GetCursorPos(ctypes.byref(pt))
    if _enable_streamline_return:
        return f"{pt.x} {pt.y}"
    return f"[M] absolute {pt.x} {pt.y}"

# ==========================
# 鼠标左键 返回格式---------------------------> [鼠标] mouse_left down/up
# ==========================
def obstructs_check_mouse_left_change():
    """
     | 检测鼠标左键状态
     | 阻断型-检查到动作前阻塞当前线程-直到出现变化
     | 返回格式---------------------------> [M] mouse_left down/up | None
    """
    global _mouse_l
    while True:
        current = (user32.GetAsyncKeyState(0x01) & 0x8000) != 0
        prev = _mouse_l
        _mouse_l = current

        if current and not prev:
            if _enable_streamline_return:
                return "down"
            return "[M] mouse_left down"
        if not current and prev:
            if _enable_streamline_return:
                return "up"
            return "[M] mouse_left up"

# ==========================
# 【新增】非阻塞鼠标左键 无动作返回None
# ==========================
def check_mouse_left_change():
    global _mouse_l
    current = (user32.GetAsyncKeyState(0x01) & 0x8000) != 0
    prev = _mouse_l
    _mouse_l = current
    if current and not prev:
        if _enable_streamline_return:
            return "down"
        return "[M] mouse_left down"
    if not current and prev:
        if _enable_streamline_return:
            return "up"
        return "[M] mouse_left up"
    return None

# ==========================
# 鼠标右键（返回格式：[鼠标] mouse_right down/up）
# ==========================
def obstructs_check_mouse_right_change():
    """
    | 检测鼠标右键状态
    | 阻断型-检查到动作前阻塞当前线程-直到出现变化
    | 返回格式---------------------------> [M] mouse_right down/up
    """
    global _mouse_r
    while True:
        current = (user32.GetAsyncKeyState(0x02) & 0x8000) != 0
        prev = _mouse_r
        _mouse_r = current

        if current and not prev:
            if _enable_streamline_return:
                return "down"
            return "[M] mouse_right down"
        if not current and prev:
            if _enable_streamline_return:
                return "up"
            return "[M] mouse_right up"

# ==========================
# 【新增】非阻塞鼠标右键 无动作返回None
# ==========================
def check_mouse_right_change():
    global _mouse_r
    current = (user32.GetAsyncKeyState(0x02) & 0x8000) != 0
    prev = _mouse_r
    _mouse_r = current
    if current and not prev:
        if _enable_streamline_return:
            return "down"
        return "[M] mouse_right down"
    if not current and prev:
        if _enable_streamline_return:
            return "up"
        return "[M] mouse_right up"
    return None

# ==========================
# 鼠标中键（返回格式：[鼠标] mouse_middle down/up）
# ==========================
def obstructs_check_mouse_middle_change():
    """
     | 检测鼠标中键状态
     | 阻断型-检查到动作前阻塞当前线程-直到出现变化
     | 返回格式---------------------------> [M] mouse_right down/up | None
    """
    global _mouse_m
    while True:
        current = (user32.GetAsyncKeyState(0x04) & 0x8000) != 0
        prev = _mouse_m
        _mouse_m = current

        if current and not prev:
            if _enable_streamline_return:
                return "down"
            return "[M] mouse_middle down"
        if not current and prev:
            if _enable_streamline_return:
                return "up"
            return "[M] mouse_middle up"

# ==========================
# 【新增】非阻塞鼠标中键 无动作返回None
# ==========================
def check_mouse_middle_change():
    global _mouse_m
    current = (user32.GetAsyncKeyState(0x04) & 0x8000) != 0
    prev = _mouse_m
    _mouse_m = current
    if current and not prev:
        if _enable_streamline_return:
            return "down"
        return "[M] mouse_middle down"
    if not current and prev:
        if _enable_streamline_return:
            return "up"
        return "[M] mouse_middle up"
    return None

# ==========================
# 鼠标滚轮
# ==========================
def on_scroll(*args):
    """
    没有用处
    """
    global _wheel_state, _total_delta, _last_scroll_time, _has_scrolled
    dy = args[3]
    _total_delta += dy
    _wheel_state = "forward" if dy > 0 else "backward"
    _last_scroll_time = time.time()
    _has_scrolled = True

# 后台的监听
listener = mouse.Listener(on_scroll=on_scroll)
listener.daemon = True
listener.start()

def check_wheel_change():
    """
    | 滚轮检测
    | 返回格式---------------------------> [M]  backward/forward/stop | None
    :return:
    """
    global _wheel_state, _total_delta, _has_scrolled

    if not _has_scrolled:
        return None

    # 判断是否停止---------------------------0.2秒无动作
    is_stopped = time.time() - _last_scroll_time > 0.2
    res = _wheel_state
    _wheel_state = None

    # 正在滚动
    if res and not is_stopped:
        if _enable_streamline_return:
            return res
        return f"[M] wheel {res}"

    # 滚动结束 → 输出一次停止，然后重置
    elif is_stopped:
        val = int(_total_delta)
        if _enable_streamline_return:
            output = f"stop {val}"
        else:
            output = f"[M] wheel stop {val}"
        _total_delta = 0
        _has_scrolled = False
        return output

    # 平时无动作
    return None

# ==========================
# 【新增】阻塞型滚轮检测 直到滚动才返回
# ==========================
def obstructs_check_wheel_change():
    while True:
        res = check_wheel_change()
        if res is not None:
            return res
        time.sleep(0.01)

# ==========================
# 鼠标移动
# ==========================
def get_mouse_delta():
    """
         | 获取鼠标运动时的坐标
         | 相对坐标
         | 返回格式---------------------------> [M] delta 100 100
        """
    global _last_x, _last_y, _last_gx, _last_gy
    pt = POINT()
    user32.GetCursorPos(ctypes.byref(pt))
    x = pt.x
    y = pt.y

    if _last_x is None:
        _last_x = x
        _last_y = y
        _last_gx = x // GRID
        _last_gy = y // GRID
        return 0, 0

    if not _enable_fast_relative:
        dx = x - _last_x
        dy = y - _last_y
        _last_x = x
        _last_y = y
        if _enable_streamline_return:
            return f"{dx} {dy}"
        return f"[M] delta {dx}, {dy}"

    gx = x // GRID
    gy = y // GRID
    if gx == _last_gx and gy == _last_gy:
        return 0, 0

    dx = x - _last_x
    dy = y - _last_y
    _last_x = x
    _last_y = y
    _last_gx = gx
    _last_gy = gy
    if _enable_streamline_return:
        return f"{dx * GRID} {dy * GRID}"
    return f"[M] {dx * GRID}, {dy * GRID}"

# ==========================
# 主程序
# ==========================
if __name__ == '__main__':
    pass