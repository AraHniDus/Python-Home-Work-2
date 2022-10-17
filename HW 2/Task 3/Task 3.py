sp = input('Введите предложение - ')
sp1 = input('Введите находимый элимент - ')
count = 0
for i in sp:
    if i == sp1:
        count = count + 1
print ('Количество находимых элиментов в предложении - ' + str(count))
