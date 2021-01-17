print('задание 3')

s = int(input('введите номер месяца (1-12) '))
if s >= 1 and s <= 12:
        print("Через список: ")
        calendar = ["зима", "весна", "лето", "осень"]
        if s == 1 or s ==2 or s == 12:
                print(calendar[0])
        elif s > 2 and s < 6:
                print(calendar[1])
        elif s > 5 and s < 9:
                print(calendar[2])
        elif s > 8 and s < 12:
                print(calendar[3])

        print("Через словарь: ")
        cal_dict = {12: "Зима", 1: "Зима", 2:"Зима",
                    3: "Весна", 4: "Весна", 5: "Весна",
                    6: "Лето", 7: "Лето", 8: "Лето",
                    9: "Осень", 10: "Осень", 11: "Осень"}
        print(cal_dict.get(s))
else:
        print("Digit is out of range")