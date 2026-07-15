file=open('truncate.txt','r+')
file.write('Nice to meet you.')
file.seek(0)
new=file.read()
print('目前文字:',new)


file.truncate(7)#從游標7的位置開始截斷
file.seek(0)#回到開頭
print('現在文字:',file.read())

