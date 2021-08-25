from starting_promt import *
from new_students import *
from login_as_student import *
from admin_login import *


def main():
    prompt()
    choice = get_starting_point()

    if choice == '1':
        create_new_student()
    elif choice == '2':
        login()
    elif choice == '3':
        admin_login()


if __name__=='__main__':
    main()