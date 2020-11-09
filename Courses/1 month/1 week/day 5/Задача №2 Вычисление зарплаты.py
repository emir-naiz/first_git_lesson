# Вычисление зар.платы
hour_salary = 70
salary = 0 # Начальная зарплата
work = int(input("Введите кол-во часов работы: "))

work_day = 8 # Рабочий день

if work > 1 and work <= 24:
    if work > work_day:
        # Кол-во часов переработки
        check = work - work_day
        # Зарплата включающая двойную ставку за переработанное время
        salary = (work_day * hour_salary) + ((check * hour_salary)*2)
        print(f'Ваша зарплата за сегодня: {salary}$')
    else:
        # счиатем зарплату
        salary = hour_salary * work
        print(f'Ваша зарплата за сегодня: {salary}$')
else:
    print('Ты врешь, ничего не получишь!')