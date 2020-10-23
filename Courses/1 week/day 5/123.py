path = 240

v = int(input("Введите объем бензобака: ")) # Объем бензобака в данное время

result = path / 100
fuel = v - (result * 12)

if fuel > 1:
    print(f'Вы доехали до места назначения, у вас осталось: {round(fuel)} литр(а) бензина')
else:

    result1 = 100 / 12
    result1 = result1 * v
    print(f'У вас закончится бензин на {round(result1)} километре!')

