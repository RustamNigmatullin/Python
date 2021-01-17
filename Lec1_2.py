print('задание 2')

seconds = int(input('введите время в секундах: '))

print(f"Итак, {seconds} секунд это:")

print(f"В секундах {seconds}, или {seconds // 60} минут, или {seconds // 3600} часов")
print(f"Время в общепринятой форме: {seconds // 3600} часов  {(seconds % 3600)//60} минут {((seconds - 3600 * (seconds // 3600)) % 60 )} секунд")
print(f"Время в краткой форме: {seconds // 3600}:{(seconds % 3600)//60}:{((seconds - 3600 * (seconds // 3600)) % 60 )}")
