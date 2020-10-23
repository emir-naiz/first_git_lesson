# Проверка пароля и пароля подтверждения
login = input('Введите имя пользователя:')
password = input('Введите пароль:')
password_repeat = input('Подтвердите пароль:')

if password == password_repeat:
    print('Успешно!')
else:
    print('Проверьте правильность пароля')
