'''
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
'''

import random

size = 20
beginning = 0
end = 100
array = [random.randint(beginning, end) for _ in range(size)]
print(f'Сгенерированный массив: {array}')

min_pos_1, min_pos_2 = end, end

for i in array:
    if min_pos_1 > i:
        min_pos_2 = min_pos_1
        min_pos_1 = i
    elif min_pos_2 > i:
        min_pos_2 = i
print(f'Два минимальных числа в массиве: {min_pos_1} и {min_pos_2}')
