'''
9. Среди натуральных чисел, которые были введены,
найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
'''
# https://drive.google.com/file/d/1d-A2fhc8saMYFs1HXnhnEAFCOtuPeeMg/view?usp=sharing
quant = int(input('Введите количество цифр: '))
attempt, max_summ, num_max_sum = 0, 0, 0
while attempt < quant:
    number = input('Введите натуральное число: ')
    summ = sum(map(int, list(number)))
    if max_summ < summ:
        max_summ = summ
        num_max_sum = number
    attempt += 1
print(f'В числе {num_max_sum},наибольшая сумма чисел: {max_summ}')
