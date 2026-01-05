import tkinter
from tkinter import *

window = tkinter.Tk()
window.title('Calculator   --zhr0913')  # Window标题
window.geometry('400x500')  # Window长宽
window.resizable(False, False)  # 设置窗口不可拉伸
window.iconbitmap("./Calculator.ico")  # 设置图标
"""
Main_menu = Menu(window)  # 创建主菜单
Theme_menu = Menu(Main_menu, tearoff=False)  # 创建主题菜单
Main_menu.add_cascade(label='主题', menu=Theme_menu)  # 将主题菜单添加到主菜单上并命名
"""
result = tkinter.StringVar()
button_frame = tkinter.Frame()
result.set('0')  # 默认显示为0
screen = tkinter.Label(window, textvariable=result, font=('Arial', 20), bg='green', borderwidth=2)  # 创建计算器显示屏幕标签


def generate_Button(text, row, col):  # 创建按钮并放置在相应行和列
    button = tkinter.Button(button_frame, text=text, padx=20, pady=20,
                            font=('Arial', 18), command=lambda: ButtonHit(text))
    button.grid(row=row, column=col, sticky='nsew')
    button_frame.rowconfigure(row, weight=1)
    button_frame.columnconfigure(col, weight=1)


generate_Button('0', 4, 0)
generate_Button('1', 3, 0)
generate_Button('2', 3, 1)
generate_Button('3', 3, 2)
generate_Button('4', 2, 0)
generate_Button('5', 2, 1)
generate_Button('6', 2, 2)
generate_Button('7', 1, 0)
generate_Button('8', 1, 1)
generate_Button('9', 1, 2)
generate_Button('.', 4, 1)
generate_Button('=', 4, 2)
generate_Button('/', 1, 3)
generate_Button('*', 2, 3)
generate_Button('-', 3, 3)
generate_Button('+', 4, 3)
button = tkinter.Button(button_frame, text='C', padx=20, pady=20, font=('Arial', 18),
                        fg='red', command=lambda: ButtonHit('C'))
button.grid(row=0, column=0, columnspan=4, sticky='nsew')


def KeyBoardEvent(event):  # 按键事件
    key = event.keysym
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(len(numbers)):
        if key == numbers[i]:
            ButtonHit(numbers[i])
    if key == 'plus':
        ButtonHit('+')
    elif key == 'minus':
        ButtonHit('-')
    elif key == 'asterisk':
        ButtonHit('*')
    elif key == 'slash':
        ButtonHit('/')
    elif key == 'Return':
        ButtonHit('=')
    elif key == 'BackSpace':
        ButtonHit('delete')
    elif key == 'equal':
        ButtonHit('=')
    elif key == 'period':
        ButtonHit('.')
    # print(key) # Debug


def ButtonHit(num):  # 按钮检测事件
    if num == '=':
        try:
            expression = result.get()
            temp = eval(expression)
            result.set(temp)
        except Exception:
            result.set('Error!')
    elif num == 'C':
        result.set('0')
    elif num == 'delete':
        current_text = result.get()
        new_text = current_text[:-1]
        result.set(new_text)
    else:
        if result.get() == '0' and num != '.':
            result.set('')
        current_text = result.get()
        new_text = current_text + str(num)
        result.set(new_text)


# window.config(menu=Main_menu)  # 将主菜单设置在窗口上
button_frame.bind('<Key>', KeyBoardEvent)  # 将键盘事件与按钮框架绑定
button_frame.focus_set()
screen.pack(side=tkinter.TOP, fill=tkinter.X, ipadx=10, ipady=40)  # 放置屏幕
button_frame.pack(fill=tkinter.BOTH, side='bottom')  # 放置按钮框架

window.mainloop()  # window循环显示
