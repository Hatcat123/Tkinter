#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'AJay'
__mtime__ = '2019/3/9 0009'

"""
import tkinter

window = tkinter.Tk()
window.title('tk7_checkButton')
window.geometry('400x400')

l = tkinter.Label(window, bg='yellow', width=20, text='空')
l.pack()


def check_select():
    if var1.get() == 1 and var2.get() == 1:
        l.config(text='我都喜欢')
    elif var1.get() == 1 and var2.get() == 0:
        l.config(text='我喜欢Python')
    elif var1.get() == 0 and var2.get() == 1:
        l.config(text='我喜欢C++')
    else:
        l.config(text='我都不喜欢')


var1 = tkinter.IntVar()
var2 = tkinter.IntVar()
c1 = tkinter.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0, command=check_select)
c2 = tkinter.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0, command=check_select)
c1.pack()
c2.pack()

window.mainloop()
