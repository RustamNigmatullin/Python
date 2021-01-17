print('задание 5')
income = int(input("Введите выручку фирмы "))
expences = int(input("Введите расходы фирмы "))
if income > expences:
        print("Прибыль: ", income - expences)
        employees = int(input("Введите число сотрудников фирмы "))
        print("Эффективность работы (доход на сотрудника) ", round((income - expences)/employees, 1))
else:
        print("Работа происходит в убыток")

