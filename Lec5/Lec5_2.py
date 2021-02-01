# -*- coding: utf-8 -*-
print('Задание 5.2')

# Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

count = 0
arr = ()

with open('Lec5_2.txt', encoding='utf-8') as file_object:
    for line in file_object:
        # print(line)
        arr = line.split()
        # print('    ')
        count = count + 1
        print('количество слов в строке', count, ':', len(arr))

# пустая строка для красоты
print(' ')
print('число строк', count)

