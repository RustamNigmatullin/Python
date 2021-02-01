print('Задание 5.1')

# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

my_file = open('5.1.txt', 'w')
while True:
    txt_input = input('введите строку')
    my_file.write(txt_input + '\n')
    if txt_input == '':
        txt_input = False
        break
