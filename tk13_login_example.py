#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'AJay'
__mtime__ = '2019/3/11 0011'

"""
import tkinter as tk

window = tk.Tk()
window.title('某某登录注册页面')
window.geometry('450x300')

# 画布
canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file='welcome.png')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')

# 用户信息
tk.Label(window, text='邮箱').place(x=60, y=150)
tk.Label(window, text='密码').place(x=60, y=190)

var_user_email = tk.StringVar()
entry_user_email = tk.Entry(window, textvariable=var_user_email)
entry_user_email.place(x=160, y=150)
var_user_password = tk.StringVar()
entry_user_password = tk.Entry(window, textvariable=var_user_password, show='*')
entry_user_password.place(x=160, y=190)


def user_login():
    pass


def user_sign_up():
    pass


# 登录注册按钮
btn_login = tk.Button(window, text='登录', command=user_login)
btn_login.place(x=170, y=230)
btn_sign_up = tk.Button(window, text='注册', command=user_sign_up)
btn_sign_up.place(x=270, y=230)

window.mainloop()
