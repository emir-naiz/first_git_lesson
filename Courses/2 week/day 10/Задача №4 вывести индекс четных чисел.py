# Вывести индекс четных чисел
task_list = ['yellow', 'red', 'blue', 'green', 'brown']
i = 0
while i < len(task_list):
    if i % 2 == 0:
        print(f"Четный список {i}: ", task_list[i])
    i = i + 1


