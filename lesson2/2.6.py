def entering_values():
    new_dict = {"Название": input("Введите название товара"), "Цена": input("Введите цену товара"), "Количество": input("Введите количество товара"), "Единица измерения": input("И единицу измерения")}
    return new_dict
a_1 = entering_values()
a_2 = entering_values()
a_3 = entering_values()
print(f"Товар 1: {a_1}")
print(f"Товар 1: {a_2}")
print(f"Товар 1: {a_3}")
name_list = [a_1.get("Название"), a_2.get("Название"), a_3.get("Название")]
print(f"Названия товаров: {name_list}")
price_list = [a_1.get("Цена"), a_2.get("Цена"), a_3.get("Цена")]
print(f"Цены товаров: {price_list}")
quantity_list = [a_1.get("Количество"), a_2.get("Количество"), a_3.get("Количество")]
print(f"Количество товаров: {quantity_list}")
unit_list = [a_1.get("Единица измерения"), a_2.get("Единица измерения"), a_3.get("Единица измерения")]
for el in unit_list:
    if unit_list.count(el) > 2:
        unit_list = [a_1.get("Единица измерения")]
    elif unit_list.count(el) > 1:
        unit_list.remove(el)
print(f"Единицы измерений товаров: {unit_list}")