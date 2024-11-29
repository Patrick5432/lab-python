import math

def f(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2
    else:
        return None

a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))
array = f(a, b, c)
if array is not None:
    print(f"Вывод: первый корень: {array[0]}, второй корень: {array[1]}")
else:
    print(f"Дискриминант меньше или равен нулю")