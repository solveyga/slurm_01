# считывание введенного значения и перевод в int
value = int(input())
# счетчик
row_count = 1
# список, в который будут записываться значения каждой строки
row = []

# для счетчика в области, где start = 2value - sum(0,value-1), end = 0, step = -1. Зачем именно такой старт?
for i in range(value ** 2 - sum(range(value)), 0, -1):
    row.append(i)
    if len(row) == row_count:
        # line - строка, состоит из всех элементов row, разделенных пробелом
        line = ' '.join(map(str, row))
        # вывод line с выравниванием 3value справа
        print(f'{line:>{value * 3}}')
        # очищение row
        row = []
        # увеличение счетчика
        row_count += 1