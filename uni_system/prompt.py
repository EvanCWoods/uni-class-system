from create_student import *

banner = '*****************************'
def prompt():
    print()
    print(banner)
    print()
    print('Welcome. What would you like to do?')
    print()
    print('1. Create a student account')
    print('2. Log in as admin')
    print()
    get_choice()
    print()
    print(banner)


def get_choice():
    choice = int(input('Enter the your choice (number): '))

    if choice == 1:
        create_student()
    elif choice == 2:
        print('logging in as admin...')