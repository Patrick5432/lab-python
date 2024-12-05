import random

secret_number = random.randint(1, 100)
print("Загадано число от 1 до 100. Попробуйте угадать его!")

while True:
    user_input = input("Введите ваше число (или 'exit' для выхода): ")
    if user_input.lower() == 'exit':
        print("Вы вышли из игры.")
        break
    
    guess = int(user_input)
    
    if guess < secret_number:
        print("Загаданное число больше.")
    elif guess > secret_number:
        print("Загаданное число меньше.")
    else:
        print("Поздравляем! Вы угадали число!")
        break
