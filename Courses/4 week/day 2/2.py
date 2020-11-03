# Функция которая перебирает все четные числа до указанного числа
def find_even_nums(number):
    even_list = []
    for i in range(1, number):
        if i % 2 == 0:
            even_list.append(i)
    return even_list

print(find_even_nums(10))