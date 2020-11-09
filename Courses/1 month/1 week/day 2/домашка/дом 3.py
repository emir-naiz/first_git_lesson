# Найти сумму цифр трехзначного числа
number = int(input())
hund = number // 100  # ищем кол-во сотен
print (hund)
tens = number // 10 % 10 # ищем кол-во десятков
print (tens)
digits = number % 100 % 10 # ищем кол-во единиц
print (digits)
print (hund + tens + digits)