将就看吧

--------------------------------------------------------


        BasicsFunction

mouse_move()

光标瞬间移动到指定位置。mouse_move (500, 500)
鼠标瞬间移动到坐标 500, 500。游戏会话内可能无法使用，主要用于各类目录操作。
对应的是AdvancedFunction的mouse_move_smooth()

mouse_click()

鼠标点击

mouse_left_down()

按住鼠标左键

mouse_left_up()

松开鼠标左键

其他两个按键原理相同，使用 right 和 middle

mouse_wheel()

每 120 个单位视为鼠标滚轮滚动一格。当然时间输入 "1" 也可以。正数表示向上滚动，负数表示向下滚动。

mouse_wheel_up()

滚轮向上滚动一格

mouse_wheel_down()

滚轮向下滚动一格

key_press()

key_press (0x41)持续按住 A 键

key_down()

key_down(0x41)按下键盘 A 键

key_up()

key_up(0x41)松开键盘 A 键

take_admin()

获取管理员权限

is_admin()

检查程序是否拥有管理员权限

get_admin()

检查是否拥有管理员权限，若没有则申请整合了 is_admin 和 take_admin

        AdvancedFunction
        
continuous_press()

调用 key_press () 函数并持续执行，无需再输入键码，可直接输入字符串，但不支持 ["] 格式

mouse_move_smooth()

调用 mouse_move () 实现鼠标平滑移动 | 鼠标平滑相对移动| dx_total: 水平总位移| dy_total: 垂直总位移| duration: 总耗时，单位秒| steps: 分多少步移动| 使用默认步数时，若位移≤25 则无法执行

        FindTarget
        
find_photo()

find_photo ('123123.png')查找匹配的图片用于条件语句中，检测到对应图片后触发后续事件

get_pixel()

| 获取指定坐标的十六进制颜色码| 参数 -------> x, y
| 返回格式 -----------------------> #FFFFF

check_color()

| 检查指定坐标像素的颜色码| 参数 -------> x, y, "#FFFFF"
| 返回格式 ----------------------> True / False

        GetInfo
        
check_mouse_left_change()

监听鼠标左键，输出 "up" 和 "down"，无信号返回 None

check_mouse_right_change()

监听鼠标右键，输出 "up" 和 "down"，无信号返回 None

check_mouse_middle_change()

监听鼠标中键，输出 "up" 和 "down"，无信号返回 None

check_wheel_change()

监听鼠标滚轮动作，输出 "forward"、"backward" 和 "stop"，无信号返回 None

obstructs_check_key()

阻塞式键盘监听，阻塞线程直至检测到按键状态改变

obstructs_check_mouse_left_change()

阻塞式监听鼠标左键，阻塞直至状态改变，输出 "up" 和 "down"

obstructs_check_mouse_right_change()

阻塞式监听鼠标右键，阻塞直至状态改变，输出 "up" 和 "down"

obstructs_check_mouse_middle_change()

阻塞式监听鼠标中键，阻塞直至状态改变，输出 "up" 和 "down"

obstructs_check_wheel_change()

阻塞式监听鼠标滚轮，阻塞直至检测到滚动动作，输出 "forward"、"backward" 和 "stop"

get_mouse_relative()

监听鼠标移动，每秒检测 50 次

check_key()

监听键盘，可传入指定键码仅检测该键，或不传参检测整个键盘，无信号返回 None

enable_fast_relative()

启用鼠标快速移动检测，启用后获取屏幕分辨率并划分为 30*30 像素网格，仅鼠标穿过网格线时回传移动坐标，以优化程序性能

disable_fast_relative()

关闭鼠标快速移动检测，恢复信息回传频率，精度更高但更卡顿

        DllInjection
        
dll_injection()

目前暂无效果

        record
        
start_recode()

录制后续鼠标键盘操作信息，以文本文档形式返回

        replay
        
start_replay()
        
回放文档

--------------------------------------------------------
        
        BasicsFunction

`mouse_move_smooth()`

mouse_move_smooth(100,100,2)

Mouse smooth/relative movement (x-axis, y-axis, required time)

Used within the game session


`mouse_move()`

The cursor instantly moves to the designated position.

mouse_move(500, 500)

The mouse moved instantaneously to the coordinates 500, 500.

The game may not be usable within the game session, and is mainly used for various directories.


`mouse_click()`

mouse click



`mouse_left_down()`

Press the left mouse button



`mouse_left_up()`

Release the left mouse button



The other two keys work on the same principle as well. Use 'right' and 'middle'



`mouse_wheel()`

Every 120 units is regarded as one rotation of the mouse wheel.

Of course, it's fine to input "1" for the time as well.

Positive numbers indicate upward scrolling, while negative numbers indicate the opposite direction.


`mouse_wheel_up()`

The roller rolls up one step.

`mouse_wheel_down()`

The roller rolls down one step.


`key_press()`

key_press(0x41)

Keep pressing the key A continuously.


`key_down(0x41)`

Press the key A on the keyboard.


`key_up(0x41)`

Keyboard lifted up A

`take_admin()`

Obtain administrative privileges.


`is_admin()`

Check whether the program has administrator privileges

`get_admin()`

Check if there is administrator privileges. If not, apply for them.

integrated 'is_admin' and 'take_admin'

        AdvancedFunction

`continuous_press()`

Call the key_press() function and execute it continuously. No longer is it necessary to input the key code; you can directly input the string, but the ["] format is not supported.

`mouse_move_smooth()`

Call mouse_move() to smoothly move the mouse | Smooth relative mouse movement
| dx_total: Total horizontal displacement
| dy_total: Total vertical displacement
| duration: Total time consumed in seconds
| steps: How many steps to move
| When the default number of steps is used, if the displacement is <= 25, it cannot be executed

        FindTarget

`find_photo()`

find_photo('123123.png')

Search for matching images

Used to be placed in conditional statements, triggering subsequent events upon detecting the corresponding image.

`get_pixel()`

| Obtain the hexadecimal color code for a specific coordinate 
| param -------> x, y
| Return format -----------------------> [C] x y #FFFFF

`check_color()`

|Check the color code of a specific coordinate pixel 
| param -------> x, y, "#FFFFF"
| Return format ----------------------> True / False

        GetInfo

`check_mouse_left_change()`

Listen to the left mouse button and output "up" and "down"，No signal returns None

`check_mouse_right_change()`

Listen to the right mouse button and output "up" and "down"，No signal returns None

`check_mouse_middle_change()`

Listen to the middle mouse button and output "up" and "down"，No signal returns None

`check_wheel_change()`

Monitor the mouse wheel movement and output "forward", "backward" and "stop"，No signal returns None

`obstructs_check_key()`

Blocking keyboard monitoring, block the thread until a key state change is detected

`obstructs_check_mouse_left_change()`

Blocking listens to the left mouse button and blocks until the state changes to output "up" and "down"

`obstructs_check_mouse_right_change()`

Blocking listens to the right mouse button and blocks until the state changes to output "up" and "down"

`obstructs_check_mouse_middle_change()`

Blocking listens to the middle mouse button and blocks until the state changes to output "up" and "down"

`obstructs_check_wheel_change()`

Blocking monitors the mouse wheel, blocks until scrolling action is detected, output "forward", "backward" and "stop"

`get_mouse_relative()`

Monitor the movement of the mouse and detect it 50 times per second.

`check_key()`

Monitor the keyboard. You can pass in specific key codes, and then only detect this key. Or no parameters are passed, and the entire keyboard is detected. No signal returns None

`enable_fast_relative()`

Enable the quick mouse movement detection. After enabling it, the screen resolution will be obtained and divided into a 30*30 pixel grid. Only when the mouse passes through the grid lines will the movement coordinates be sent back, in order to optimize the program performance.

`disable_fast_relative()`

Disable the quick mouse movement detection, the frequency of returning information is restored, it becomes more accurate but also more laggy.

        DllInjection

`dll_injection()`

It hasn't had any effect yet.

        record

`start_recode()`

Record the subsequent output information from the mouse and keyboard and return it in the form of a text document.

        replay

`start_replay()`

Replay the specified text document.
