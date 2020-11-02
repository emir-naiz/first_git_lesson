def factorial(number):
    i = 1
    result = 1
    while i <= number:
        result = result * i
        i = i + 1
    return result
print(factorial(5))


def factorial(number):
    result = 1
    for i in range(1,number+1):
        result = result * i
    return result
print(factorial(5))
