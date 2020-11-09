import random
product_list = ['asus','acer','iphone','samsung','intel hd','nvidia',
                'adata','kingston','macbook','xiaomi','iMac','amd','apacer']
def register(login, password_input, check_password):
    register_list = []
    if password_input == check_password:
        global code
        code = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
        register_list.append(login)
        register_list.append(password_input)
        return register_list
    else:
        return "Пароли не совпадают!"
user = register('user','123456','123456')
username = user[0]
password = user[1]
print(username,password)




def auth(login, check_password):
    if login == username and check_password == password:
        return ["Вход выполнен!",login, check_password]
    else:
        return "Вы ввели неверные данные"
print(auth('user','123456'))


def write_to(product_list):
    with open('product_list.txt', 'w') as file1:
        for product in product_list:
            file1.write(product + '\n')
write_to(product_list)


def sort_list():
    with open('product_list.txt') as file2:
        f2 = file2.readlines()
        print(f2)
        for product in f2:
            product = product.strip()
            if product == 'acer' or product == 'asus' or product == 'macbook' or product == 'iMac':
                file0 = open('computers.txt', 'a')
                file0.write(product + '\n')
            elif product == 'iphone' or product == 'samsung' or product == 'xiaomi':
                file1 = open('phones.txt', 'a')
                file1.write(product + '\n')
            elif product == 'intel hd' or product == 'amd' or product == 'nvidia':
                file2 = open('video_card.txt', 'a')
                file2.write(product +'\n')
            elif product == 'adata' or product == 'kingston' or product == 'apacer':
                file3 = open('hdd.txt', 'a')
                file3.write(product + '\n')
sort_list()


def activate(our_code,code):
    if our_code == code:
        print('Все хорошо!')
    else:
        print('Неверный код!')
print('Код, пришедший на почту',code)
our_code = list(input("Введите код для активации аккаунта: "))
true_code = []
for line in code:
    true_code.append(str(line))
activate(our_code, true_code)


def open_file(filename:str):
    with open(filename) as f1:
        f1_read = f1.read()
        return f1_read
user_input = input("Вариант фильтрации: computers, phones, video_card, hdd: ")


def screen_input(user_input):
    if user_input == 'computers':
        print(open_file('computers.txt'))
    elif user_input == 'phones':
        print(open_file('phones.txt'))
    elif user_input == 'video_card':
        print(open_file('video_card.txt'))
    elif user_input == 'hdd':
        print(open_file('hdd.txt'))
screen_input(user_input)







































