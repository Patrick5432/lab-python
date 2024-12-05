import random

secret_number = random.randint(0, 100)
attempts = 10
print("Загадано число от 0 до 100. Угадайте его за 10 попыток!")

for attempt in range(1, attempts + 1):
    guess = int(input(f"Попытка {attempt}: Введите ваше число: "))
    
    if guess < secret_number:
        print("Загаданное число больше.")
    elif guess > secret_number:
        print("Загаданное число меньше.")
    else:
        print("Поздравляем! Вы угадали число!")
        break
else:
    print(f"Вы не угадали число. Загаданное число было: {secret_number}")