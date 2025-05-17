n = 5
while n < 10:
    print('Цикл работает')
    n += 1

n = 5
while n < 10:
    print('Работает')
    if n == 7:
        break # прерывает цикл
    n += 1

n = 5
while n < 10:
    n += 1
    if n == 7:
        continue # продолжает цикл
    print(n)

