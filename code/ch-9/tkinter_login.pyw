import tkinter
import tkinter.messagebox
import os
import os.path

path = os.getenv('temp')
filename = os.path.join(path, 'info.txt')

# 创建应用程序窗口
root = tkinter.Tk()

#定义窗口大小
root['height'] = 140
root['width'] = 200

# 在窗口上创建标签组件
labelName = tkinter.Label(root,
                          text='User Name:',
                          justify=tkinter.RIGHT,
                          anchor = 'e',
                          width=80)
labelName.place(x=10, y=5, width=80, height=20)

# 创建字符串变量和文本框组件，同时设置关联的变量
varName = tkinter.StringVar(root, value='')
entryName = tkinter.Entry(root,
                          width=80,
                          textvariable=varName)
entryName.place(x=100, y=5, width=80, height=20)

labelPwd = tkinter.Label(root,
                         text='User Pwd:',
                         justify=tkinter.RIGHT,
                         anchor = 'e',
                         width=80)
labelPwd.place(x=10, y=30, width=80, height=20)

# 创建密码文本框
varPwd = tkinter.StringVar(root, value='')
entryPwd = tkinter.Entry(root,
                         show='*',
                         width=80,
                         textvariable=varPwd)
entryPwd.place(x=100, y=30, width=80, height=20)

# 尝试自动填写用户名和密码
try:
    with open(filename) as fp:
        n, p = fp.read().strip().split(',')
        varName.set(n)
        varPwd.set(p)
except:
    pass

# 记住我，复选框
rememberMe = tkinter.IntVar(root, value=1)
# 选中时变量值为1，未选中时变量值为0，默认选中
checkRemember = tkinter.Checkbutton(root,
                                    text='Remember me?',
                                    variable=rememberMe,
                                    onvalue=1, offvalue=0)
checkRemember.place(x=30, y=70, width=120, height=20)

# 登录按钮事件处理函数
def login():
    # 获取用户名和密码
    name = entryName.get()
    pwd = entryPwd.get()
    if name=='admin' and pwd=='123456':
        tkinter.messagebox.showinfo(title='恭喜',
                                    message='登录成功！')
        if rememberMe.get() == 1:
            # 把登录成功的信息写入临时文件        
            with open(filename, 'w') as fp:
                fp.write(','.join((name,pwd)))
        else:
            try:
                os.remove(filename)
            except:
                pass
    else:
        tkinter.messagebox.showerror('警告',
                                     message='用户名或密码错误')
# 创建按钮组件，同时设置按钮事件处理函数
buttonOk = tkinter.Button(root,
                          text='Login',
                          activeforeground='#ff0000',# 按下按钮时文字颜色
                          command=login)
buttonOk.place(x=30, y=100, width=50, height=20)

# 取消按钮的事件处理函数
def cancel():
    #清空用户输入的用户名和密码
    varName.set('')
    varPwd.set('')
buttonCancel = tkinter.Button(root,
                              text='Cancel',
                              command=cancel)
buttonCancel.place(x=90, y=100, width=50, height=20)

#启动消息循环
root.mainloop()
