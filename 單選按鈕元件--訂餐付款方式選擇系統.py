'''訂餐付款方式的選擇系統'''
import tkinter as tk
from tkinter import messagebox
rank=tk.Tk()

rank.title('訂餐付款方式選擇系統')

var=tk.StringVar()#核取文字

price=120

pay1=tk.Radiobutton(font=('新細明體',14),text='現金',value='現金',variable=var)
pay1.pack()

pay2=tk.Radiobutton(font=('新細明體',14),text='信用卡',value='信用卡',variable=var)
pay2.pack()

pay3=tk.Radiobutton(font=('新細明體',14),text='LINE Pay',value='LINE Pay',variable=var)
pay3.pack()

def pay_for():
    pay=var.get()
    if pay=='':
        messagebox.showwarning('warning','請選擇付款方式')
    else:
        messagebox.showinfo('付款方式確認',pay)
        messagebox.showinfo('價格:',price)
      
button=tk.Button(rank,text='確認付款',command=pay_for)
button.pack()

rank.mainloop()