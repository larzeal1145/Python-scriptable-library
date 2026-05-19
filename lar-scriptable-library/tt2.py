from LarScriptaleLibrary.BasicsFunction import *
from keyboard import *
import time
import winsound

s = False
get_admin()
print('alt+i预备，f启动，alt+o退出')
if __name__ == '__main__':
    while True:
        time.sleep(0.01)
        if is_pressed('alt + i'):
            s = not s
            if s:
                winsound.Beep(800,150)
            else:
                winsound.Beep(600,150)

        if is_pressed('alt + o'):
            winsound.Beep(450,150)
            break

        if s:
            if is_pressed('f'):

                key_press(0x35)
                time.sleep(0.02)
                key_press(0x35)
                time.sleep(0.02)
                key_press(0x45)

                key_press(0x32)
                time.sleep(0.02)
                key_press(0x32)
                time.sleep(0.02)

                key_press(0x45)
                time.sleep(1.2)
                key_press(0x45)
                time.sleep(1.2)
                key_press(0x45)


                time.sleep(0.02)
                key_press(0x33)
                time.sleep(0.02)
                key_press(0x33)
                time.sleep(0.05)
                key_press(0x45)

                time.sleep(0.02)
                key_press(0x34)               # 4
                time.sleep(0.02)
                key_press(0x45)      # e
                time.sleep(0.02)
                key_press(0x45)
                time.sleep(0.02)
                key_press(0x34)               # 4 激活
                time.sleep(0.02)
                key_press(0x34)               # 4 激活
                time.sleep(0.02)

                key_press(0x32)
                time.sleep(0.01)
                key_press(0x31)
                time.sleep(0.01)
                key_press(0x31)
                time.sleep(0.01)

                key_press(0x45)
                time.sleep(0.1)
                key_press(0x45)

                winsound.Beep(600,150)
                s = False
