import tkinter as tk
cellphone=tk.Tk()
cellphone.title('手機設定管理系統')

label=tk.Label(cellphone,text='手機設定功能',font=('微軟正黑體',20),fg="#161757")
label.pack()

open_message=tk.StringVar()
turn=tk.IntVar()

def on():
    if turn.get()==1:
        open_message.set('開啟通知')
    else:
        open_message.set('關閉通知')

enable=tk.StringVar()
message1=tk.IntVar()

def dark():
    if message1.get()==1:
        enable.set('啟用深色模式')
    else:
        enable.set('深色模式關閉')

voluntary=tk.IntVar()
copy=tk.StringVar()

def photo():
    if voluntary.get()==1:
        copy.set('自動備份照片功能模式開啟')
    else:
        copy.set('自動備份照片功能模式關閉')

location=tk.StringVar()
function=tk.IntVar()

def position():
    if function.get()==1:
        location.set('開啟定位功能')
    else:
        location.set('關閉定位功能')

advice=tk.Checkbutton(cellphone,text='開啟通知',variable=turn,command=on)
advice.pack()

model=tk.Checkbutton(cellphone,text='深色模式開啟',variable=message1,command=dark)
model.pack()

picture=tk.Checkbutton(cellphone,text='備份照片',variable=voluntary,command=photo)
picture.pack()

unfold=tk.Checkbutton(cellphone,text='開啟定位功能',variable=function,command=position)
unfold.pack()

label2=tk.Label(cellphone,textvariable=open_message)
label2.pack()

label3=tk.Label(cellphone,textvariable=enable)
label3.pack()

label4=tk.Label(cellphone,textvariable=copy)
label4.pack()

label5=tk.Label(cellphone,textvariable=location)
label5.pack()

cellphone.mainloop()