print('задание 4')

s = input('введите строку из нескольких не очень длинных слов (до 10 символов): ')
s = s.split()
b = 0
i = 0
while i < len(s):
        if len(s[i]) < 10:
                print(i + 1, s[i], len(s[i]))
                i += 1
        else:
                b = s[i]
                b = b[:10]
                s[i] = b
                print(i + 1, s[i], len(s[i]))
                i += 1
