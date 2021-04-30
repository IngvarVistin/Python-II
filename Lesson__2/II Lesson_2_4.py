'''
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
'''
# https://drive.google.com/file/d/1d-A2fhc8saMYFs1HXnhnEAFCOtuPeeMg/view?usp=sharing
numbers = int(input('Введите количество чисел: '))
figure = input('Введите цифру для подсчёта: ')
attempt = 0
attempt_figure = 0
while attempt < numbers:
    num = input('Введите последовательность цифр: ')
    attempt += 1
    attempt_figure += num.count(figure)
print(f'В последовательности цифр {num} содержится {attempt_figure} цифр {figure}!')
