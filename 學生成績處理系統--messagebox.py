'''學生成績處理系統'''
import tkinter as tk
from tkinter import messagebox

file=tk.Tk()
file.title('學生成績處理系統')

name='Ming'
score=58

def score_system():
    if score<0 or score>100:
        result=messagebox.showerror('成績處理系統','成績輸入錯誤')

    elif score>=60:
        result=messagebox.showinfo('成績處理系統','Ming: 及格')

    else:
        result=messagebox.askyesnocancel('成績處理系統','Ming: 不及格, 是否參加補考 ?')

        if result is True:
                messagebox.showinfo('成績處理系統','已參加補考')
        elif result is False:
                messagebox.showinfo('成績處理系統','不參加補考')
        else:
                messagebox.showinfo('成績處理系統','稍後再決定')


button=tk.Button(file,text='成績處理系統',command=score_system)
button.pack()

file.mainloop()