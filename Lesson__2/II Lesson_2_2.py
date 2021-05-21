'''
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''
# https://drive.google.com/file/d/1d-A2fhc8saMYFs1HXnhnEAFCOtuPeeMg/view?usp=sharing
def func(number, even=0, odd=0, all=0):
    if number == 0:
        return even, odd, all
    if number % 2 == 0:
        even += 1
        all += 1
    else:
        odd += 1
        all += 1
    number = number // 10   # Не понял, почему без этого не работает и показывает превышение глубины рекурсии.
    return func(number, even, odd, all)

num = int(input('Введите многозначное число: '))
print(func(num))
