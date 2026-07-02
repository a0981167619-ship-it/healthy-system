import tkinter as tk
conventional=tk.Tk()
var=tk.StringVar()
entry=tk.Entry(conventional,textvariable=var)
entry.pack()

label=tk.Label(conventional,textvariable=var)
label.pack()

conventional.mainloop()
