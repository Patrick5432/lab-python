n = int(input("Введите количество элементов ряда Фибоначчи: "))
fibonacci_series = [1, 1]

for i in range(2, n):
    next_number = fibonacci_series[i-1] + fibonacci_series[i-2]
    fibonacci_series.append(next_number)

print("Ряд Фибоначчи:", fibonacci_series[:n])