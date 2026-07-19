file=open('rb+--範例檔.bin','rb+')
file.write(b'mysterious')
file.seek(0)
print(file.read())
file.seek(2)#從索引值為2的位置開始讀取
print(file.read())

file.write(b'misunderstanding')
file.seek(0)
print(file.read())

file_a=open('rb+--範例檔.bin','wb+')#清空原檔案內容、並重新寫入新的內容
file_a.write(b'0b0001')
file_a.seek(0)
pass_by=file_a.read()
print(pass_by)

file_b=open('rb+--範例檔.bin','ab+')
file_b.write(b'0b1110')
file_b.seek(7)#從索引值為7的位置開始讀取
print(file_b.read())
