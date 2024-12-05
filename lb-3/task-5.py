import math

num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))
gcd = math.gcd(num1, num2)
print(f"Наибольший общий делитель чисел {num1} и {num2} равен {gcd}")