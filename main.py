print('привет', 'мир', '!')

print(55, 67, 78.5)

print(True)

a = 1
b = 2
print(a + b)
print('сумма =', a + b)

x = 2
y = 5
print(x, '+', y, '=', x+y, sep = '')

print('туториал', 'по', 'print', sep = '\n') #\n переносит на другую строку

a = 5
print(a)
a = b = f = 7
print(a, b, f)

a -= 1
a = a - 1
print(a)

print(5/2) #выводит дробное значение
print(5//2) #выводит целое число (отбрасывание дробной части без округления)

print(5 * 2) #умножение
print(5 ** 2) #возведение в степень

a = 4
b = 10
print('a =', a, 'b =', b)
a, b = b, a
print('a =', a, 'b =', b) #обмен значениями

a = input('enter value: ') #ввод данных
print(a)

a = int(input('enter value: ')) #ограничивает ввод: только целочисленные значения (int)
print(a)

"""
так можно писать 
многострочные комментарии
"""

a = 5
b = 8
c = -10
d = 500000
e = 600_000 #нижнее подчеркивание используется для удобства чтения числа
print(a, b, c, d, e)

num = 1.7e2 #1.7*10^2
print(num)

#логический тип данных (boolean)
print(bool(0))
print(bool(-1))
print(bool(5))
print(bool(0.0))
print(bool(True))
print(bool(False))
print(bool(''))
print(bool(' '))
print(bool('Hello world'))

print(2 == 2) # == - сравнение чисел
print(2 != 3) # != - знак неравенства

# строки (string)
print('М.Ю.Лермонтов "Бородино"') #названия можно записать в двойных кавычках
print("М.Ю.Лермонтов \"Бородино\"") #экранирование
print('Hello ' + 'world') #объединение двух строк в одну (конкатенация)
print('Hello world ' * 3) #дупликация

print(5 + 5)
# print(5 + '5') будет ошибка по типу данных
print(5 + int('5'))

a = 5
b = 10
result = a + b
print(a, '+', b, '=', result)
final = str(a) + ' + ' + str(b) + ' = ' + str(result)
print(final)
final_v2 = (f'Результат выражения:\n'
            f'{a} + {b} = {result}')
print(final_v2)

#списки (list)
myList = ['string', 543, 544.4, True] #отсчет элементов списка начинается с нуля
print(myList) #выводит весь список
print(myList[0]) #выводит нулевой элемент списка (по порядковому номеру он первый)
print(myList[1:3]) #выводит первый и второй элементы списка (третий не включительно)
print(myList[1:]) #выводит с первого элемента и до конца списка