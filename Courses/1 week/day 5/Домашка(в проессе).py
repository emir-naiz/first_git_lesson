path = 240 # расстояние до местоназна-е

bmwx5 = 20 # расход на 100 км
mercedes220 = 18 # расход на 100 км
hondafit = 9 # расход на 100 км

fuel = int(input("Введите объем бензобака: "))

result = path / 100

car = input(f'Введите свое авто: ')

if car == "hondafit":
     fuel = fuel - (result * hondafit)
     print (f"Вам не хватило : {fuel} литр(а) бензина")
     result = 100 / hondafit
     result = result * hondafit
     print(f'У вас закончится бензин на {round(result)} километре!')
elif car == "mercedes220":
     fuel = fuel - (result * mercedes220)
     print (f"Вам не хватило: {round(fuel)} литр(а) бензина")
elif car == "bmwx5":
     fuel = fuel - (result * bmwx5)
     print (f"Вам не хватило: {round(fuel)} литр(а) бензина")



