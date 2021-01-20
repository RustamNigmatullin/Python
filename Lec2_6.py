print('задание 6')
item_0 = {'key1': 1, 'key2': 2}
key1 = input('введите ключ 1, ключ 2 и тд через запятую')
for s in key1:
   print(s)
a = classmethod dict.fromkeys(item_0)

print(a)


# item_0 = {'наименование': 1, 'цена': 2, 'количество': 3, 'единица измерения': 4}
# пустой элемент
# WMonths = [ 'наименование', 'цена', 'количество']
# NumMonths = [ 'фен', 200, 5]
# F = { nm:wm for (nm,wm) in zip(WMonths, NumMonths) }
# print(F) # {12: 'Dec', 1: 'Jan', 2: 'Feb'}
#
#
# A = { 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five' }
#
# # 4. Добавить к множеству ключей числа 8, 11
# D = keys | { 8, 11 } # D = {1, 2, 3, 4, 5, 8, 11}
