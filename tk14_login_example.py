#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'AJay'
__mtime__ = '2019/3/11 0011'

"""
import requests
import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title('某某登录注册页面')
window.geometry('450x300')

# 画布
canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')

# 用户信息
tk.Label(window, text='邮箱').place(x=60, y=150)
tk.Label(window, text='密码').place(x=60, y=190)

# 输入框
var_user_email = tk.StringVar()
entry_user_email = tk.Entry(window, textvariable=var_user_email)
entry_user_email.place(x=160, y=150)
var_user_password = tk.StringVar()
entry_user_password = tk.Entry(window, textvariable=var_user_password, show='*')
entry_user_password.place(x=160, y=190)


def user_login():
    user_email = var_user_email.get()
    user_pwd = var_user_password.get()
    json={
        "user_email":user_email,
        "user_pwd":user_pwd,
    }
    try:
        req = requests.post(url='http://127.0.0.1:5000/login/',json=json)
        print(req.json())
        if req.json().get('stats')==201:
            pass
        else:
            is_sign_up = tk.messagebox.askyesno(title='欢迎',message='你还没有注册，是否进行注册？')
            if is_sign_up:
                user_sign_up()
    except Exception as e:
        ask = tk.messagebox.askretrycancel(title='网络错误',message='请检查你的网络')
        if ask:
            user_login()



def user_sign_up():
    pass


# 登录注册按钮
btn_login = tk.Button(window, text='登录', command=user_login)
btn_login.place(x=170, y=230)
btn_sign_up = tk.Button(window, text='注册', command=user_sign_up)
btn_sign_up.place(x=270, y=230)

window.mainloop()
