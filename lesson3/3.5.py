def my_fanc():
    my_list = input("Введите числа через пробел")
    new_list = my_list.split(" ")
    for el in new_list:
        if el == " ":
            new_list.remove(" ")
    print(f"Мы получили список {new_list}")
    n = 0
    s = 0
    while n < len(new_list):
        s += int(new_list[n])
        n += 1
    return s
    print(s)
my_fanc()
"""
        elif el == " " and el == "+":
            my_list.remove(" ")
            my_list.remove("+")
        print(f"Мы получили список {my_list}")
            n = 0
            s = 0
            while n < len(my_list):
                s += int(my_list[n])
                n += 1
            return s
            s += s
        print(my_fanc())
"""