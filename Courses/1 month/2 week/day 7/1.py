numbers = [1,'red',2,'yellow','green',3,5.7,10.9,[10.5,10,'lalala']]
int_list = []
float_list = []
str_list = []
i = 0
while i < len(numbers):
    if isinstance(numbers[i],str):
        str_list.append(numbers[i])
    elif isinstance(numbers[i],float):
        float_list.append(numbers[i])
    else:
        int_list.append(numbers[i])
    i += 1
print(f'Общий список {numbers}')
print(f'f Список содержащий строки: {str_list}')
print(f'Список содержащий целые числа: {int_list}')
print(f'Список содержащий дробные числа: {float_list}')

