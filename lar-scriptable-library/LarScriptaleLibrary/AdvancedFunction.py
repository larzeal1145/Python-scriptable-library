import ctypes
import time
from ctypes import wintypes
import sys
import keyboard
from LarScriptaleLibrary.BasicsFunction import *

# ==============================================
# 鼠标平滑移动
# ==============================================

user32 = ctypes.WinDLL("user32", use_last_error=True)

# 常量
INPUT_MOUSE = 0
MOUSEEVENTF_MOVE = 0x0001

# 结构体定义
class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ("dx", wintypes.LONG),
        ("dy", wintypes.LONG),
        ("mouseData", wintypes.DWORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ctypes.POINTER(wintypes.ULONG)),
    ]

class INPUT(ctypes.Structure):
    _fields_ = [
        ("type", wintypes.DWORD),
        ("mi", MOUSEINPUT),
    ]

def _mouse_move_relative(dx, dy):
    inp = INPUT()
    inp.type = INPUT_MOUSE
    inp.mi.dx = dx
    inp.mi.dy = dy
    inp.mi.dwFlags = MOUSEEVENTF_MOVE
    user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))

def mouse_move_smooth(dx_total, dy_total, duration=0.3, steps=50):
    """
     | 平滑相对移动鼠标
     | dx_total:总横向位移
     | dy_total:总纵向位移
     | duration:总耗时秒
     | steps:分多少步移动
     | 当位移<=25时无法运行,你可以检测鼠标当前坐标然后加上偏移量用瞬间移动
    """
    step_dx = dx_total / steps
    step_dy = dy_total / steps
    delay = duration / steps  # 每步延时

    for _ in range(steps):
        _mouse_move_relative(int(round(step_dx)), int(round(step_dy)))
        time.sleep(delay)


VK_CAPS = 0x14
VK_SPACE = 0x20

CHAR_VK = {
    '0':0x30,'1':0x31,'2':0x32,'3':0x33,'4':0x34,
    '5':0x35,'6':0x36,'7':0x37,'8':0x38,'9':0x39,
    'a':0x41,'b':0x42,'c':0x43,'d':0x44,'e':0x45,
    'f':0x46,'g':0x47,'h':0x48,'i':0x49,'j':0x4A,
    'k':0x4B,'l':0x4C,'m':0x4D,'n':0x4E,'o':0x4F,
    'p':0x50,'q':0x51,'r':0x52,'s':0x53,'t':0x54,
    'u':0x55,'v':0x56,'w':0x57,'x':0x58,'y':0x59,'z':0x5A,

    '`': 0xC0,
    '-': 0xBD, '=': 0xBB,
    '[': 0xDB, ']': 0xDD, '\\': 0xDC,
    ';': 0xBA, "'": 0xDE,
    ',': 0xBC, '.': 0xBE, '/': 0xBF,
    ' ': VK_SPACE,  # 空格
}

def continuous_press(text: str, interval: float = 0.04):
    """
     | 可连续点击，无需键码
     | 暂不支持 “
    :param text: ------键盘输入 "123 Abc,[/]"
    :param interval: 延迟 可选,不传参则视作 0.04
    :return: param text
    """
    caps_on = False
    for ch in text:
        if ch == ' ':
            key_press(VK_SPACE)
            time.sleep(interval)
            continue

        need_caps = ch.isupper()
        cur_char = ch.lower()

        # 只切换大小写，不加延时
        if need_caps != caps_on:
            key_press(VK_CAPS)
            caps_on = need_caps

        # 仅字符按键后休眠间隔
        if cur_char in CHAR_VK:
            key_press(CHAR_VK[cur_char])
            time.sleep(interval)

    # 结尾复原大小写也不加延时
    if caps_on:
        key_press(VK_CAPS)

if __name__ == "__main__":

    # time.sleep(6)
    # # 平滑右移200
    # mouse_move_smooth(2000, 0, 0.1)
    # time.sleep(0.3)
    #
    # # 平滑下移200
    # mouse_move_smooth(0, 200, 0.1)
    # time.sleep(0.3)
    #
    # # 平滑左移200
    # mouse_move_smooth(-200, 0, 0.4)
    # time.sleep(0.3)
    #
    # # 平滑上移200
    # mouse_move_smooth(0, -200, 0.4)
    continuous_press("123,AbC", 0.1)
    pass
