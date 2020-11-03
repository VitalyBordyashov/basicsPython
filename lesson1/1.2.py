time = int(input("Введите время в секундах"))
hour = time//3600
minute = time//60
second = time%60
if hour < 10:
    hour = str("0" + str(hour))
if minute < 10:
    minute = str("0" + str(minute))
if second < 10:
    second = str("0" + str(second))
print(f"Время составляет: {hour}:{minute}:{second}")