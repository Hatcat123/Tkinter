#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'AJay'
__mtime__ = '2019/3/11 0011'

"""
import tkinter

window = tkinter.Tk()
window.title('tk12_position')
window.geometry('400x400')

for i in range(4):
    for j in range(3):
        tkinter.Label(window, text=1).grid(row=i, column=j, pady=10)

tkinter.Label(window, text=1).place(x=220, y=20, anchor='nw')

window.mainloop()
