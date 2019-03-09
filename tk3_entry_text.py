#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'AJay'
__mtime__ = '2019/3/9 0009'

"""

import tkinter


window =tkinter.Tk()          # 创建整个框架
window.title('tk3_entry_text')
window.geometry('200x200')

e=tkinter.Entry(window)        #创建一个输入框
# e=tkinter.Entry(window,show='*')
e.pack()

def insert_point():
    var=e.get()
    t.insert('insert',var)
def insert_end():
    var=e.get()
    t.insert('end',var)
    t.insert(2.2,var)

b1=tkinter.Button(window,text='点插',width=15,height=2,command=insert_point)# 创建一个点插的按钮
b1.pack()

b2=tkinter.Button(window,text='尾插',width=15,height=2,command=insert_end)# 创建一个尾插的按钮
b2.pack()
t=tkinter.Text(window,height=2) # 创建一个text面板
t.pack()

window.mainloop()