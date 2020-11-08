def name_fanc(name, surname, year_of_birth, city, email, tel):
    my_dict = {"имя": name, "фамилия": surname, "год рождения": year_of_birth, "город проживания": city, "email": email, "телефон": tel}
    return my_dict
print(name_fanc(name = input("Введите имя"), surname = input("Введите фамилию:"), year_of_birth = input("Введите год рождения:"), city = input("Введите город проживания:"), email = input("Введите email:"), tel = input("Введите телефон")))
