# Вход в систему использую ЛОГИЧЕСКОЕ И
login = 'username'
password = '123456'
login1 = input("Введите имя пользователя: ")
password1 = input("Введите пароль: ")

if login1 == login and password1 == password:
    print('Вы вошли в систему')
else:
    print('Не удается войти. Поажлуйста, проверьте правильность написания логина и пароляю.')