mail = 'auidfhaweuhfoaewi Dear afhar0hf0r a09rhfa0erfh a0fhaehf[90e Sales urefherhfpesr'

spam1 = 'Sales'
spam2 = 'Dear'
sending = False

if spam1 not in mail and spam2 not in mail : # отрицаем вхождение спама в письмо
    sending = True # меняем значение переменной
    print(sending)
else:
    print('Это спам!', sending)


