# Создайте функцию где можно добавить и удалить число.
list1 = [1,2,3,4,5,6,7,8,9,10]

def change_list(mode,number):
    if mode == 'add':
        list1.append(number)
    elif mode == 'remove' and number in list1:
        list1.remove(number)
    else:
        print('Вы ввели неверный мод!')

change_list('add',11)
change_list('remove',8)
print(list1)


