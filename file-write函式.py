file=open('empty.py',mode='w')
w=file.write('can')#將字串寫入檔案
print(w)#返回字串長度

file2=open('empty.py',mode='w')
w2=file2.write("I'm helpless")
print(w2)

file3=open('empty.py',mode='w')
list=['sad\n','upset\n','powerless\n']#換行
file3.writelines(list)

file3=open('empty.py',mode='r')#再次讀取
print(file3.read())

file4=open('empty.py',mode='w')
list2=['hope\n','expect\n','surprise\n']
file4.writelines(list2)

file4=open('empty.py',mode='r')
w4=file4.read()
print(w4)#印出讀取的文檔內容