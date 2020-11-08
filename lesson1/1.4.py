integer = int(input("Введите целое число:"))
maxNamber = int(integer % 10)
S = int(integer // 10)
while S != 0:
    if S % 10 > maxNamber:
        maxNamber = S % 10
    S = S // 10
print(f"Максимальная цифра в вашем01264 числе: {maxNamber}")