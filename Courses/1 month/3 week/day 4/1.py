text = "Помню пили мы не лимонад, запотевали бокалы вина,время"

check = text.find("время")
if check > 0:
    print('Есть это слово!')
elif check < 0:
    print('Этого слово там нет!')

