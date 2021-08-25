import pandas as pd
import numpy as np

def login():
    data = pd.read_csv('user_info/students.csv')
    usernamesCol = data.columns[-2]
    passwordsCol = data.columns[-1]
    usernames = np.array(data[usernamesCol])
    passwords = np.array(data[passwordsCol])

    logInUsername = input('Enter your username: ')
    logInPassword = input('Enter your password: ')

    for i in range(len(usernames)):
        username = usernames[i]
        if username == logInUsername:
            userMatch = True
        else:
            userMatch = False

    for i in range(len(passwords)):
        password = passwords[i]
        if password == logInPassword:
            passMatch = True
        else:
            passMatch = False

    if userMatch and passMatch:
        print('Logging in...')
    else:
        print('Incorrect username or password.')
