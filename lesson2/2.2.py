s = input("Введите элементы списка через пробел")
main_list = list(s)
for el in main_list:
    if el == " ":
        main_list.remove(" ")
print(f"Мы получили список {main_list}")
i = 0
while i < len(main_list):
    n = main_list.pop(i)
    main_list.insert(i + 1, n)
    i += 2
print(f"Меняем местами соседние элементы.. и получаем {main_list}")