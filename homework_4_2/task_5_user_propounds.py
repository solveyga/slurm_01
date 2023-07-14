upper_number = 100
under_number = 0

for i in range(1,9):
    guess_number = (upper_number - under_number) // 2 + under_number
    print(f"Попытка №{i}: Это число {guess_number}?")
    users_answer = input()
    if users_answer == '=':
        print("Ура, я победил!")
        break
    elif users_answer == '+':
        under_number = guess_number
    else:
        upper_number = guess_number
else:
    print('Я проиграл...')


