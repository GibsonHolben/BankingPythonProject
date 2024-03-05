import sys
import tkinter

import Variables as v
import file_managr as fm
import user_profile


def login(input_name, input_pass):
    name_good = False
    pass_good = False
    index = 0
    v.state = 1
    for name in v.names:
        if name == input_name:
            print('name found')
            name_good = True
    for passw in v.passwords:
        if passw == input_pass:
            print('password match')
            pass_good = True
        else:
            index += 1
    if name_good and pass_good:
        print('profile_page')
        user_profile.profile_page(index)


def create(input_name, input_pass):
    v.state = 2
    v.names.append(input_name)
    v.passwords.append(input_pass)
    v.balance.append('0')
    fm.save_data()
    name_label = tkinter.Label(v.screen, text='Created a user named: ' + input_name, font=("Arial", 50))
    name_label.pack()


def exit_b():
    sys.exit(0)
