a = 5
b = 7
if a == b:
    print('a == b')
else:
    print('a != b')


num1str = input('Введите число')
num1 = int(num1str)
if num1 > 5:
    print('Это число больше пяти')

num2str = input('Введите число')
num2 = int(num2str)
if num2 >= 0:
    num2 = num2 + 1
else:
    num2 = num2 - 2
print(num2)

# homework
num3str = input('Введите число')
num3 = int(num3str)
if num3 >= -9 and num3 <= 2:
    print('Да')
else:
    print('Нет')