''' 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь. '''

number = str(input("Введите трёхзначное число: "))
summ = int(number[0]) + int(number[1]) + int(number[2])
composition = int(number[0]) * int(number[1]) * int(number[2])
number = int(input("Введите трёхзначное число: "))
x = number//100
y = number % 100 // 10
z = number % 10
summ = x + y + z
composition = x * y * z
print(f'Сумма цифр в числе = {summ}\n'
      f'Произведение цифр в числе = {composition}')