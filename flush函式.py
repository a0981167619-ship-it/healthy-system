file=open('flush範例檔.py','w+')#檔案可讀寫
file.write('can we?')
file.seek(0)#回到開頭
print(file.read())
file.flush()#使用flush仍可繼續寫入

file.write('\nwe can?')
file.seek(0)
print(file.read())
file.close()