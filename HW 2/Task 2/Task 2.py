N = int(input('Введите число: '))
list = []
def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)
for e in range(1, N + 1):
    list.append(mult(e))

print(f"Произведения чисел от 1 до {N}:  {list}")



