string = 'File not found'
str_count = string.count('f')
if str_count == 1:
    print(string.count('f'))
elif str_count >= 2:
    print(string.find('f'), string.rfind('f'))
elif str_count == 0:
    print('No f')


