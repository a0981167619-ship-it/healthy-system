'''留言板-捲軸元件'''
import tkinter as tk
obtain=tk.Tk()
obtain.title('留言板')#設置標題名稱為留言板
obtain.geometry('300x200')#設置視窗大小
scroll=tk.Scrollbar(obtain)
text=tk.Text(obtain,yscrollcommand=scroll.set)
scroll.config(command=text.yview)                 #兩者互相連接

scroll.pack(side='left',fill='y')
text.pack(side='right',fill='y',expand=True)

for i in range(100):
    text.insert(tk.END,'school 、teacher 、student、math、graduation、english、science')

obtain.mainloop()