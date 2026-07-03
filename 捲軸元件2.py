'''閱讀器'''
import tkinter as tk
obtain=tk.Tk()
obtain.title('閱讀器')#設定標題
obtain.geometry('400x250')#設定視窗元件大小

scrollbar=tk.Scrollbar(obtain)
Text=tk.Text(obtain,yscrollcommand=scrollbar.set)   #兩者互相連接
scrollbar.config(command=Text.yview)

scrollbar.pack(side='right',fill='y')
Text.pack(expand=True,fill='y',side='left')

def button():
    for i in range(10):
      Text.insert(tk.END,'reading is a good hobby, can broaden you horizons')  

button=tk.Button(obtain,command=button,text='載入文章')
button.pack()
obtain.mainloop()