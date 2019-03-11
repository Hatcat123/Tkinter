#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'AJay'
__mtime__ = '2019/3/11 0011'

"""
import tkinter

window = tkinter.Tk()
window.title('tk10 frame')
window.geometry('400x400')

tkinter.Label(window,text='在主窗口上').pack()

frm = tkinter.Frame(window)
frm.pack()
frm_l=tkinter.Frame(frm)
frm_r = tkinter.Frame(frm)

frm_l.pack(side='left')
frm_r.pack(side='right')

tkinter.Label(frm_l,text='在左窗口上1').pack()
tkinter.Label(frm_l,text='在左窗口上2').pack()
tkinter.Label(frm_l,text='在左窗口上3').pack()
tkinter.Label(frm_r,text='在右边窗口上').pack()

window.mainloop()
