my_list = [7, 5, 3, 3, 2]
print(my_list)
r = int(input("Введите рейтинг"))
if my_list.count(int(r)) >= 1:
    my_list.insert(my_list.index(int(r)) + my_list.count(int(r)), int(r))
print(my_list)
a = max(my_list)
b = min(my_list)
if r > a:
    my_list.insert(0, int(r))
elif r <= b:
    my_list.append(int(r))
else:
    i = 0
    while r < my_list[i]:
        i += 1
    print(i)
    my_list.insert(i, int(r))
print(my_list)