# # задача №7
# def distance(x1, y1, x2, y2):
#     return (((x2 - x1)**2) + ((y2 - y1)**2))**0.5
# def trngl_per(x1, y1, x2, y2, x3, y3):
#     a = distance(x1, y1, x2, y2)
#     b = distance(x2, y2, x3, y3)
#     c = distance(x3, y3, x1, y1)
#     return a + b + c
# print(trngl_per(1, 2, 4, 5, 6,7))
#
# # задача №8
# def is_prime(n):
#     if n < 2: return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True
#
# primes = [i for i in range(100, 1000) if is_prime(i)]
# print(primes)
#
# # задача №9
# def sum_dgts(n):
#     summa = 0
#     for d in str(n):
#         summa += int(d)
#     return summa
#
# def lucky(n):
#     s = str(n)
#     if sum_dgts(s[:3]) == sum_dgts(s[3:]):
#         print('Число счастливое')
#     else:
#         print('Число не счастливое')
# lucky(123456)
#
# # задача №10
# def mx(n1, n2, n3, n4, n5, n6):
#     return max(n1, n2, n3, n4, n5, n6)
# print(mx(10, 35, 7543, 314, 6556,6))

# задача №13
# def area(a, b, h):
#     s = ((a + b)/2) * h
#     side = (((a - b)/2)**2 + h**2)**0.5
#     p = a + b + 2 * side
#     return s, p
# tr1 = area(4, 10, 3)
# tr2 = area(6, 15, 5)
# print(f'Сумма площадей трапеций: {tr1[0] + tr2[0]}')
# print(f'Сумма периметров трапеций: {tr1[1] + tr2[1]}')

# задача №14
# def cir(r):
#     return 3.14 * (r ** 2)
# def tri(a, h):
#     return (a * h)/2
# def rec(a, b):
#     return a * b
#
# print('1 - Круг')
# print('2 - Треугольник')
# print('3 - Прямоугольник')
# figure = input('Введите номер фигуры, площадь которой необходимо найти: ')
# if figure == '1':
#     r = float(input('Введите радиус круга: '))
#     print('Площадь круга:',cir(r))
# elif figure == '2':
#     a = float(input('Введите основание: '))
#     h = float(input('Введите высоту: '))
#     print('Площадь треугольника:',tri(a, h))
# elif figure == '3':
#     a = float(input('Введите первую сторону: '))
#     b = float(input('Введите вторую сторону: '))
#     print('Площадь прямоугольника:', rec(a,b))
# else:
#     print('Введена ошибочная команда')

# задача №16
# def draw_square(n, s):
#     for i in range(n):
#         print(s * n)
# n = int(input("Введите размер квадрата (n): "))
# s = input("Введите символ для квадрата (s): ")
# draw_square(n, s)

# задача №17
# def num(n):
#     for i in range(1, n+1):
#         if n % i == 0:
#             print(i, end=' ')
#     print()
#
# while True:
#     x = int(input('Введите число (0 для выхода из программы): '))
#     if x == 0:
#         break
#     num(x)
