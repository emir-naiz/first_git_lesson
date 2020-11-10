string = input()
if len(string) > 10:
    str_len = str(len(string)-2)
    result = string[0] + str_len + string[len(string)-1]
    print(result)
else:
    print(string)





