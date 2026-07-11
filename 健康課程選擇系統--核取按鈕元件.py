'''健康課程選擇系統'''
import tkinter as tk
health=tk.Tk()
health.title('健康課程選擇系統')

label=tk.Label(health,text='健康課程選擇系統',font=('標楷體',20))
label.pack()

y_var=tk.IntVar()
h_var=tk.IntVar()
c_var=tk.IntVar()
s_var=tk.IntVar()
textvar=tk.StringVar()#存取文字內容
textvar1=tk.StringVar()
textvar2=tk.StringVar()
textvar3=tk.StringVar()

def healthy():
    if y_var.get()==1:#使用者有勾選
        textvar.set('參與有氧課程')
    else:
        textvar.set('有氧課程不參與')

def heavy_h():
    if h_var.get()==1:
        textvar1.set('參與重量訓練')
    else:
        textvar1.set('重量訓練不參與')

def course_class():
    if c_var.get()==1:
        textvar2.set('瑜珈課程參與')
    else:
        textvar2.set('瑜珈課程不參與')

def s_class():
    if s_var.get()==1:
        textvar3.set('參與伸展課程')
    else:
        textvar3.set('伸展課程不參與')


oxygen=tk.Checkbutton(health,variable=y_var,text='有氧課程',command=healthy)
oxygen.pack()

heavy=tk.Checkbutton(health,variable=h_var,text='重量訓練',command=heavy_h)
heavy.pack()

course=tk.Checkbutton(health,variable=c_var,text='瑜珈課程',command=course_class)
course.pack()

stretch=tk.Checkbutton(health,variable=s_var,text='伸展課程',command=s_class)
stretch.pack()

r_label=tk.Label(health,textvariable=textvar)
r_label.pack()

label2=tk.Label(health,textvariable=textvar1)
label2.pack()

label3=tk.Label(health,textvariable=textvar2)
label3.pack()

label4=tk.Label(health,textvariable=textvar3)
label4.pack()
health.mainloop()