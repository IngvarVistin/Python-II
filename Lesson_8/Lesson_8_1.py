'''
1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
'''

import hashlib

string = (input('Введите строку из латинских букв: ')).lower()

sum_substr = set()

for i in range(len(string)):
    for j in range(len(string), i, -1):
        hash_str = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
        sum_substr.add(hash_str)
print(sum_substr)

print(f'{len(sum_substr) -1} различных подстрок в строке {string}')