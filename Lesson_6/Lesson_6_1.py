'''
2.9 Среди натуральных чисел, которые были введены,
найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
6.1 Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
'''
import random
import sys

def show(obj):
    print(f'{type(obj)=}, {sys.getsizeof(obj)=}, {obj=}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                show(key)
                show(value)
        else:
            for item in obj:
                show(item)
'''
Вариант №1
'''
#quant = int(input('Введите количество цифр: '))
#quant = random.randint(5, 100)
quant = 30  # Чтобы генерировалось одинаковое количество цифр для анализа затрат памяти
attempt, max_summ, num_max_sum = 0, 0, 0
while attempt < quant:
    #number = input('Введите натуральное число: ')
    number = random.randint(10, 1000)
    summ = sum(map(int, str(number)))
    if max_summ < summ:
        max_summ = summ
        num_max_sum = number
    attempt += 1
print(f'В числе {num_max_sum},наибольшая сумма чисел: {max_summ}')

show(quant)
show(num_max_sum)
show(max_summ)

'''
Вариант №2
'''

mass = []
max_summ, num_max_sum = 0, 0
for i in range(30):
    number = random.randint(10, 1000)
    mass.append(number)
for number in mass:
    summ = sum(map(int, str(number)))
    if max_summ < summ:
        max_summ = summ
        num_max_sum = number
print(f'В числе {num_max_sum}, из последовательности {mass},\nнаибольшая сумма чисел: {max_summ}')

show(mass)
show(num_max_sum)
show(max_summ)

'''
OS x64, Python 3.8
Первый вариант затрачивает меньше памяти, т.к. не нужно хранить весь список сгенерированных данных в памяти, в отличае от 2-го варианта

В числе 799,наибольшая сумма чисел: 25
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=30
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=799
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=25
В числе 967, из последовательности [532, 680, 354, 643, 980, 807, 175, 967, 99, 377, 151, 648, 790, 950, 993, 461, 696, 728, 631, 941, 677, 824, 352, 130, 734, 29, 817, 443, 77, 674],
наибольшая сумма чисел: 22
type(obj)=<class 'list'>, sys.getsizeof(obj)=336, obj=[532, 680, 354, 643, 980, 807, 175, 967, 99, 377, 151, 648, 790, 950, 993, 461, 696, 728, 631, 941, 677, 824, 352, 130, 734, 29, 817, 443, 77, 674]
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=532
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=680
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=354
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=643
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=980
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=807
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=175
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=967
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=99
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=377
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=151
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=648
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=790
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=950
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=993
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=461
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=696
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=728
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=631
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=941
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=677
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=824
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=352
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=130
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=734
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=29
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=817
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=443
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=77
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=674
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=967
type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=22

'''
