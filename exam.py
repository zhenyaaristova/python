# задача 1
# num1 = float(input('Введите первое число: '))
# num2 = float(input('Введите второе число: '))
# oper = input('Введите оператор (+, -, *, /): ')
# res = None
#
# if oper == '+':
#     res = num1 + num2
# elif oper == '-':
#     res = num1 - num2
# elif oper == '*':
#     res = num1 * num2
# elif oper == '/':
#     if num2 != 0:
#         res = num1 / num2
#     else:
#         print('Деление на ноль!')
# else:
#     print('Некорректный оператор!')
#
# if res != None:
#     print(f'{num1} {oper} {num2} = {res}')

# задача 5
# nums = input('Введите числа (через запятую): ')
# cl_nums = nums.split(',')
# result = 0
#
# for i, x in enumerate(cl_nums):
#     if i % 2 != 0:
#         num = float(x.strip())
#         result += num
#
# print(f'Сумма чисел на нечетных позициях равна {result}')