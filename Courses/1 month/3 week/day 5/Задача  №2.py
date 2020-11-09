# 22. В форме интернет-магазина пользователю нужно ввести свой номер телефона.
# Номер телефона состоит из 10 цифр, однако некоторые пользователи вводят его в формате +996555123456,
# некоторые - 996555123456, а некоторые и вовсе вводят только 9 цифр (без первой) 555123456.
# Вам необходимо привести номер к стандарту +996555123456
number = input()

if number.startswith('996'):
    number = '+'+number
    print(number)
elif number.startswith('+996'):
    print(number)
elif not number.startswith('+996') and not number.startswith('0') and len(number) == 9:
    number = '+996'+number
    print(number)
elif number.startswith('0') and len(number) == 10:
    number = '+996' + number
    print(number)
else:
    print('Введите номер телефона в правильном формате!')




