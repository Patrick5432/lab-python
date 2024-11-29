numbers = []
for i in range(4):
    number = int(input(f"Введите целое число {i + 1}: "))
    numbers.append(number)
max_number = max(numbers)
print(f"Максимальное число: {max_number}")
