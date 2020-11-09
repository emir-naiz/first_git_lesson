strings = ['hello Emma, how are u?',
           'Dear Emma, please fix production',
           'SALES lining sales','buy right now dont lose your chance',
           'Emma help me please','Emma SOS production is down']

def write_to(strings):
    with open('email.txt', 'w') as file1:
        for mail in strings:
            file1.write(mail.lower() + '\n')

def open_file(filename, text):
    with open(filename, 'a') as file2:
        file2.write(text.capitalize())

write_to(strings)

def sort_mail():
    with open('email.txt') as file3:
        mail_list = file3.readlines()
        for mail in mail_list:
            if mail.startswith('sales') or mail.startswith('buy right now'):
                open_file('spam.txt', mail)
            elif mail.startswith('dear') or 'help' in mail or 'sos' in mail:
                open_file('work_email.txt', mail)
            else:
                open_file('emma.txt', mail)
sort_mail()























