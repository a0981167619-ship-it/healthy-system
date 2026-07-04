'''範例'''
import tkinter as tk
from tkinter import messagebox
choice=tk.Tk()
choice.title('單選按鈕元件')#設置標題

var=tk.StringVar()#核取文字

work1=tk.Radiobutton(choice,text='工程師',value='工程師',variable=var)
work1.pack()

work2=tk.Radiobutton(choice,text='老師',value='老師',variable=var)     #建立選擇,使用者只能在三者當中選一個
work2.pack()

work3=tk.Radiobutton(choice,text='建築師',value='建築師',variable=var)
work3.pack()

def choice_career():
    work=var.get()
    if work=='':
        messagebox.showwarning('warning','請選擇一個職業')
    else:
        print('你的選擇是:',work)

button=tk.Button(choice,text='職業選擇',command=choice_career)
button.pack()
choice.mainloop()

