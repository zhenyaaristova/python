import math

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

print('туториал', 'по', 'print', sep = '\n') # \n переносит на другую строку

a = 5
print(a)
a = b = f = 7
print(a, b, f)

a -= 1
a = a - 1
print(a)

print(5/2) # выводит дробное значение
print(5//2) # выводит целое число (отбрасывание дробной части без округления)

print(5 * 2) # умножение
print(5 ** 2) # возведение в степень

a = 4
b = 10
print('a =', a, 'b =', b)
a, b = b, a
print('a =', a, 'b =', b) # обмен значениями

a = input('enter value: ') # ввод данных
print(a)

a = int(input('enter value: ')) # ограничивает ввод: только целочисленные значения (int)
print(a)

"""
так можно писать 
многострочные комментарии
"""

a = 5
b = 8
c = -10
d = 500000
e = 600_000 # нижнее подчеркивание используется для удобства чтения числа
print(a, b, c, d, e)

num = 1.7e2 #1.7*10^2
print(num)

# логический тип данных (boolean)
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
print('М.Ю.Лермонтов "Бородино"') # названия можно записать в двойных кавычках
print("М.Ю.Лермонтов \"Бородино\"") # экранирование
print('Hello ' + 'world') # объединение двух строк в одну (конкатенация)
print('Hello world ' * 3) # дупликация

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

# списки (lists)
myList = ['string', 543, 544.4, True] #отсчет элементов списка начинается с нуля
print(myList) # выводит весь список
print(myList[0]) # выводит нулевой элемент списка (по порядковому номеру он первый)
print(myList[1:3]) # выводит первый и второй элементы списка (третий не включительно)
print(myList[1:]) # выводит с первого элемента и до конца списка

# кортежи (tuples)
myTuple = (65, 45.21, True, 'String')
print(myTuple)
print(myTuple[0])
print(myTuple[3])
print(myTuple[2:4])
print(myTuple[1:])

# словари (dictionaries)
myDict = {'name': 'Evgeniya', 'role': 'QA', 123: 'test-value', 456: 567.54}
print(myDict)
print(myDict['name'])
print(myDict[123])
# в словаре невозможно обратиться к значению по индексу, как в списках и кортежах
# print(myDict[0]) будет ошибка

name = 'Evgeniya'
myDict = {
    'name': name,
    'role': 'QA'
}
print(myDict['name'])
print(myDict.keys()) # выводит ключи
print(myDict.values()) # выводит значения

# множества (sets)
myList = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 7] # оставляет только УНИКАЛЬНЫЕ значения
mySet = set(myList)
print(mySet)

myList = ['Good', 'good', 'day', 'day'] # чувствителен к регистру
mySet = set(myList)
print(mySet)

# преобразование типа данных
# в данном случае значение а перезаписывается:
a = 5
a = 'string'
a = [5, 5, 6]

# преобразование без утери значения:
# в целочисленное значение:
a = 1.7
a = int(a)
print(a)

# в строку:
x = 5.66
x = str(x)
print(x)

a = 'hello world!'
a = list(a)
print(a) # строка разбивается на буквы

myList = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 7]
mySet = set(myList)
myList = list(mySet)
print(myList)

myTuple = tuple(myList)
print(myTuple)

print(ord('A')) # выводит код буквы
print(chr(1040)) # выводит букву соответствующую коду
print(f"\\u{ord("а"):64x}") # вывод юникод-значения буквы "а"

# основные операторы
a = 5
b = 10
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) # остаток от деления
print(10//3) # отбрасывает остаток
print(-10//3) # округляет
print(5==5) # равенство
print(5!=5) # неравенство


a = a + b
print(a)
a += b # эквивалентная короткая запись

# Стандартные математические функции
print(abs(-89)) # модуль числа
print(abs(67))

print(pow(5, 2)) # возведение в степень
print(pow(5, -5))
print(pow(5, 2, 5)) # возводит 5 в степень 2, делит на третье значение (5) и оставляет остаток от деления

print(round(2.654279869)) # округление
print(round(2.7878679, 2)) # округляет до 2 знака после запятой (второе значение)

# Функции в библиотеке MATH

# округление в большую сторону
print(math.ceil(5.7)) # 6
print(math.ceil(5.2)) # 6
# округление в меньшую сторону
print(math.floor(5.7)) # 5
print(math.floor(5.24)) # 5

print(math.log(25, 2)) # логарифм 25 по основанию 2
print(math.sqrt(25)) # квадратный корень из 25
