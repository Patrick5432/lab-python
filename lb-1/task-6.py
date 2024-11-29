temperature = float(input("Введите температуру воды (в градусах Цельсия): "))

if temperature < 0:
    state = "твердое"
elif 0 <= temperature <= 100:
    state = "жидкое"
else:
    state = "газообразное"

print(f"При температуре {temperature}°C вода находится в {state} состоянии.")
