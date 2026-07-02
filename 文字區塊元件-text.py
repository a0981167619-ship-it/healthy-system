import tkinter as tk
victory=tk.Tk()
victory.title('text-多行文字')
sentence='math=76 english=88 chinese=87 biology=96'
text1=tk.Text(victory,borderwidth=30,height=30,wrap='word')
text1.insert('1.2',sentence)
text1.insert(tk.END,'  history=87')
text1.pack()


aword='I think it was possible you agree?'
text2=tk.Text(borderwidth=10,height=30,bg="#FDFDEE",wrap='char',highlightbackground="#E9E78F",highlightcolor="#79D8AC",highlightthickness=2)#外邊框被景色為黃色,highlightcolor點進去時:外框會變色
text2.insert("1.1",aword)#在第一行的第一個位置插入字串
text2.insert(tk.INSERT,'I think it is a perfect plan')
text2.pack()


'''每日代辦事項'''
def added():
    text3.insert(tk.END,entry.get()+'\n')
 
entry=tk.Entry(victory)
entry.pack()

text3=tk.Text(victory,borderwidth=30,height=30,wrap='char',bg='#FFF3BF',highlightbackground='#FFD6E0',highlightthickness=2)
text3.pack()

button=tk.Button(victory,text='增加',command=added)
button.pack()

victory.mainloop()
