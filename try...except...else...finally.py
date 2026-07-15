try:#找除0錯誤
    b=int(input('請輸入整數:'))
    a=10/b
except ZeroDivisionError:#except--攔截程式錯誤
    print('Error-除0錯誤')

try:
    print(c)
except NameError:
    print('Error-未宣告變數')

try:
    a=10+[1,2,3]#數字不可以直接加list
except TypeError:
    print('Error--類型錯誤')

try:
    list=[1,2,3,4]
    print(list[4])
    print(list[10])
except IndexError:
    print('Error--指定索引錯誤')


try:
    bc=float(input('請輸入一浮點數:'))
    print(bc)
except ValueError:
    print('Error--輸入錯誤\n 請輸入浮點數:')

try:
   a=2
   list=[1,2,3]
   if a in list:
       print(a)
except SyntaxWarning:
    print('Warning--語法錯誤')

try:
    fish=int(input('請輸入一種動物:'))
    print('動物為{0}'.format(fish))
except Exception:
    print('Error')


