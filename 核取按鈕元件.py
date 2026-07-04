'''範例'''
import tkinter as tk
prominent=tk.Tk()
prominent.title('Checkbutton')

var=tk.IntVar()

check=tk.Checkbutton(prominent,text='分數',variable=var,onvalue=100,offvalue=0)
check.pack()

def check_open():
    print(var.get())

button=tk.Button(prominent,text='查看成績',command=check_open)
button.pack()

prominent.mainloop()