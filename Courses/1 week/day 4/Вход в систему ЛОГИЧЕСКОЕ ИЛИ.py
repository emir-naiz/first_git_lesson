# Вход в систему ЛОГИЧЕСКОЕ ИЛИ
phone = '0704507705' # наш телефон
email = 'user@name.com' # наша эл.почта
password = '123456' # пароль

check_input = input("phone или email: ") # выбираем что вводить
if check_input == 'phone':
    phone_check = input("Введите телефон: ") # вводим телефон
    password_check = input("Введите пароль: ")
    if phone_check == phone and password_check == password:
        print('Вы вошли в ссистему')
    else:
        print('Вы ввели неверные данные')
elif check_input == 'email':
    email_check = input("Введите E-Mail: ") # вводим эл.почту
    password_check = input("Введите пароль: ")
    if email_check == email and password_check == password:
        print('Вы вошли в систему')
    else:
        print('Вы ввели неверные данные')




