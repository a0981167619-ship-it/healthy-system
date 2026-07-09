'''網路購物訂單計算系統'''
import tkinter as tk
net=tk.Tk()
net.title('網路購物訂單計算系統')
net.geometry('500x400')

label=tk.Label(text='網路購物訂單計算系統',font=('新細明體',40))
label.pack(side='top')

label1=tk.Label(text='商品名稱:',font=('新細明體',20))
label1.pack(anchor='n')#將位置定為上方中間

product=tk.Entry(net)
product.pack()

label2=tk.Label(text='商品單價:',font=('新細明體',20))
label2.pack(pady=30)

cost=tk.Entry(net)
cost.pack()

label3=tk.Label(text='購買數量:',font=('新細明體',20))
label3.pack(pady=30)

buy=tk.Entry(net)
buy.pack()

result=tk.Label(net,font=('新細明體',20))
result.pack()

outcome=tk.Label(net,font=('新細明體',20))
outcome.pack()

end=tk.Label(net,font=('新細明體',20))
end.pack()

def order():
    product1=product.get()
    result.config(text='商品名稱:'+product1)

    outcome1=cost.get()
    outcome.config(text='商品單價:'+outcome1)

    end1=buy.get()
    end.config(text='購買數量:'+end1)

button=tk.Button(text='計算訂單',command=order)
button.pack()



net.mainloop()