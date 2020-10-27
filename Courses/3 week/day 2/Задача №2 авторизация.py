# авторизация
username = 'user'
password = '123456'

def login(login,check_password):
    if login == username and check_password == password:
        return login, check_password
    else:
        return "Вы ввели неверные данные"

print (login('user','123456'))



