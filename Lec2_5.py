print('задание 5')

my_list = [8, 7, 6, 6, 5, 3]
s = int(input("введите число 0-9: "))
print("начальный рейтинг: ", my_list)
i = 0
while i < len(my_list):
#  находим позицию в списке, куда воткнунть введенное пользователем число, и втыкаем
   if my_list[i] < s:
      break
   else: i += 1
my_list.insert(i, s)
print("итоговый рейтинг:  ", my_list)
