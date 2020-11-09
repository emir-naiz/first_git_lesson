number = int(input())

magic_number1 = 5
magic_number2 = -5

if number > 0:
    if number == magic_number1:
        print('YES')
    else:
        print('NO')
elif number < 0:
    if number == magic_number2:
        print('YES')
    else:
        print('NO')
else:
    print(0)




