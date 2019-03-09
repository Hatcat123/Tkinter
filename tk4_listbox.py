#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'AJay'
__mtime__ = '2019/3/9 0009'

"""
import tkinter


window=tkinter.Tk()
window.title('tk4_listbox')
window.geometry('400x400')

var1 = tkinter.StringVar()
l=tkinter.Label(window,bg='yellow',width=4,textvariable=var1)
l.pack()

def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)
b=tkinter.Button(window,text='打印',width=5,height=1,command=print_selection)
b.pack()

var2 =tkinter.StringVar()
var2.set((11, 22, 33, 44))  # 传入var2一个元组

lb=tkinter.Listbox(window,listvariable=var2)
list_items =[1,2,3,4]
for item in list_items:
    lb.insert('end',item)

lb.insert(1,'开始')# 在第一个后面插入
lb.insert(2,'第二个')# 在第二个后面插入
# lb.delete(2)  # 删除第二个
lb.pack()

window.mainloop()

