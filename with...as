with open('二維串列.py','r',encoding='utf-8') as file:
    print(file.read())#讀取檔案裡的內容

try:#使用try...finally方法,兩者結果相等
    file=open('二維串列.py','r',encoding='utf-8')
finally:
    print(file.read())

with open('example.txt','w+',encoding='utf-8') as i:
    i.write('list=[23,456,259]')
    i.seek(0)#回到開頭
    print('檔案內容:',i.read())

try:
    file=open('example.py','w+',encoding='utf-8')
finally:
    file.flush()
    file.write('list=[128,256,512]')
    file.seek(0)
    print('檔案內容:',file.read())
