# if-else условный оператор
username = input('Ведите имя пользователя:')

len_username = len(username)
if len_username > 20:
    print('Кол-во букв превышает больше 20 символов')
else:
    print('Продолжайте регистрироваться дальше')
