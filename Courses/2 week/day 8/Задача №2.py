#                0             1             2          3       4          5            6
day_plan = ['go to shop', 'clean house', 'cook smth', 'eat', 'walk', 'watch movie', 'wash up']
plan_len = len(day_plan)
i = 0 # счетчик
while i < plan_len:
    action = input("Введите действие: ")
    if action in day_plan:
        act_index = day_plan.index(action) # Находим индекс нашего действия
        if act_index == 0: # Действие выполняются в приоритете, нужно всегда выполнять действие которое сверху
            day_plan.remove(action) # Дело сделано, вычеркиваем из списка
            i = i + 1
        else:
            print("Не торопитесь!")
    else:
        print("Вы это не планировали!")

    print(f"Оставшиеся дела: {day_plan}")
