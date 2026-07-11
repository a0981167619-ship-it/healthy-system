'''旅遊行程選擇系統'''
import tkinter as tk
travel=tk.Tk()
travel.title('旅遊行程選擇系統')

label=tk.Label(travel,text='旅遊行程選擇',font=('標楷體',20),fg='blue')
label.pack()

activity=tk.IntVar()
beach=tk.StringVar()

def sea():
    if activity.get()==1:
        beach.set('海邊活動納入行程')
    else:
        beach.set('海邊活動不納入此次行程')

mountain=tk.IntVar()
hiking=tk.StringVar()

def  hill():
    if mountain.get()==1:
        hiking.set('登山健行活動納入行程')
    else:
        hiking.set('登山健行活動不納入此次行程')

museum=tk.IntVar()
display=tk.StringVar()

def paint():
    if museum.get()==1:
        display.set('博物館參觀納入此次行程')
    else:
        display.set('博物館參觀不納入此次行程')

night=tk.IntVar()
market=tk.StringVar()

def night_market():
    if night.get()==1:
        market.set('吃夜市美食')
    else:
        market.set('不吃夜市美食')

seaside=tk.Checkbutton(travel,command=sea,text='海邊活動',variable=activity)
seaside.pack()

hike=tk.Checkbutton(travel,command=hill,text='登山活動',variable=mountain)
hike.pack()

visit=tk.Checkbutton(travel,command=paint,text='博物館參觀',variable=museum)
visit.pack()

delicious=tk.Checkbutton(travel,command=night_market,text='夜市美食',variable=night)
delicious.pack()

label2=tk.Label(travel,textvariable=beach)
label2.pack()

label3=tk.Label(travel,textvariable=hiking)
label3.pack()

label4=tk.Label(travel,textvariable=display)
label4.pack()

label5=tk.Label(travel,textvariable=market)
label5.pack()
travel.mainloop()

