'''遊戲角色狀態欄'''
import tkinter as tk
role=tk.Tk()
role.title('遊戲角色狀態欄')
role.geometry('600x400')#設置視窗大小

label=tk.Label(text='遊戲角色資訊簡介',font=('微軟正黑體',38))
label.pack(anchor='n')#位置定為正上方

label1=tk.Label(text='英雄資訊',font=('微軟正黑體',20))
label1.pack(pady=20,anchor='w')#位置定為左方中間

label2=tk.Label(text='英雄名稱: 森圖爾特',font=('微軟正黑體',20),fg="#3F07DA")
label2.pack(pady=20,anchor='w')

label3=tk.Label(text='主要位置: 射手',font=('微軟正黑體',20))
label3.pack(pady=20,anchor='w')

label4=tk.Label(text='使用此英雄時機: 對方有一半的英雄皆不為魔攻英雄時、可使用',font=('微軟正黑體',20),fg='red')
label4.pack(pady=20,anchor='w')

label5=tk.Label(text='搭配英雄: 夸克、貂蟬',font=('微軟正黑體',20))
label5.pack(pady=20,anchor='w')

label6=tk.Label(text='上述純屬於我以前的印象',font=('微軟正黑體',30),fg='red')
label6.pack(anchor='s',pady=200)#位置定為下方中間
role.mainloop()