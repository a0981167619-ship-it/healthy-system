file=open('truncate.txt','r+')#可寫入任何位置
file.write('Hello My name is sherrie')
file.seek(0)
print('目前檔案內的文字為:',file.read())

file.truncate(5)#從游標的第5個位置截斷
file.seek(0)
print('截斷後的文字為:',file.read())

