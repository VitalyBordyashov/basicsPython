def my_fanc():
    main_str = input("Введите числа через пробел")
    s = main_str.split(" ")
    print(s)
    summa = 0
    for el in s:
        if el == " ":
            s.remove(el)
        n = int(el)
        summa = summa + n
    print(f"Сумма ваших числе равна: {summa}")
my_fanc()
