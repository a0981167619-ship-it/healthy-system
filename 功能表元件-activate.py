'''activate--範例'''
import tkinter as tk
active=tk.Tk()
active.title('activate')
menu=tk.Menu(active)

active.config(menu=menu)

work_menu=tk.Menu(menu,tearoff=0)
menu.add_cascade(label='工作',menu=work_menu)#新增主功能表元件
work_menu.add_command(label='職業')#index=0
work_menu.add_command(label='工作內容')#index=1                    新增次功能表元件
work_menu.add_command(label='詳細說明')#index=2

work_menu.activate(1)#指定index=1的內容

active.mainloop()

