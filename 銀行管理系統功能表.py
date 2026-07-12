'''銀行管理系統功能表'''
import tkinter as tk
from tkinter import messagebox
bank=tk.Tk()
bank.title('銀行管理系統功能表')

menu=tk.Menu(bank)
bank.config(menu=menu)

account=tk.Menu(menu,tearoff=0)
menu.add_cascade(label='帳戶管理',menu=account)

cost=tk.IntVar()

def pay():
    if cost.get():
        messagebox.showinfo('銀行餘額系統','顯示目前帳戶餘額')
    else:
        messagebox.showinfo('銀行餘額系統','關閉目前帳戶餘額')

account.add_checkbutton(label='查看餘額',command=pay,variable=cost)

store=tk.IntVar()

def keep():
    if store.get():
        messagebox.showinfo('帳戶存款','存款成功')
    else:
        messagebox.showinfo('帳戶存款','存款失敗')

account.add_checkbutton(label='存款',command=keep,variable=store)

carry=tk.IntVar()

def mention():
    if carry.get():
        messagebox.showinfo('帳戶提款','提款成功')
    else:
        messagebox.showinfo('帳戶提款','提款失敗')

account.add_checkbutton(label='提款',command=mention,variable=carry)

service=tk.Menu(menu,tearoff=0)
menu.add_cascade(label='服務功能',menu=service)

transfer=tk.IntVar()

def change():
    if transfer.get():
        messagebox.showinfo('客戶服務功能','轉帳成功')
    else:
        messagebox.showinfo('客戶服務功能','取消轉帳')

service.add_checkbutton(label='轉帳',command=change,variable=transfer)

pay_f=tk.IntVar()

def frees():
    if pay_f.get():
        messagebox.showinfo('銀行付款系統','繳費成功')
    else:
        messagebox.showinfo('銀行付款系統','繳費失敗')

service.add_checkbutton(label='繳費',command=frees,variable=pay_f)

trade=tk.IntVar()

def business():
    if trade.get():
        messagebox.showinfo('交易系統','顯示本月的交易紀錄')
    else:
        messagebox.showinfo('交易系統','關閉本月的交易紀錄')

service.add_checkbutton(label='交易紀錄',command=business,variable=trade)

system=tk.Menu(menu,tearoff=0)
menu.add_cascade(label='系統',menu=system)

code=tk.IntVar()

def modify():
    if code.get():
        messagebox.showinfo('帳戶設定系統','修改密碼成功')
    else:
        messagebox.showinfo('帳戶設定系統','修改密碼失敗')

system.add_checkbutton(label='修改密碼',command=modify,variable=code)

about=tk.IntVar()

def information():
    if about.get():
        messagebox.showinfo('系統設定','關於系統')
    else:
        messagebox.showinfo('系統設定','關閉系統設定')

system.add_checkbutton(label='關於系統',command=information,variable=about)

depart=tk.IntVar()

def leave():
    if depart.get():
        messagebox.showinfo('系統','離開系統')
    else:
        messagebox.showinfo('系統','關閉系統')

system.add_checkbutton(label='離開',command=leave,variable=depart)

bank.mainloop()