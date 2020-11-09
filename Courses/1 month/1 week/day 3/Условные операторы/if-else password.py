# if-else условный оператор
password = input('Ведите пароль:')

len_password = len(password)
if len_password >= 8:
    print('Успешно')
else:
    print('Ваш пароль должен содержать больше 8 символов')