# -*- coding: utf-8 -*-
print('Задание 5.3')

# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников
count = 0
arr = ()
salary = 0
total_salary = 0
with open('Lec5_3.txt') as file_object:
    for line in file_object:
        arr = line.split()
        salary = int(arr[1])
        total_salary = total_salary + salary
        if salary > 20000:
            print('Зарплата сотрудника', arr[0], 'больше 20000 и равна', arr[1])
        count = count + 1
print('в списке', count, 'сотрудникa(ов), средняя зарплата:', round((total_salary / count), 2))


