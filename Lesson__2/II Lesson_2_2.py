'''
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''

number = input('Введите многозначное число: ')
even = 0
odd = 0
all = 0

for i in number:
    if int(i) % 2 == 0:
        even += 1
        all += 1
    else:
        odd += 1
        all += 1
print(f'Количество чётных цифр в числе: {even}\n'
      f'Количество нечётных цифр в числе: {odd}\n'
      f'Всего цифр в числе: {all}')
