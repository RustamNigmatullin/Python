print('Задание 2')


def func_first(var_1, var_2, var_3, var_4, var_5, var_6):
    res = (f"Фамилия: {var_2}; Имя: {var_1}; год рождения: {var_3}; город: {var_4}; почта: {var_5}, телефон: {var_6}")
    return res

name_param = input('Введите имя ')
surname_param = input('Введите фамилию ')
birthyear_param = input('Введите год рождения ')
city_param = input('Введите город проживания ')
email_param = input('Введите e-mail ')
phone_param = input('Введите телефон ')

print('Запись:', func_first(var_1=name_param, var_2=surname_param, var_3=birthyear_param, var_4=city_param, var_5=email_param, var_6=phone_param))