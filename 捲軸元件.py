import tkinter as tk
'''範例'''
mystery=tk.Tk()
mystery.title('捲軸元件')#設定標題
mystery.geometry('300x200')#設定視窗大小

scroll=tk.Scrollbar(mystery)
text=tk.Text(mystery,yscrollcommand=scroll.set)#跟Scrollbar連接
scroll.config(command=text.yview)#跟text連接

text.pack(side='right',expand=True,fill='y')#位置在右邊,左右分散對齊
scroll.pack(side='left',fill='y')#垂直捲軸

for i in range(100):
    text.insert(tk.END,'123456*********************\n')

mystery.mainloop()

