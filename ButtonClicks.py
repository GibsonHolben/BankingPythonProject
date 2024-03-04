import sys
import Variables as v
import file_managr as fm
import user_profile


def login():
    name_good = False
    pass_good = False
    index = 0
    v.state = 1
    input_name = v.screen.textinput('NamePrompt', "Please enter your name")
    for name in v.names:
        if name == input_name:
            print('name found')
            name_good = True
    input_pass = v.screen.textinput('PasswordPrompt', "Please enter your password")
    for passw in v.passwords:
        if passw == input_pass:
            print('password match')
            pass_good = True
        else:
            index += 1
    if name_good and pass_good:
        print('login')
        user_profile.login(index)


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
