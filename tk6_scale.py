#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'AJay'
__mtime__ = '2019/3/9 0009'

"""

import tkinter

window = tkinter.Tk()
window.title('tk6_scale')
window.geometry('400x400')

l=tkinter.Label(window,bg='yellow',width=20,text='empty')
l.pack()

def print_select(v):
    l.config(text='移动到'+v)
s=tkinter.Scale(window,label='移动',from_=5,to=100,orient=tkinter.HORIZONTAL,
                length=200,showvalue=0,tickinterval=40,resolution=0.01,command=print_select)
s.pack()

window.mainloop()
