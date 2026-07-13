import linecache
test=linecache.getline('test檔.py',2)
print(test)

linecache.checkcache('test檔.py')#檢查緩存區數據並更新

test2=linecache.getline('test檔.py',1)
print(test2)

linecache.checkcache('test檔.py')