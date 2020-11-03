import random
product_list = ['asus','acer','iphone','samsung','intel hd','nvidia',
                'adata','kingston','macbook','xiaomi','iMac','amd','apacer']
def register(login, password_input, check_password):
    register_list = []
    if password_input == check_password:
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
        for product in f2:
            if product == 'acer' or product == 'asus' or product == 'macbook' or product == 'iMac':
                file0 = open('computers.txt','w')
                file0.write(product)
            elif product == 'iphone' or product == 'samsung' or product == 'xiaomi':
                file1 = open('phones.txt','w')
                file1.write(product)
            elif product == 'intel hd' or product == 'amd' or product == 'nvidia':
                file2 = open('video_card.txt','w')
                file2.write(product)
            elif product == 'adata' or product == 'kingston' or product == 'apacer':
                file3 = open('hdd.txt','w')
                file3.write(product)
print(sort_list())





























