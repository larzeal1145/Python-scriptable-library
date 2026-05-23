## Lar-scriptable-library

基于python的脚本库

尝试以最简便的封装使复代码运行

不要用于商业


机翻的将就看吧
# -----------------------------------------------
## 基础功能 BasicsFunction
`mouse_move()`
鼠标瞬间移动至指定坐标
mouse_move(500, 500)
鼠标即刻移动到500, 500坐标位置
游戏内通常无法使用，多用于各类目录操作

The cursor instantly moves to the designated position.
mouse_move(500, 500)
The mouse moved instantaneously to the coordinates 500, 500.
The game may not be usable within the game session, and is mainly used for various directories.

`mouse_click()`
鼠标单击

mouse click

`mouse_left_down()`
按下鼠标左键

Press the left mouse button

`mouse_left_up()`
松开鼠标左键

Release the left mouse button

其余两个按键原理相同，使用'right'和'middle'即可

The other two keys work on the same principle as well. Use 'right' and 'middle'

`mouse_wheel()`
每120个单位代表滚轮转动一格
也可直接输入数值1
正数代表向上滚动，负数则反向滚动

Every 120 units is regarded as one rotation of the mouse wheel.
Of course, it's fine to input "1" for the time as well.
Positive numbers indicate upward scrolling, while negative numbers indicate the opposite direction.

`mouse_wheel_up()`
滚轮向上滚动一格

The roller rolls up one step.

`mouse_wheel_down()`
滚轮向下滚动一格

The roller rolls down one step.

`key_press()`
key_press(0x41)
持续按下A键

key_press(0x41)
Keep pressing the key A continuously.

`key_down(0x41)`
按下键盘A键

key_down(0x41)
Press the key A on the keyboard.

`key_up(0x41)`
松开键盘A键

key_up(0x41)
Keyboard lifted up A

`take_admin()`
获取管理员权限

take_admin()
Obtain administrative privileges.

`is_admin()`
检测程序是否具备管理员权限

is_admin()
Check whether the program has administrator privileges

`get_admin()`
检查权限，无权限则自动申请
整合权限检测与权限获取功能

get_admin()
Check if there is administrator privileges. If not, apply for them.
integrated 'is_admin' and 'take_admin'
# -----------------------------------------------
## 高级功能 AdvancedFunction
`mouse_move_smooth()`
mouse_move_smooth(100,100,2)
鼠标平滑相对移动（横坐标，纵坐标，移动耗时）
适用于游戏内操作

mouse_move_smooth(100,100,2)
Mouse smooth/relative movement (x-axis, y-axis, required time)
Used within the game session

`continuous_press()`
无需按键码即可连续点击输入
暂不支持双引号
参数text：可输入数字、字母、符号等字符
参数interval：延时参数，可选，默认0.04

continuous_press()
Supports continuous clicking without key codes  
Currently does not support "  
:param text: ------ Keyboard input "123 Abc,{/]"  
:param interval: Delay, optional; if not provided, defaults to 0.04 :return: param text

`hot_key()`
检测多键同时按下，支持1至5个按键
全部按键按下时返回'down'

hot_key()
Detects simultaneous key press actions, from a minimum of 1 to a maximum of 5 keys  
Returns 'down' when all keys are pressed 

`close_process()`
强制关闭当前窗口

close_process()
Forcefully close the current window.
# -----------------------------------------------
## 图像查找 FindTarget
`find_photo()`
find_photo('123123.png')
检索匹配图像
常用于条件判断，识别目标图像后触发后续动作

find_photo('123123.png')
Search for matching images
Used to be placed in conditional statements, triggering subsequent events upon detecting the corresponding image.
# -----------------------------------------------
## 信息获取 GetInfo
`check_mouse_left_change()`
监听鼠标左键，输出按下、松开状态

check_mouse_left_change()
Listen to the left mouse button and output "up" and "down"

`check_mouse_right_change()`
监听鼠标右键，输出按下、松开状态

check_mouse_right_change()
Listen to the right mouse button and output "up" and "down"

`check_mouse_middle_change()`
监听鼠标中键，输出按下、松开状态

check_mouse_middle_change()
Listen to the middle mouse button and output "up" and "down"

`check_wheel_change()`
监控鼠标滚轮动作，输出前进、后退、静止状态

check_wheel_change()
Monitor the mouse wheel movement and output "forward", "backward" and "stop".

`get_mouse_relative()`
监测鼠标移动，每秒检测50次

get_mouse_relative()
Monitor the movement of the mouse and detect it 50 times per second.

`check_key()`
键盘监听，可指定按键码单独监听，不传参则监听全局键盘

check_key()
Monitor the keyboard. You can pass in specific key codes, and then only detect this key. Or no parameters are passed, and the entire keyboard is detected.

`enable_fast_relative()`
开启鼠标快速移动检测
将屏幕分割为30*30像素网格，仅鼠标越过网格线才回传坐标，优化程序性能

enable_fast_relative()
Enable the quick mouse movement detection. After enabling it, the screen resolution will be obtained and divided into a 30*30 pixel grid. Only when the mouse passes through the grid lines will the movement coordinates be sent back, in order to optimize the program performance.

`disable_fast_relative()`
关闭鼠标快速移动检测
恢复数据回传频率，精度更高但会产生轻微延迟

disable_fast_relative()
Disable the quick mouse movement detection, the frequency of returning information is restored, it becomes more accurate but also more laggy.

`enable_streamline_return()`
启用精简返回模式，仅输出基础按键状态与纯坐标数值

enable_streamline_return()
Enable the streamlined return mode, and only return the most basic up/down and pure coordinate numbers.

`disable_streamline_return()`
关闭精简返回模式

disable_streamline_return()
Disable the streamlined return mode, and only return the most basic up/down and pure coordinate numbers.
# -----------------------------------------------
## 动态库注入 DllInjection
`dll_injection()`
该功能暂未生效

dll_injection()
It hasn't had any effect yet.
# -----------------------------------------------
## 操作录制 record
`start_recode()`
录制后续键鼠操作信息，并以文本文件形式保存

start_recode()
Record the subsequent output information from the mouse and keyboard and return it in the form of a text document.
# -----------------------------------------------
## 操作回放 replay
`start_replay()`
读取指定文档并回放操作

start_replay()
Replay the specified text document.





# -----------------------------------------------
    BasicsFunction


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
# -----------------------------------------------

    AdvancedFunction

`mouse_move_smooth()`

mouse_move_smooth(100,100,2)

Mouse smooth/relative movement (x-axis, y-axis, required time)

Used within the game session

`continuous_press()`



Supports continuous clicking without key codes  
Currently does not support "  
:param text: ------ Keyboard input "123 Abc,{/]"  
:param interval: Delay, optional; if not provided, defaults to 0.04 :return: param text



`hot_key()`



Detects simultaneous key press actions, from a minimum of 1 to a maximum of 5 keys  
Returns 'down' when all keys are pressed 

`close_process()`

Forcefully close the current window.

# -----------------------------------------------
    FindTarget

`find_photo()`

find_photo('123123.png')

Search for matching images

Used to be placed in conditional statements, triggering subsequent events upon detecting the corresponding image.


# -----------------------------------------------
    GetInfo

`check_mouse_left_change()`

Listen to the left mouse button and output "up" and "down"

`check_mouse_right_change()`

Listen to the right mouse button and output "up" and "down"

`check_mouse_middle_change()`

Listen to the middle mouse button and output "up" and "down"

`check_wheel_change()`

Monitor the mouse wheel movement and output "forward", "backward" and "stop".

`get_mouse_relative()`

Monitor the movement of the mouse and detect it 50 times per second.

`check_key()`

Monitor the keyboard. You can pass in specific key codes, and then only detect this key. Or no parameters are passed, and the entire keyboard is detected.

`enable_fast_relative()`

Enable the quick mouse movement detection. After enabling it, the screen resolution will be obtained and divided into a 30*30 pixel grid. Only when the mouse passes through the grid lines will the movement coordinates be sent back, in order to optimize the program performance.

`disable_fast_relative()`

Disable the quick mouse movement detection, the frequency of returning information is restored, it becomes more accurate but also more laggy.

`enable_streamline_return()`

Enable the streamlined return mode, and only return the most basic up/down and pure coordinate numbers.

`disable_streamline_return()`

Disable the streamlined return mode, and only return the most basic up/down and pure coordinate numbers.


# -----------------------------------------------
    DllInjection

`dll_injection()`

It hasn't had any effect yet.
# -----------------------------------------------
    record

`start_recode()`

Record the subsequent output information from the mouse and keyboard and return it in the form of a text document.
# -----------------------------------------------
    replay

`start_replay()`

Replay the specified text document.
