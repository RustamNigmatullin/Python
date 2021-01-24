print('Задание 1')


def func_first(var_1, var_2):
    try:
        return round(var_1/var_2)
    except ZeroDivisionError:
        return 'Деление на ноль, ошибка'


first_num = int(input('Введите первое число '))
second_num = int(input('Введите второе число '))
print('Результат:', func_first(first_num, second_num))