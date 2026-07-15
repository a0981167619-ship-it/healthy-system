file=open('truncate.txt','r+')
file.write('list=[1,2,3,4,5,6,7,8,9,10,11,12]')
file.seek(0)#回到開頭
print('目前檔案內文字內容:',file.read())

file.truncate(10)#從第10個位置開始截斷
file.seek(0)
print('截斷後的檔案文字內容:',file.read())

file.close()#關閉檔案