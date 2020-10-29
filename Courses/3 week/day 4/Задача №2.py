# Дана строка: если она начинается с прописной буквы, преобразовать в вверхний регистр.
# Если она начинается с заглавной буквы перевести в нижний регистр.
# Если ее длина больше 10 - первую букву сделать заглавной, а все остальные прописные.
string = "emirthebestofthebest"
if not string.istitle() and len(string) < 10:
    string = string.upper()
    print(string)
elif string.istitle() and len(string) < 10:
    string = string.lower()
    print(string)
elif len(string) > 10:
    string = string.capitalize()
    print(string)



