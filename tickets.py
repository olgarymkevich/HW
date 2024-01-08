amount = 0
tickets = int(input("Введите количество билетов: "))
for age in range(tickets):
    age = int(input("Введите ваш возраст: "))
    if age < 18:
        amount += 0
    elif 18 <= age < 25:
        amount += 990
    elif age >= 25:
        amount += 1390

discount = amount*10/100
amount_1 = amount - discount
if tickets <= 3:
    print("Сумма к оплате: ", int(amount), "руб.")
else:
    print("Сумма к оплате: ", int(amount_1), "руб.")