import sqlite3
import random

connection = sqlite3.connect('student_accounts.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS
    students(student_id INTEGER, student_first_name TEXT, student_last_name TEXT, student_username TEXT, student_password TEXT)""")


def create_student():

    student_id = random.randint(100000, 999999)
    student_first_name = input('What is your first name? ')
    student_last_name = input('What is your last name? ')
    student_username = input('Create a username: ')
    student_password = input('Create a password: ')

    print(student_id, student_first_name, student_last_name, student_username, student_password)

    cursor.execute(f"INSERT INTO students VALUES ('{student_id}', '{student_first_name}', '{student_last_name}', '{student_username}', '{student_password}')")
    
    successful_creation_message()


def successful_creation_message():
    print()
    log_in_now()
    print()


def log_in_now():
    option = input('Your account has been created. Would you like to log in now? (y/n) ')

    if option == 'y':
        print('going to the log in screen')
    elif option == 'n':
        print('See you soon.')