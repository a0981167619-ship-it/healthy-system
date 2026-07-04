'''範例'''
import tkinter as tk
publicity=tk.Tk()

var=tk.IntVar()

tv=tk.StringVar()

def upon():
    if var.get()==1:#如果使用者已勾選
        tv.set('已勾選')
    else:
        tv.set('未勾選')

check=tk.Checkbutton(publicity,variable=var,text='贊成',command=upon)
check.pack()

label=tk.Label(publicity,textvariable=tv)
label.pack()

publicity.mainloop()
