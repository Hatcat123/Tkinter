#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'AJay'
__mtime__ = '2019/3/9 0009'

"""

import tkinter

# Example (Hello, World):
# import tkinter
# from tkinter.constants import *
# tk = tkinter.Tk()
# frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
# frame.pack(fill=BOTH,expand=1)
# label = tkinter.Label(frame, text="Hello, World")
# label.pack(fill=X, expand=1)
# button = tkinter.Button(frame,text="Exit",command=tk.destroy)
# button.pack(side=BOTTOM)
# tk.mainloop()

import tkinter

window = tkinter.Tk()
window.title('tk_Label_Button')
window.geometry('200x100')

var = tkinter.StringVar()
l = tkinter.Label(window, textvariable=var, bg='green', width='15', height='2')
l.pack()

on_hit = False


def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('你点击了我')
    else:
        on_hit = False
        var.set('')


b = tkinter.Button(window, text='按钮', width=15, height=2, command=hit_me)
b.pack()
window.mainloop()
