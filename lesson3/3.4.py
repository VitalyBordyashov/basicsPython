def my_fanc():
    x = int(input("Введите число x"))
    y = int(input("В какую степень со знаком минус вы хотите возвести его, введите y без минуса"))
    i = 1
    s = 1
    if y == 0:
        print(f"Значение {x} в степени {-y} равно 1")
    while i <= abs(y):
        s = s * x
        i += 1
    print(1/s)
my_fanc()

