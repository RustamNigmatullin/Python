# -*- coding: utf-8 -*-

print('Задание 5.7 (ч.1)')

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами
# и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

arr = ()
arr_dict = {}
income = 0
aver_income = 0
count = 0

with open('Lec5_7.txt', encoding='utf-8') as file_object:
    for line in file_object:
        arr = line.split()
        print('прибыль фирмы', arr[1] + ' ' + arr[0], int(arr[2]) - int(arr[3]))

        if int(arr[2]) > int(arr[3]):
            income = income + int(arr[2]) - int(arr[3])
            count = count + 1
            name = arr[0]

    aver_income = income / count
    arr_dict[name] = income
print('доход всех прибыльных фирм ', income)
print('число прибыльных фирм ', count)
print('средняя прибыль/фирму (только для прибыльных) ', aver_income)


