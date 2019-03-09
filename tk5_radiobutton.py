#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'AJay'
__mtime__ = '2019/3/9 0009'

"""
import tkinter

window = tkinter.Tk()
window.title('tk5_radiobutton')
window.geometry('400x400')

var=tkinter.StringVar()
l=tkinter.Label(window,bg='green',width=20,text='空')
l.pack()

def print_select():
    l.config(text='你选择的是'+var.get())

r1=tkinter.Radiobutton(window,text='选项1',variable=var,value='1',command=print_select)
r2=tkinter.Radiobutton(window,text='选项2',variable=var,value='2',command=print_select)
r3=tkinter.Radiobutton(window,text='选项3',variable=var,value='3',command=print_select)
r1.pack()
r2.pack()
r3.pack()





window.mainloop()
