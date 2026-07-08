'''學生成績單'''
import tkinter as tk
student=tk.Tk()
student.title('學生成績單')
student.geometry('500x300')#設置視窗大小

label=tk.Label(text='學生成績單',font=('Calibri',38))
label.grid(column=2,row=0)#定位為第0列、第二欄

label1=tk.Label(text='科目',font=('Calibri',20))
label1.grid(column=0,row=1,padx=20)#定位為第一列、第0欄

label2=tk.Label(text='成績:',font=('Calibri',20))
label2.grid(column=1,row=1,padx=20)#定位為第一列、第一欄

label3=tk.Label(text='國文: 90分',font=('Calibri',20))
label3.grid(column=1,row=2,pady=15)#定位為第二列、第一欄

label4=tk.Label(text='英文: 85分',font=('Calibri',20))
label4.grid(column=1,row=3,pady=15)#定位為第三列、第一欄

label5=tk.Label(text='數學: 95分',font=('Calibri',20))
label5.grid(column=1,row=4,pady=15)#定位為第四列、第一欄



student.mainloop()
