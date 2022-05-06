import re
import tkinter
import tkinter.messagebox
from tkinter import *
root = tkinter.Tk()
# 设置窗口大小和位置
root.geometry('600x590+100+100')
# 不允许改变窗口大小
# root.resizable(False, False)
# 设置窗口标题
root.title('简易计算器-深圳技术大学')

# 放置用来显示信息的文本框，并设置为只读
contentVar = tkinter.StringVar(root, '')
contentEntry = tkinter.Entry(root, textvariable=contentVar,bd=2,font = "Helvetica 44 bold", justify=RIGHT)
contentEntry['state'] = 'readonly'
contentEntry.place(x=0, y=0, width=600, height=100)

frame = tkinter.Frame(root, width=400, height=300)


# 按钮通用代码
def buttonClick(btn):    
    content = contentVar.get()
    # 如果已有内容是以小数点开头的，前面加0
    if content.startswith('.'):
        content = '0' + content

    # 根据不同按钮做出相应的处理
    if btn in '0123456789':
        content += btn
    elif btn == '.':
        lastPart = re.split(r'\+|-|\*|/]', content)[-1]
        if '.' in lastPart:
            tkinter.messagebox.showerror('错误', '小数点太多了')
            return
        else:
            content += btn
    elif btn == 'C':
        content = ''
    elif btn == '=':        
        try:
            # 对输入的表达式求值
            content = str(eval(content))
        except:
            tkinter.messagebox.showerror('错误', '表达式错误')
            return
    elif btn in operators:
        if content.endswith(operators):
            tkinter.messagebox.showerror('错误', '不允许存在连续运算符')
            return
        content += btn
    elif btn == 'S':
        n = content.split('.')
        if all(map(lambda x: x.isdigit(), n)):
            content = eval(content) ** 0.5
        else:
            tkinter.messagebox.showerror('错误', '表达式错误')
            return
            
    contentVar.set(content)

# 放置清除按钮和等号按钮
Wbtn=20
Hbtn=5
btnClear = tkinter.Button(frame, text='Clear', height=Hbtn,width=Wbtn,bd=0,command=lambda:buttonClick('C'))
btnClear.grid(row=0,column=0)
btnCompute = tkinter.Button(frame, text='=', height=Hbtn,width=Wbtn,bd=0, command=lambda:buttonClick('='))
btnCompute.grid(row=0,column=1)
btnPow = tkinter.Button(frame, text='**', height=Hbtn,width=Wbtn, bd=0,command=lambda:buttonClick('**'))
btnPow.grid(row=0,column=2)
btnDiv = tkinter.Button(frame, text='//', height=Hbtn,width=Wbtn, bd=0,command=lambda:buttonClick('//'))
btnDiv.grid(row=0,column=3)
# 放置10个数字、小数点和计算平方根的按钮
digits = list('012+345-678*9./S')
index = 0
for row in range(4):
    for col in range(4):
        d = digits[index]
        index += 1
        btnDigit = tkinter.Button(frame, text=d, height=Hbtn,width=Wbtn,bd=0,command=lambda x=d:buttonClick(x))
        btnDigit.grid(row=row+1, column=col)

frame.place(x=0, y=100)
# # 放置运算符按钮
operators = ('+', '-', '*', '/', '**', '//')
# for index, operator in enumerate(operators):
#     btnOperator = tkinter.Button(frame, text=operator, command=lambda x=operator:buttonClick(x))
#     btnOperator.place(x=230, y=80+index*30, width=50, height=20)

root.mainloop()
