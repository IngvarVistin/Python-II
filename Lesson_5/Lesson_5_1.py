'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
чья прибыль ниже среднего.
'''
from collections import namedtuple
buisnesses = namedtuple('buisnesses', 'name_buisnes, first_quarter, scond_quarter, third_quarter, fourth_quarter, full_profit')
all_buisnesses = set()
quant_buisness = int(input('Введите количество предприятий: '))
total_profit = 0
for i in range(1, quant_buisness + 1):
    name_buisnes = input(f'\nВведите наиминование {i}-го предприятия: ')
    first_quarter = int(input('\nВведите прибыль за первый кваартал: '))
    scond_quarter = int(input('Введите прибыль за второй кваартал: '))
    third_quarter = int(input('Введите прибыль за третий кваартал: '))
    fourth_quarter = int(input('Введите прибыль за четвертый кваартал: '))
    full_profit = first_quarter + scond_quarter + third_quarter + fourth_quarter
    total_profit += full_profit
    company = buisnesses(
        name_buisnes=name_buisnes, first_quarter=first_quarter, scond_quarter=scond_quarter,
        third_quarter=third_quarter, fourth_quarter=fourth_quarter, full_profit=full_profit
        )
    all_buisnesses.add(company)

print(f'Средняя прибыль по всем предприятиям за год составляет: {total_profit / quant_buisness}')
for company in all_buisnesses:
    if company.full_profit > (total_profit / quant_buisness):
        print(f'Предприятие {company.name_buisnes} с прибылью выше среднего заработало {company.full_profit}')
    else:
        print(f'Предприятия {company.name_buisnes} с прибылью ниже среднего заработало: {company.full_profit}')
