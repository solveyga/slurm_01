# очень красиво. Вместо моего громоздкого вычисления сразу взяли шаг и уменьшали его
number = 50
step = 50
for i in range(1, 9):
    print (f'Попытка №{i}: ', end='')
    print (f'Это число {number}?')
    char = input()
    step = round(step/2)
    if char == '=':
        print('Ура, я победил!')
        break
    elif char == '-':
        number -= step
    else:
        number += step
else:
    print('Я проиграл...')