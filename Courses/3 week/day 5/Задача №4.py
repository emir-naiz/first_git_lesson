# У вас есть число и нужно определить какая цифра из этого числа является наибольшей.
number = '1234567'
list1 = []
for digit in number:
    list1.append(int(digit))
print(max(list1))

# У вас есть число и строки. Нужно определить какая цифра из этого числа является наибольшей.
number = '12345asdfg67'
list1 = []
for digit in number:
    if digit.isdigit():
        list1.append(digit)
print(list1)
print(number)
print(max(list1))