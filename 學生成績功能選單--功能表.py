'''學生成績功能選單'''
import tkinter as tk
score=tk.Tk()
score.title('學生成績功能選單')
menu=tk.Menu(score)
score.config(menu=menu)

score=tk.Menu(menu,tearoff=0)#將分隔線拿除
menu.add_cascade(label='成績',menu=score)#新增主功能項目
score.add_command(label='查詢成績')#index=0
score.add_command(label='輸入成績')#index=1
score.add_command(label='修改成績')#index=2                     #增加次功能項目
score.add_command(label='刪除成績')#index=3

score.activate(3)#選單選取index=3

system=tk.Menu(menu,tearoff=0)
menu.add_cascade(label='系統',menu=system)
system.add_command(label='清除資料')#index=0
system.add_command(label='重置系統')#index=1
system.add_command(label='離開')#index=2

system.activate(0)#選單選取index=0

score.mainloop()