# -*- coding: utf-8 -*-
import json

print('Задание 5.7(ч2)')

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами
# и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

arr = ()
arr_dict = {}
arr_dict_profitable = {}
income = 0
aver_income = 0
count = 0
list_firms = []

with open('Lec5_7.txt', encoding='utf-8') as file_object:
    for line in file_object:
        arr = line.split()
        name_0 = arr[0]
        income_0 = int(arr[2]) - int(arr[3])
        arr_dict[name_0] = income_0

        if int(arr[2]) > int(arr[3]):
            income = income + int(arr[2]) - int(arr[3])
            count = count + 1
            name = arr[0]

    aver_income = income / count
    arr_dict_profitable['average profit'] = aver_income
list_firms.append(arr_dict)
list_firms.append(arr_dict_profitable)

print(list_firms)
with open('my_json', 'w') as my_file:
    json.dump(list_firms, my_file)
