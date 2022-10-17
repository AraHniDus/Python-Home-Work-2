num = float(input("Введите число: "))
sum = 0
for i in str(num):
    if i != ".":
        sum += int(i)
print("Сумма цифр числа равна: ", sum)
