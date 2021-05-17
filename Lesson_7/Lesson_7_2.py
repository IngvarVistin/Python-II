'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
 заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
'''
import random
def sort(array):
    if len(array) <= 1:
        return array
    else:
        middle = int(len(array) // 2)
        left = sort(array[:middle])
        right = sort(array[middle:])
        return merge(left, right)
def merge(left, right):
    res = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            res.append(left[0])
            left = left[1:]
        else:
            res.append(right[0])
            right = right[1:]
    if len(left) > 0:
        res += left
    if len(right) > 0:
        res += right
    return res
    return array

array = [random.uniform(0, 49) for i in range(10)]
print(f'Исходный массив: {array}\n'
      f'Отсортированный массив: {sort(array)}')
