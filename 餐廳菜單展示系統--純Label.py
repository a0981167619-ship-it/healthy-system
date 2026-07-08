'''餐廳菜單展示系統'''
import tkinter as tk
restaurant=tk.Tk()
restaurant.title('餐廳菜單顯示系統')

label=tk.Label(text='今日菜單',font=('標楷體',38))
label.pack(pady=25)

label1=tk.Label(text='牛肉麵',font=('標楷體',20))
label1.pack(pady=10)

label2=tk.Label(text='價格:120元',font=('標楷體',20))
label2.pack(pady=10)

label3=tk.Label(text='雞肉飯',font=('標楷體',20))
label3.pack(pady=10)

label4=tk.Label(text='價格:80元',font=('標楷體',20))
label4.pack(pady=10)

label5=tk.Label(text='奶茶',font=('標楷體',20))
label5.pack(pady=10)

label6=tk.Label(text='價格:50元',font=('標楷體',20))
label6.pack(pady=10)

restaurant.mainloop()