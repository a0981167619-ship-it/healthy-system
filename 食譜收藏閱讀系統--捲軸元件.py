'''食譜收藏閱讀系統'''
import tkinter as tk
recipe=tk.Tk()

recipe.title('食譜收藏閱讀系統')

label1=tk.Label(text='食譜收藏閱讀系統',font=('標楷體',20))
label1.pack(side='top')

scroll=tk.Scrollbar(recipe)

text=tk.Text(recipe,yscrollcommand=scroll.set,highlightbackground="#83D6E0",highlightthickness=3)   #兩者互相連接

scroll.config(command=text.yview)

text.pack(fill='y',expand=True,side='left')
scroll.pack(fill='y',side='right')

def recipe1():
    for i in range(100):
                      text.insert(tk.END,'recipe')

button=tk.Button(recipe,command=recipe1,text='check')
button.pack()

recipe.mainloop()





