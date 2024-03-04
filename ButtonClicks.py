import sys
import Variables as v
import file_managr as fm


def login():
    v.state = 1
    input_name = v.screen.textinput('NamePrompt', "Please enter your name")
    print(v.names)
    for name in v.names:
        if name == input_name:
            print('name found')


def create():
    v.state = 2
    input_name = v.screen.textinput('NamePrompt', "Please enter a name")
    pass_name = v.screen.textinput('PasswordPrompt', "Please enter a password")
    v.names.append(input_name)
    v.passwords.append(pass_name)
    v.balance.append('0')
    fm.save_data()


def exit_b():
    sys.exit(0)
