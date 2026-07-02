'''每日代辦事項'''
import tkinter as tk
victory=tk.Tk()
def added():
    text3.insert(tk.END,entry.get()+'\n')
 
entry=tk.Entry(victory)
entry.pack()

text3=tk.Text(victory,borderwidth=30,height=30,wrap='char',bg='#FFF3BF',highlightbackground='#FFD6E0',highlightthickness=2)
text3.pack()

button=tk.Button(victory,text='增加',command=added)
button.pack()

victory.mainloop()
