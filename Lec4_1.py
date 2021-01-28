print('Задание 1')

from sys import argv
script_name, hours_sum_param, pay_per_hour_param, bonus_param = argv


print("Имя скрипта: ", script_name)
print("Выработка в часах: ", hours_sum_param)
print("Часовая ставка: ", pay_per_hour_param)
print("Премия: ", bonus_param)
print('Зарплата работника', int(hours_sum_param) * int(pay_per_hour_param) + int(bonus_param))
