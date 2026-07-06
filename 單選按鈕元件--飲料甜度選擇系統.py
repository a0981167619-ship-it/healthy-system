'''飲料甜度選擇系統'''
import tkinter as tk
from tkinter import messagebox #匯入messagebox

drinks=tk.Tk()
drinks.title('飲料甜度選擇系統')#設置標題
var=tk.StringVar()

sugar1=tk.Radiobutton(drinks,text='無糖',value='無糖',variable=var)
sugar1.pack()

sugar2=tk.Radiobutton(drinks,text='微糖',value='微糖',variable=var)
sugar2.pack()                                                               #建立選擇

sugar3=tk.Radiobutton(drinks,value='半糖',text='半糖',variable=var)
sugar3.pack()

sugar4=tk.Radiobutton(drinks,text='全糖',value='全糖',variable=var)
sugar4.pack()

def drink():
    sugar=var.get()

    if sugar=='':
        messagebox.showwarning('Warning','請選擇一個糖度')
    else:
        messagebox.showinfo('飲料糖度',sugar)
button=tk.Button(drinks,text='選擇飲料糖度',command=drink)#建立按鈕
button.pack()

drinks.mainloop()

