student_list = ['Emir', 'Aijan', 'Nazira', 'Baizak', 'Zarina', 'Sultan']
current_list = []
i = 0
student_len = len(student_list)
come_in = i
while come_in != '0':
    come_in = input("Введите имя студента: ")
    if come_in not in current_list: # проверяем пришел ли студент на занятия
        if come_in in student_list: # проверяем есть ли студент в общем списке
            current_list.append(come_in) # добавляем студента
            print("Студент пришел на занятия")
        else:
            print("Такого студента не существует в списке!")
    else:
        print("Студент уже пришел")

current_list_not = student_list
while i < len(current_list):
    if current_list[i] in current_list_not:
        current_list_not.remove(current_list[i])
    i += 1
print("Список присутствующих:", current_list)
print("Список отсутствующих:", current_list_not)



