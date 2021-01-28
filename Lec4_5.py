print('Задание 5')
from functools import reduce

list_0 = list(range(100, 1001, 2))
print('list_0', list_0)
print('произведение элементов: ', reduce(lambda x, y: x * y, list_0))
