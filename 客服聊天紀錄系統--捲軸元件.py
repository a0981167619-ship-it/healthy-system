'''客服聊天紀錄系統'''
import tkinter as tk
guest=tk.Tk()
guest.title('客服聊天紀錄系統')

scroll=tk.Scrollbar(guest,orient='horizontal')
text=tk.Text(guest,xscrollcommand=scroll.set,wrap='none')    #兩者互相連接
scroll.config(command=text.xview)

scroll.pack(fill='x',side='bottom')
text.pack(expand=True,fill='both',side='right')

def survice():
    for k in range(50):
        text.insert(tk.END,'您好,這是一段非常長的測試訊息')

button=tk.Button(guest,text='測試',command=survice)
button.pack()
guest.mainloop()