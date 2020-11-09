def millionare():
    answer_list = ['Шекспир','Пушкин','Бунин','Булгаков']
    true_answer = 'Булгаков'
    print("Ответьте на вопрос: Кто написал Мастер и Маргарита?: ")
    print("Варианты ответов:", answer_list)
    help = input('Нужны ли вам подсказки?: "Да или Нет:" ')
    if help == 'Да':
        poll = input('У вас три подсказки: "50х50, Звонок другу, Помощь зала:" ')
        if poll == '50x50':
            for i in range(2):
                if answer_list[i] != true_answer:
                    answer_list.remove(answer_list[i])
            print(answer_list)
            my_answer = input("Введите свой ответ: ")
            if my_answer == true_answer:
                return "Вы победили, забирайте деньги!"
            else:
                return "Вы ответили неверно! Вылетаете"
        elif poll == "Помощь зала":
            help_list = []
            for i in range(6):
                help_answer = input("Введите ответ с зала: ")
                help_list.append(help_answer)
            print(help_list)
            my_answer = input("Введите свой ответ: ")
            if my_answer == true_answer:
                return "Вы победили, забирайте деньги!"
            else:
                return "Вы ответили неверно! Вылетаете"
        elif poll == "Звонок другу":
            call_answer = input("Введите ответ на вопрос: ")
            print(call_answer)
            my_answer = input("Введите свой ответ: ")
            if my_answer == true_answer:
                return "Вы победили, забирайте деньги!"
            else:
                return "Вы ответили неверно! Вылетаете"

print(millionare())









