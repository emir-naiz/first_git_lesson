try:
    number1 = int(input())
except ValueError:
    number1 = 1
try:
    number2 = int(input())
except ValueError:
    number2 = 1
print(number1+number2)