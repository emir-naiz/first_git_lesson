# exceptions
try:
    string = '1'
    number = 1
    print(string+number)
except TypeError:
    print('error')


list1 = [1,2,3,4]
try:
    for i in range(10):
        print(list1[i])
except IndexError:
    print('Вы вышли за грань списка!')