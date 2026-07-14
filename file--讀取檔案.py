file=open('datetime模組.py','r',encoding='utf-8')
read=file.read(5)#僅讀取檔案前5個字元
print(read)

file1=open('return.py','r',encoding='utf-8')
read1=file1.read(20)#僅讀取檔案前20個字元
print(read1)

'''file.readlines'''
file3=open('傳值呼叫.py','r',encoding='utf-8')
read3=file3.readlines(20)#用於讀取整行並以序列結構返回
print(read3)

file4=open('學生成績單.py','r',encoding='utf-8')
read4=file4.readlines(45)
print(read4)

file5=open('最大值.py','r',encoding='utf-8')
read5=file5.readlines(30)
print(read5)

'''file.readline'''
file6=open('轉轉轉六邊形.py','r',encoding='utf-8')
read6=file6.readline(8)#用於讀取整行字串
print(read6)

file7=open('遞迴-費伯那序列.py','r',encoding='utf-8')
read7=file7.readline(6)
print(read7)
