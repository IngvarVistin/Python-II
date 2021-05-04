'''
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
'''
import random

size = 20
beginning = -50
end = 100
array = [random.randint(beginning, end) for _ in range(size)]
print(f'Сгенерированный массив: {array}')
min_i, pos_i = 0, 0
for i in array:
    if min_i > i:
        min_i = i
        pos_i = array.index(i)
if min_i >= 0:
    print('В массиве нет отрицацельных чисел!')
else:
    print(f'Минимальный отрицательный элемент в массиве: {min_i}\n'
          f'Позиция в массиве: {pos_i}')
