revenue = int(input("Какова выручка вашей фирмы за указанный период?"))
cost = int(input("Какова сумма издежек вашей фирмы за указанный период?"))
if revenue > cost:
    print(f"Ваша фирма работает рентабельна! Прибыль превышает издержки в {float(revenue/cost)} раз(а)")
    numberEmployees = int(input("А акова численность персонала организации?"))
    print(f"Получается на одного сотрудника приходится {round(((revenue - cost) / numberEmployees), 1)} рублей прибыли")
elif revenue == cost:
    print("Ваша фирма работает в ноль")
else:
    print("Ваша фирма работает в убыток :(")