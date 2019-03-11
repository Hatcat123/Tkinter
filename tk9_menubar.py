#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'AJay'
__mtime__ = '2019/3/11 0011'

"""

import tkinter

window = tkinter.Tk()
window.title('tk9_menubar')
window.geometry('400x400')

l = tkinter.Label(window, text='', bg='green')
l.pack()
init_num = 1


def add_num():
    global init_num
    l.config(text='num add is {}'.format(str(init_num)))
    init_num += 1


menubar = tkinter.Menu(window)

filemenu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label='文件', menu=filemenu)
filemenu.add_command(label='新文件', command=add_num)
filemenu.add_command(label='打开', command=add_num)
filemenu.add_command(label='保存', command=add_num)
filemenu.add_separator()
filemenu.add_command(label='退出', command=add_num)

editmemu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label='编辑', menu=editmemu)
editmemu.add_command(label='剪切', command=add_num)
editmemu.add_command(label='复制', command=add_num)
editmemu.add_command(label='粘贴', command=add_num)
editmemu.add_command(label='全选', command=add_num)

submenu = tkinter.Menu(menubar, tearoff=0)
editmemu.add_cascade(label='导入', menu=submenu, underline=0)
submenu.add_command(label='按钮1', command=add_num)
submenu.add_command(label='按钮2', command=add_num)
submenu.add_command(label='按钮3', command=add_num)

selecmenu = tkinter.Menu(menubar, tearoff=0)
submenu.add_cascade(label='选择', menu=selecmenu)
selecmenu.add_command(label='选择1', command=add_num)
selecmenu.add_command(label='选择2', command=add_num)
selecmenu.add_command(label='选择3', command=add_num)

window.config(menu=menubar)

window.mainloop()
