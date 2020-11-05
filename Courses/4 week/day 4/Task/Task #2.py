products = {'gucci boots':10000,'channel':20000,'adidas boots':8000,
            'nike sport-suit':23000,'gucci sport-suit':24000,
            'Lonsdale suit':8000,'nike boots':9000,
            'dior chest':10000,'raben waist':15000,
            'wedding dress':500000}

username = 'username'
password = 'pass12345'
def auth(login,password):
    if login == username and len(login) >= 8 and not password.isdigit() and not password.isalpha():
        return ["Вход выполнен!", login, password]
    else:
        return ["Введите правильные данные!", login, password]
print(auth('username','pass12345'))

def counter(money,price):
    if money > price:
        handing_over = money - price
        return handing_over
print(counter(10,9))

def cart():
    cart_list = []
    for i in range(2):
        product = input("Введите товар: ")
        if product in products:
            cart_list.append(product)
    return cart_list

def wallet():
    test_cart = cart()
    for line in test_cart:
        print(products[line])
        money = input("Введите сумму которая имеется:" )
        purchase = cart_list
        if money == purchase:







