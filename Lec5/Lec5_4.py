# -*- coding: utf-8 -*-
print('Задание 5.4')

# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
digit = ()
count = 0
rus_digit = ('Один', 'Два', 'Три', 'Четыре')
out_f = open("5_4_1.txt", "w")
with open('Lec5_4.txt', encoding='utf-8') as file_object:
    for line in file_object:
        arr = line.split()
        arr[0] = rus_digit[count]
        out_f.writelines(arr)
        out_f.write('\n')
        count += 1
out_f.close()
