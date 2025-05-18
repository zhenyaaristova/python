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


