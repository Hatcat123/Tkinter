#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'AJay'
__mtime__ = '2019/3/11 0011'

"""
import tkinter
import tkinter.messagebox

window = tkinter.Tk()
window.title('tk11_msgbox')
window.geometry('400x400')

def msg_showinfo():
    tkinter.messagebox.showinfo(title='信息',message='word')
def msg_showwarning():
    tkinter.messagebox.showwarning(title='警告',message='word')
def msg_showerror():
    tkinter.messagebox.showerror(title='hello',message='word')
def msg_askquestion():
    msg = tkinter.messagebox.askquestion(title='hello',message='word')
    print(msg)
def msg_askyesno():
    msg  = tkinter.messagebox.askyesno(title='删除',message='是否删除')
    print(msg)
def msg_askretrycancel():
    msg  = tkinter.messagebox.askretrycancel(title='重试',message='内存出现问题，请重试')
    print(msg)
    while msg is True:
        msg =tkinter.messagebox.askretrycancel(title='重试', message='内存出现问题，请重试')
        print(msg)
def msg_askokcancel():
    msg = tkinter.messagebox.askokcancel(title='hello',message='word')
    print(msg)
def msg_askyesnocancel():
    msg = tkinter.messagebox.askyesnocancel(title='hello',message='word')
    print(msg)
tkinter.Button(window,text='信息',command=msg_showinfo).pack()
tkinter.Button(window,text='警告',command=msg_showwarning).pack()
tkinter.Button(window,text='错误',command=msg_showerror).pack()
tkinter.Button(window,text='问题',command=msg_askquestion).pack()
tkinter.Button(window,text='删除',command=msg_askyesno).pack()
tkinter.Button(window,text='重试',command=msg_askretrycancel).pack()
tkinter.Button(window,text='askokcancel',command=msg_askokcancel).pack()
tkinter.Button(window,text='askyesnocancel',command=msg_askyesnocancel).pack()




window.mainloop()
