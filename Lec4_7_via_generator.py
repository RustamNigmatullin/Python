print('Задание 7')
# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def fact(digit):
        fact = 1
        for x in range(1, digit + 1):
            fact = fact * x
            print(x, '! =', end=' ')
            yield fact
            # fact = fact * el


digit = int(input('input n: '))
for el in fact(digit):
    print(el)