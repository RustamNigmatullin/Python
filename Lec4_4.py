print('Задание 4')

list_0 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
list_1 = []

for el in range(len(list_0)):
    if list_0.count(list_0[el]) == 1:
       list_1.append(list_0[el])
print('list_0', list_0)
print('list_1', list_1)


