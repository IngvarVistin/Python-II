'''
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
Результаты анализа сохранить в виде комментариев в файле с кодом.
'''
# С решетом Эратосфена

import cProfile
import timeit

def eratothfen(n):
    a = [0] * n             # создание массива с n количеством элементов
    for i in range(n):      # заполнение массива
        a[i] = i            # значениями от 0 до n-1
    a[1] = 0
    m = 2                   # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n:            # перебор всех элементов до заданного числа
        if a[m] != 0:       # если он не равен нулю, то
            j = m * 2       # увеличить в два раза (текущий элемент простое число)
            while j < n:
                a[j] = 0    # заменить на 0
                j = j + m   # перейти в позицию на m больше
        m += 1
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    del a
    return b
cProfile.run('eratothfen(100_000)')
'''
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.035    0.035 <string>:1(<module>)
        1    0.034    0.034    0.035    0.035 Lesson_4_2.py:12(eratothfen)
        1    0.000    0.000    0.035    0.035 {built-in method builtins.exec}
     9592    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
print(timeit.timeit('eratothfen(100_000)', number=1, globals=globals()))    #0.035516500000000006

cProfile.run('eratothfen(1_000_000)')
'''
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.005    0.005    0.380    0.380 <string>:1(<module>)
        1    0.369    0.369    0.375    0.375 Lesson_4_2.py:12(eratothfen)
        1    0.000    0.000    0.380    0.380 {built-in method builtins.exec}
    78498    0.006    0.000    0.006    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
print(timeit.timeit('eratothfen(1_000_000)', number=1, globals=globals()))  #0.4332422
# При уыеличении чисел на порядок, на порядок увеличивается и время.
