'''
6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
'''
# https://drive.google.com/file/d/1d-A2fhc8saMYFs1HXnhnEAFCOtuPeeMg/view?usp=sharing
import random
rand_num = random.randint(0, 100)
attempt = 0
while attempt < 10:
    num = int(input('Угадайте число: '))
    attempt += 1
    print(f'Попытка № {attempt}, осталось {10-attempt} попыток!')
    if num == rand_num:
        print('Вы угадали число!')
        break
    elif num > rand_num:
        print('Вы назвали число больше, чем загадано!')
    else:
        print('Вы назвали число меньше, чем загадано')
else:
    print('Вы не угадали!')
    print(f'Загаданное число = {rand_num}')