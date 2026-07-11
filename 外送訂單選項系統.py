'''外送訂單選項系統'''
import tkinter as tk
deliver=tk.Tk()
deliver.title('外送訂單選項系統')

label=tk.Label(deliver,text='外送訂單選項系統',font=('標楷體',25))
label.pack()

var=tk.IntVar()
var1=tk.StringVar()

def certain():
    if var.get()==1:#使用者有勾選
        var1.set('加辣、加蛋、加起司、加大份量')
    else:
        var1.set('都不加')

check=tk.Checkbutton(deliver,text='加辣',font=('微軟正黑體',12),variable=var,command=certain)
check.pack()

push=tk.Checkbutton(deliver,text='加蛋',font=('微軟正黑體',12),variable=var,command=certain)
push.pack()

note=tk.Checkbutton(deliver,text='加起司',font=('微軟正黑體',12),variable=var,command=certain)
note.pack()

press=tk.Checkbutton(deliver,text='加大份量',font=('微軟正黑體',12),variable=var,command=certain)
press.pack()

label=tk.Label(deliver,textvariable=var1)
label.pack()
deliver.mainloop()
    