# задача №1
n = int(input('Введите число от 1 до 7:'))
days = ['Понедельник', 'Вторник', 'Среда', 'Четверг','Пятница','Суббота','Воскресенье']
if 1 <= n <= 7:
    print(days[n - 1])
else:
    print('Число некорректное')

# задача №2
num = int(input('Введите число:'))
if num % 2 == 0:
    print('Четное число')
else:
    print('Нечетное число')

# задача №3
# вариант 1
n = abs(int(input('Введите число от 0 до 999:')))
if -999 <= n <= 999:
    if (n / 100) >= 1:
        print('Трехзначное число')
    elif (n / 10) >= 1:
        print('Двузначное число')
    else:
        print('Однозначное число')
else:
    print('Вне диапазона')

# вариант 2
n = abs(int(input('Введите число от 0 до 999:')))
if -999 <= n <= 999:
    if len(str(n)) == 3:
        print('Трехзначное число')
    elif len(str(n)) == 2:
        print('Двузначное число')
    else:
        print('Однозначное число')
else:
    print('Вне диапазона')

# задача №4
age = int(input('Введите возраст:'))
if 0 <= age <= 130:
   if age < 18:
       print('Голосование недоступно')
   else:
       print('Вам можно голосовать')
else:
    print('Введите корректный возраст')

# задача №5
num1 = float(input('Введите первое число:'))
num2 = float(input('Введите второе число:'))
num3 = float(input('Введите третье число:'))
print('Наибольшее число:', max(num1, num2, num3))

# задача №6
# вариант 1
num1 = float(input('Введите первое число:'))
num2 = float(input('Введите второе число:'))
num3 = float(input('Введите третье число:'))
if num1 == num2 or num1 == num3 or num2 == num3:
    print('Среди чисел есть одинаковые')
else:
    print('Все числа различны')

# вариант 2
nums = []
while True:
    num = input('Введите число: ')
    if num == '':
        break
    else:
        nums.append(float(num))

num_set = set(nums)
if len(nums) != len(num_set):
    print('Среди чисел есть одинаковые')
else:
    print('Все числа различны')

# задача №7
num1 = float(input('Введите первое число:'))
num2 = float(input('Введите второе число:'))
num3 = float(input('Введите третье число:'))
print(sorted([num1, num2, num3]))

# задача №8
mng1 = float(input('Введите продажи 1го менеджера:'))
mng2 = float(input('Введите продажи 2го менеджера:'))
mng3 = float(input('Введите продажи 3го менеджера:'))
salary = 200
if mng1 < 0 or mng2 < 0 or mng3 < 0:
    print('Премия не может быть отрицательной!')
else:
    if mng1 < 500:
        mng1 = mng1 * 0.03 + salary
    elif 500 <= mng1 <= 1000:
        mng1 = mng1 * 0.05 + salary
    else:
        mng1 = mng1 * 0.08 + salary
    if mng2 < 500:
        mng2 = mng2 * 0.03 + salary
    elif 500 <= mng2 <= 1000:
        mng2 = mng2 * 0.05 + salary
    else:
        mng2 = mng2 * 0.08 + salary
    if mng3 < 500:
        mng3 = mng3 * 0.03 + salary
    elif 500 <= mng3 <= 1000:
        mng3 = mng3 * 0.05 + salary
    else:
        mng3 = mng3 * 0.08 + salary
cash = max(mng1, mng2, mng3)
if mng1 > mng2 and mng1 > mng3:
    print('Лучший менеджер - №1')
elif mng2 > mng1 and mng2 > mng3:
    print('Лучший менеджер - №2')
else:
    print('Лучший менеджер - №3')
extracash = cash + 200
print('К начислению (с учетом премии 200$):', extracash)

# задача №9
year = int(input('Введите год:'))
month = int(input('Введите месяц:'))
myDict = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
if year % 4 == 0:
    myDict[2] = 29
if year <= 0:
    print('Неверное значение')
if 0 <= month > 12:
    print('Неверное значение')
print('Количество дней:', myDict[month])

# задача №10
age = int(input('Введите возраст:'))
if age < 0 or age > 130:
    print('Неверный возраст')
    exit(0)
time = int(input('Введите время сеанса:'))
if time < 0 or time > 23:
    print('Неверное время')
    exit(0)

if age <= 2:
    print('Бесплатно')
else:
    price = 15
    if 3 <= age <= 12:
        price = 10
    if time <= 12:
        price = price * 0.8
    print(price)
