print('Задание 5')

summa = 0

while True:
    txt = input('введите числа через пробел, для выхода <q>')
    if 'q' in txt:
        new_txt = txt.split()
        new_txt.pop()
        for el in new_txt:
            el = int(el)
            summa = summa + el
        break
    else:
        new_txt = txt.split()
        for el in new_txt:
            el = int(el)
            summa = summa + el
        print('Сумма промежуточная', summa)
print('Сумма финальная', summa)