print('задание 2')

# s = ['вв', 1, -1.550, ': ', 585] // можно ли ввести так же с клавиатуры через input?
s = list(input('введите список '))
new_s = []
i = 1
while i < len(s):
        new_s.append(s[i])
        new_s.append(s[i - 1])
        i += 2
if len(new_s) < len(s):
        new_s.append(s[i-1])
print(new_s)
print("Вопрос к проверяющему: можно ли ввести так же с клавиатуры через input, как в закомментир. примере?")

