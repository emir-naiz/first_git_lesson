# сортировка четных и нечетных чисел
numbers = [1,9,2,4,7,12,18,22]
prime_numbers = []
non_prime_numbers = []

i = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        prime_numbers.append(numbers[i])
    else:
        non_prime_numbers.append(numbers[i])
    i += 1
print(f'Общий список {numbers}')
print(f'Список с четными числами: {prime_numbers}')
print(f'Список с нечетными числами: {non_prime_numbers}')


