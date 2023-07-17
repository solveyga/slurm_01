import random

propounded_number = random.randint(0, 100)

print("Число загадано!", end=" ")

for i in range(1, 9):
    print(f"Попытка №{i}:")
    users_number = int(input())
    if propounded_number == users_number:
        print("Вы выиграли!")
        break
    word = "меньше" if users_number > propounded_number else "больше"
    print(f"Неправильно! Загаданное число {word}!")
    i += 1
else:
    print("Вы проиграли!")
