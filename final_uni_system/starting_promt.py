banner = '***************************************'
def prompt():
    print()
    print()
    print(banner)
    print('Welcome. What would you like to do?')
    print('1. Create a new student account')
    print('2. Log in as a student')
    print('3. Log in as admin')
    print(banner)
    

def get_starting_point():
    choice = input('Enter your option: ')
    print()
    print()
    return choice