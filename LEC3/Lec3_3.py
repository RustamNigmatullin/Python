print('Задание 3')


def m_func(var_1, var_2, var_3):
    if var_1 == var_2 or var_1 == var_3 or var_2 == var_3:
        print('есть одинаковые числа! расчет будет выполнен')
    s = (var_1 + var_2 + var_3) - min(var_1, var_2, var_3)
    return s


first_arg = int(input('Введите первое число: '))
sec_arg = int(input('Введите второе число: '))
third_arg = int(input('Введите третье число: '))

print ('сумма наибольших двух чисел: ', m_func(first_arg, sec_arg, third_arg))
