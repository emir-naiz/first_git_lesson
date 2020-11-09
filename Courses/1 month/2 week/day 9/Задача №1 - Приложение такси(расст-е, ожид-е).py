# программа для такси (расстояние, ожидание)
sum_km = 10
wait = 2
path = int(input("Путь: "))
cost = 40
wait_status = input("Водитель, введите статус ожидания: ")
come_status = input("Введите ваш статус ожидания: ")
i = 1
while come_status != 'True':
    cost = cost + wait
    i = i + 1
    come_status = input("Введите ваш статус ожидания: ")
cost = cost + (path * sum_km)
print(cost)

