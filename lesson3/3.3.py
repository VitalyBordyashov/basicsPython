def my_fanc(a,b,c):
    my_list = [a, b, c]
    m = min(my_list)
    n = my_list.index(m)
    my_list.pop(n)
    s = sum(my_list)
    return s
print(f"Сумма 2-х максимальных числе равна: {my_fanc(int(input('Введите 1 число')), int(input('Введите 2 число')), int(input('Введите 3 число')))}")
