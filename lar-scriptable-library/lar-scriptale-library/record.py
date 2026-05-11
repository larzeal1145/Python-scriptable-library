import time
import os
import threading
from ctypes import *

from GetInfo import *
from keyboard import *
from BasicsFunction import *
from mouse import *

# ======================
# 全局停止标志（线程安全）
# ======================
stop_flag = False

# ======================
# 鼠标绝对坐标
# ======================
user32 = windll.user32


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def _get_absolute_pos():
    pt = POINT()
    user32.GetCursorPos(byref(pt))
    return pt.x, pt.y


# ======================
# 中断监听线程 —— 已全部改用 check_key()
# ======================
def _stop_listener():
    global stop_flag
    while not stop_flag:
        # 检查 Alt(0x12) 和 O(0x4F)
        alt_state = check_key(0x12)
        o_state = check_key(0x4F)

        # 只要两个键都触发（down）就停止
        if alt_state is not None and o_state is not None:
            print("\n[中断] 收到停止信号")
            stop_flag = True
            break
        time.sleep(0.02)


# ======================
# 自动生成文件名
# ======================
def _create_record_filename():
    index = 1
    while True:
        timestr = time.strftime("%Y%m%d_%H%M%S")
        filename = f"record_{index}_{timestr}.txt"
        if not os.path.exists(filename):
            return filename
        index += 1


# ======================
# 配置
# ======================
INTERVAL = 1 / 50


# ======================
# 录制主函数
# ======================
def start_record():
    """
    进行录制
     | :param filename: record_1_20260424_175845
     | 录制_1号_年月日_今日具体时间
     | :return: error
     | 按 alt + o 停止
    """
    global stop_flag
    stop_flag = False  # 重置标志

    RECORD_FILE = _create_record_filename()

    # 启动中断监听线程
    threading.Thread(target=_stop_listener, daemon=True).start()

    # 起始位置
    start_x, start_y = _get_absolute_pos()
    with open(RECORD_FILE, "w", encoding="utf-8") as f:
        f.write(f"START_POS                      {start_x} {start_y}\n")

    print(f"开始录制 → 文件：{RECORD_FILE}")
    print("按 alt + o 停止")

    last = time.time()
    last_x, last_y = _get_absolute_pos()  # 初始坐标

    # ======================
    # 主录制循环
    # ======================
    while not stop_flag:
        now = time.time()
        if now - last < INTERVAL:
            continue
        last = now

        # 获取当前坐标
        current_x, current_y = _get_absolute_pos()

        # 计算偏移
        delta_x = current_x - last_x
        delta_y = current_y - last_y

        # 记录移动
        if delta_x != 0 or delta_y != 0:
            ts = f"{time.time():.3f}"
            line = f"{ts} MOUSE_MOVE      {delta_x} {delta_y}"
            with open(RECORD_FILE, "a", encoding="utf-8") as f:
                f.write(line + "\n")

        # 更新坐标
        last_x = current_x
        last_y = current_y

        # ============= 鼠标按键 =============
        left = check_mouse_left_change()
        if left is not None:
            ts = f"{time.time():.3f}"
            action = left.split()[-1]
            line = f"{ts} MOUSE_LEFT                                 {action}"
            with open(RECORD_FILE, "a", encoding="utf-8") as f:
                f.write(line + "\n")

        right = check_mouse_right_change()
        if right is not None:
            ts = f"{time.time():.3f}"
            action = right.split()[-1]
            line = f"{ts} MOUSE_RIGHT                                {action}"
            with open(RECORD_FILE, "a", encoding="utf-8") as f:
                f.write(line + "\n")

        middle = check_mouse_middle_change()
        if middle is not None:
            ts = f"{time.time():.3f}"
            action = middle.split()[-1]
            line = f"{ts} MOUSE_MIDDLE                               {action}"
            with open(RECORD_FILE, "a", encoding="utf-8") as f:
                f.write(line + "\n")

        # ============= 滚轮 =============
        wheel = check_wheel_change()
        if wheel is not None:
            ts = f"{time.time():.3f}"
            action = wheel.split()[2]
            line = f"{ts} MOUSE_WHEEL                                {action}"
            with open(RECORD_FILE, "a", encoding="utf-8") as f:
                f.write(line + "\n")

        # ============= 键盘 =============
        key_data = check_key()
        if key_data is not None:
            try:
                parts = key_data.split()
                hex_key = parts[1]
                state = parts[2]
                ts = f"{time.time():.3f}"
                line = f"{ts} KEY {hex_key}                        {state}"
                with open(RECORD_FILE, "a", encoding="utf-8") as f:
                    f.write(line + "\n")
            except:
                pass

    print("录制停止")


# ======================
# 启动
# ======================
if __name__ == "__main__":
    enable_fast_relative()
    start_record()