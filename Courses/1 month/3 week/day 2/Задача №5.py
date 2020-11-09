
def translator():
    print(f"Выберите правильный ответ, как переводится 'Кошка': {['cat', 'apple','guitar','cheese']}")
    answer = input("Введите ответ: ")
    if answer == 'cat':
        print("Вы ответили правильно!")
    else:
        print("Вы ответили неверно!")

translator()





