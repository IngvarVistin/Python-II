'''
1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''

result = {}     # Создаём словарь
for i in range(2, 10):
    result[i] = []      # Присваиваем ключи от 2 до 9
    for _ in range(2, 100):
        if _ % i == 0:      # Если элемент последовательности от 2 до 99 делится на элемент ключа словаря без остатка,
            result[i].append(_)     # то добавляем его в значение словаря как список
    print(f'Число {i} кратно - {len(result[i])} числам из последовательности от 2 до 99')
