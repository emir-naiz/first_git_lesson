list1 = [1,2,3,4,5,6] # список

def change_list(mode,number): # функция
    if mode == 'add':
        list1.append(number)
    elif mode == 'remove' and number in list1:
        list1.remove(number)
    elif mode == 'pop':
        if number > len(list1):
            print('Вы ввели слишком большое число')
    else:
        print('Вы ввели неверный мод!')

change_list('add',7)
change_list('remove',7)
change_list('pop',4)
print(list1)