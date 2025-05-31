# задача №1
for x in range(2, 51, 2):
    print(x)

# задача №2
summ = 0
for x in range(1, 101):
    summ = summ + x
print(summ)

#2 вариант решения
print(sum(range(1, 101)))

# задача №3
num = int(input("Введите число:"))
prime = True
if num >= 2:
    for x in range (2, num):
        if num % x == 0:
            prime = False
            break
else:
    prime = False
if prime:
    print('Число является простым')
else:
    print('Число не является простым')

# задача №4
num = int(input("Введите число:"))
result = 1
for x in range(1, num+1):
    result *= x
print(result)

# задача №5
num1 = 0
num2 = 1
print(num1)
print(num2)
for x in range (8):
    num3 = num1 + num2
    print(num3)
    num1 = num2
    num2 = num3

# задача №6
for x in range(10, 0, -1):
    print(x)

# задача №7
string = input('Введите текст: ')
n = 0
vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
for x in string:
    if x in vowels:
        n += 1
print(n)

# задача №8
numb = input('Введите число:')
sum = 0
for x in numb:
    sum += int(x)
print(sum)

# задача №9
for x in range(1, 11):
    for y in range(1, 11):
        n = x * y
        print(f'{x} * {y} = {n}')

# задача №10
numbers = [3, -10, 65, 5, 10, 7, 345]
result = []
for x in numbers:
    if abs(x) > 5:
        result.append(x)
print(result)

# задача 11
letters = 'hvbhFfffFfFgG'
result = ''

for letter in letters:
    if letter.islower():
        result += letter
print(result)


# задача 12
secret_list = ["Мавпродош", "Лорнектиф", "Древерол", "Фиригарпиг", "Клодобродыч"]

while True:
    nickname = input("Введите ваш никнейм: ")
    if nickname in secret_list:
        print(f"Ты – свой. Приветствую, любезный {nickname}!")
        break
    else:
        print("Тут ничего нет. Еще есть вопросы?")

