'''
3.5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
4.1 Проанализировать скорость и сложность алгоритма
'''

import random
import cProfile
import timeit

def mass_1(size, beginning, end):
    array = [random.randint(beginning, end) for _ in range(size)]
#    print(f'Сгенерированный массив: {array}')
    min_i, pos_i = 0, 0
    for i in array:
        if min_i > i:
            min_i = i
            pos_i = array.index(i)
    if min_i >= 0:
        return 'В массиве нет отрицацельных чисел!'
    else:
        return f'Минимальный отрицательный элемент в массиве: {min_i}\nПозиция в массиве: {pos_i}'

cProfile.run('mass_1(10_000, -10_000, 10_000)')
'''
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.019    0.019 <string>:1(<module>)
        1    0.001    0.001    0.019    0.019 Lesson_4_1.py:35(mass)
        1    0.002    0.002    0.018    0.018 Lesson_4_1.py:36(<listcomp>)
    10000    0.006    0.000    0.013    0.000 random.py:200(randrange)
    10000    0.003    0.000    0.016    0.000 random.py:244(randint)
    10000    0.005    0.000    0.007    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.019    0.019 {built-in method builtins.exec}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    16327    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
'''

print(timeit.timeit('mass_1(10_000, -10_000, 10_000)', number=1, globals=globals()))        # 0.008897000000000002
print(timeit.timeit('mass_1(10_000, -10_000, 10_000)', number=100, globals=globals()))      # 0.870988
print(timeit.timeit('mass_1(10_000, -10_000, 10_000)', number=1000, globals=globals()))     # 8.7144886

def mass_2(size, beginning, end):
    array = [random.randint(beginning, end) for _ in range(size)]
#    print(f'Сгенерированный массив: {array}')
    if min(array) >= 0:
        return 'В массиве нет отрицацельных чисел!'
    else:
        return f'Минимальный отрицательный элемент в массиве: {min(array)}\nПозиция в массиве: {array.index(min(array))}'

cProfile.run('mass_2(10_000, -10_000, 10_000)')
'''
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.024    0.024 <string>:1(<module>)
        1    0.001    0.001    0.024    0.024 Lesson_4_1.py:65(mass)
        1    0.002    0.002    0.018    0.018 Lesson_4_1.py:66(<listcomp>)
    10000    0.006    0.000    0.013    0.000 random.py:200(randrange)
    10000    0.003    0.000    0.015    0.000 random.py:244(randint)
    10000    0.005    0.000    0.007    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.024    0.024 {built-in method builtins.exec}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        1    0.005    0.005    0.005    0.005 {built-in method builtins.print}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    16268    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
'''
print(timeit.timeit('mass_2(10_000, -10_000, 10_000)', number=1, globals=globals()))    # 0.00894109999999948
print(timeit.timeit('mass_2(10_000, -10_000, 10_000)', number=100, globals=globals()))    # 0.9092558999999998
print(timeit.timeit('mass_2(10_000, -10_000, 10_000)', number=1000, globals=globals()))     # 8.9917814
