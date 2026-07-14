file=open('a++.py','a+')
data=file.read()#讀取原本內容
print(data)

file.write('\nwe destination is in front of hospital.')
file.seek(0)#回到開頭
a=file.read()
print(a)

file.write('\n uh...')
file.seek(0)
a1=file.read()
print(a1)
file.close()