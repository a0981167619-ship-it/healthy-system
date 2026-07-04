'''檔案開啟確認系統'''
import tkinter as tk
from tkinter import messagebox

angle=tk.Tk()
angle.title('檔案開啟確認系統')

file_name='C++.pdb'

def open_file():
    outcome=messagebox.askyesnocancel('檔案開啟詢問','是否開啟 C++.pdb ?')

    if outcome is True:
        messagebox.showinfo('檔案開啟詢問','正在開啟檔案')
    
    elif outcome is False:
        messagebox.showwarning('檔案開啟詢問','已取消開啟')

    else:
        messagebox.showinfo('檔案開啟詢問','返回上一頁')


Button=tk.Button(angle,text='檔案開啟',command=open_file)
Button.pack()

angle.mainloop()