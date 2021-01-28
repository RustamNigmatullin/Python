print('Задание 2')
list_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print('list_1:', list_1)
list_2 = []
list_2 = [list_1[x + 1] for x in range(len(list_1) - 1) if list_1[x + 1] > list_1[x]]
print('list_2:', list_2)