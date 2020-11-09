login = input()
result_login = len(login) < 20
password = input()
result_password = len(password) < 8
print(result_login,result_password)