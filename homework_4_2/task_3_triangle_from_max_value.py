users_number = int(input())

max_value = 1
for i in range(1,users_number+1):
    max_value = max_value + i

for i in range(users_number):
    for j in range(i+1):
        max_value = max_value-1
        print(max_value, end=' ')
    print()