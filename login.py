from os import system
from colorama import init, Fore, Back, Style
from getpass import getpass
import stdiomask
from time import sleep

init(autoreset=True)

def show_menu():
    print(Fore.GREEN + '''  Welcome to project
    Login system
    [1] New user login
    [2] login
    [3] exit    
''')
    option = int(input('Enter yout option'))
    return (option)



def do_login():
    login = input('name: ')
    passw = stdiomask.getpass(prompt='Password: ', mask='*')
    return(login, passw)

def search_user(login,password):
    users = []
    try:
        with open('users.txt', 'r+',encoding='Utf-8', newline='' ) as file:
            for line in file:
                line = line.strip(",")
                users.append(line.split())
            for user in users:
                name = user[0]
                password = user[1]
                if login == name and password == password:
                    return True
    except FileNotFoundError:
        return False

while True:
    system ('cls')
    option = show_menu()

    if option == 1:
        login,passw = do_login()
        if login == passw:
            print("your password is the same as the user")
            passw = getpass('Password: ')
        user = search_user(login,passw)
        if user == True:
            print(Fore.RED+'Existing user')
            sleep(2)

        else:
            with open('users.txt', 'a+', encoding = 'Utf-8', newline='') as file:
                file.writelines(f'{login} {passw}\n')
            print(Fore.CYAN + 'Registration approved')
            exit()
    elif option == 2:
        login, passw = do_login()
        user = search_user(login, passw)
        if user == True:
            print(Fore.CYAN + 'Login successfully completed')
            sleep(1)
            exit()
        else:
            print(
                Fore.RED+'You may have entered your username or password wrong.\n Please check.')
            sleep(2)

    else:
        system('cls')
        print(Fore.LIGHTMAGENTA_EX + 'GoodBay')
        break