'''會員加分系統'''
import tkinter as tk
promptly=tk.Tk()
promptly.title('會員加分系統')#設置標題
var=tk.IntVar()

chb=tk.Checkbutton(promptly,bg="#E8F534",variable=var,offvalue=0,onvalue=50)#設置為有勾選可加50分,沒勾選為0分
chb.pack()

def score():
    print('目前分數:',var.get())#取得目前的分數

button=tk.Button(promptly,text='計算加分',command=score)
button.pack()
promptly.mainloop()