def setify(number_list):
    number_list.sort()
    empty_list = []
    for number in empty_list:
        if number not in empty_list:
            empty_list.append(number)
    return empty_list

print(setify(1,2,3,3,4,4,6,6,5,5))

print(set(([1,2,3,3,4,4,6,6,5,5]))) # при помощи set можно удалить дублирующие цифры