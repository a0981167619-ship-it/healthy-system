'''文字編輯器顯示設定系統'''
import tkinter as tk
from tkinter import messagebox

edit=tk.Tk()
edit.title('文字編輯器顯示設定系統')#設置標題
menu=tk.Menu(edit)
edit.config(menu=menu)

set=tk.Menu(menu,tearoff=0)#把分隔線拿除
menu.add_cascade(label='設定',menu=set)#新增主功能表的項目

define=tk.IntVar()
define1=tk.IntVar()  #因為三個函式不能共用一個Var
define2=tk.IntVar()


def tool():#工具列
    if define.get()==1:#沒勾為0,有勾為1
        messagebox.showinfo('工具列','顯示工具列已開啟')
    else:
        messagebox.showinfo('工具列','顯示工具列未開啟')

set.add_checkbutton(label='顯示工具列',variable=define,command=tool)

def c_line():#自動換行模式
    if define1.get()==1:
        messagebox.showinfo('自動換行','自動換行已開啟')
    else:
        messagebox.showinfo('自動換行','自動換行已關閉')

set.add_checkbutton(label='自動換行',variable=define1,command=c_line)

def dark():#深色模式
    if define2.get()==1:
        messagebox.showinfo('深色模式','深色模式已開啟')
    else:
        messagebox.showinfo('深色模式','深色模式已關閉')

set.add_checkbutton(label='深色模式',variable=define2,command=dark)
edit.mainloop()