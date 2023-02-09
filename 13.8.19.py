
tikets = int(input("Введите необходимое количество билетов:"))
count = 0
for i in range(tikets):
    age = int(input("Введите возраст посетителя:"))
    if age < 18:
        print("Вход бесплатный")
        count = count + 0
    elif 18 <= age <= 25:
        print("Стоимость билета 990 рублей")
        count = count + 990
    else:
        print("Стоимость билета 1390 рублей")
        count = count + 1390
print("Стоимость билетов = ", count)
if tikets >= 3:
    print("Применяется скидка 10%")
    count = count * 90 / 100
    print("Итоговая сумма составила = ", count)
else:
    print("Итоговая сумма составила = ", count)
