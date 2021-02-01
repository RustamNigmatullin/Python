# -*- coding: utf-8 -*-
import random
print('Задание 5.5')

# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
arr = ()
summa = 0

N = 10
f = open('Lec5_5.txt', 'w')
for i in range(0, N):
    f.write(str(random.randint(0, 100)) + " ")
f.close()

with open('Lec5_5.txt') as file_object:
    for line in file_object:
        arr = line.split()
        print('в файл записаны числа', arr)
        for i in range(len(arr)):
            summa = summa + int(arr[i])

file_object.close()
print('сумма всех чисел в файле', summa)