import random

def guess_the_number():
    # Компьютер загадывает случайное число от 1 до 100
    secret_number = random.randint(1, 100)
    print("Я загадал число от 1 до 100. Попробуй его угадать!")
    
    # Переменная для хранения количества попыток
    attempts = 0
    
    while True:
        # Игрок вводит своё предположение
        guess = int(input("Введите ваше предположение: "))
        
        attempts += 1
        
        if guess == secret_number:
            print(f"Поздравляю! Вы угадали число {secret_number} с {attempts} попыткой.")
            break
        elif guess < secret_number:
            print("Ваше число меньше загаданного. Попробуйте ещё раз.")
        else:
            print("Ваше число больше загаданного. Попробуйте ещё раз.")
            
# Запускаем игру
guess_the_number()