# задача №7
def distance(x1, y1, x2, y2):
    return (((x2 - x1)**2) + ((y2 - y1)**2))**0.5
def trngl_per(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)
    return a + b + c
print(trngl_per(1, 2, 4, 5, 6,7))

# задача №8
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

primes = [i for i in range(100, 1000) if is_prime(i)]
print(primes)

# задача №9
def sum_dgts(n):
    summa = 0
    for d in str(n):
        summa += int(d)
    return summa

def lucky(n):
    s = str(n)
    if sum_dgts(s[:3]) == sum_dgts(s[3:]):
        print('Число счастливое')
    else:
        print('Число не счастливое')
lucky(123456)

# задача №10
def mx(n1, n2, n3, n4, n5, n6):
    return max(n1, n2, n3, n4, n5, n6)
print(mx(10, 35, 7543, 314, 6556,6))
