# задача №1
string = input('Введите строку: ')
print(string[::-1])

# задача №2
st1 = input('Введите первую строку: ').lower()
st2 = input('Введите вторую строку: ').lower()
str1 = sorted(st1)
str2 = sorted(st2)
if str1 == str2:
    print('Строки являются анаграммами')
else:
    print('Строки не являются анаграммами')

# задача №3
string = input('Введите строку: ').lower()
vowels = 'ауоыиэяюёе'
consonants = 'бвгджзйклмнпрстфхцчшщ'
v = 0
c = 0
for x in string:
    if x in vowels:
        v += 1
    elif x in consonants:
        c += 1
print(f'Гласных букв: {v} Согласных букв: {c}')

# задача №4
string = input('Введите строку: ').lower()
string = string.replace(' ', '')
string = string.replace(',', '')
if string == string[::-1]:
    print('Строка является палиндромом')
else:
    print('Строка не является палиндромом')