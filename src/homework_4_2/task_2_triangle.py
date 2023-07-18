users_number = int(input())
printed_number = 0

for i in range(users_number):
    for j in range(i + 1):
        printed_number += 1
        print(printed_number, end=" ")
    print()
