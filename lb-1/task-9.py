num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
result_power = num1 ** num2
result_division = result_power / num1
remainder = result_division % num1
print(f"Остаток от деления: {remainder}")