# Найдите максимум трех чисел с помощью функции
def max_of_three(number1,number2,number3):
    max1 = max(number1,number2)
    max2 = max(max1,number3)
    print(max2)

max_of_three(1,10,7)

# Найдите максимум четырех чисел с помощью функции
def max_of_three(number1,number2,number3,number4):
    max1 = max(number1,number2)
    max2 = max(number3,number4)
    max3 = max(max1,max2)
    print(max3)

max_of_three(1,10,7,20)

# Найдите минимум четырех чисел с помощью функции
def min_of_three(number1,number2,number3,number4):
    max1 = min(number1,number2)
    max2 = min(number3,number4)
    max3 = min(max1,max2)
    print(max3)

min_of_three(1,10,7,20)


