filepath = 'user_info/students.csv'

class Student:
    def __init__(self, firstName, lastName, username, password):
        self.firstName = firstName
        self.lastName = lastName
        self.userName = username
        self.password = password


def create_new_student():
    firstName = input('Enter your first name: ')
    lastName = input('Enter your last name: ')
    username = input('Create a user name: ')
    password = input('Create a password: ')

    f = open(filepath, 'a')
    f.write(firstName + ',' + lastName + ',' + username + ',' + password + '\n')