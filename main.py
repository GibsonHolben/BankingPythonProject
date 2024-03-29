import os
import tkinter
from tkinter import *
import Variables as v
import ButtonClicks as cmd
import file_managr as fm

path = v.home + '/Documents/PythonBank/'
name_input = None
password_input = None
# Check if the folder exists
if not os.path.isdir(path):
    # if not make one
    os.makedirs(path)

v.names = fm.read_file(v.home + '/Documents/PythonBank/names.bank').split(',')
v.passwords = fm.read_file(v.home + '/Documents/PythonBank/pass.bank').split(',')
v.balance = fm.read_file(v.home + '/Documents/PythonBank/bal.bank  ').split(',')

if v.names[0] == '':
    v.names[0] = 'DEFAULT_USER'
if v.passwords[0] == '':
    v.passwords[0] = 'DEFAULT_PASS'
if v.balance[0] == '':
    v.balance[0] = '0'


def screen_setup():
    v.screen = Tk()
    v.screen.overrideredirect(True)
    v.screen.geometry("{0}x{1}+0+0".format(v.screen.winfo_screenwidth(), v.screen.winfo_screenheight()))
    v.screen.overrideredirect()


def button_Setup():
    global name_input
    global password_input
    title_label = tkinter.Label(v.screen, text='Gibson Bank', font=("Arial", 20, 'bold'))
    v.Buttons.append(title_label)
    login_button = Button(v.screen, text="Login", command=login, height=2, width=6, background='white')
    v.Buttons.append(login_button)
    create_button = Button(v.screen, text="Create", command=create, height=2, width=6, background='white')
    v.Buttons.append(create_button)
    exit_button = Button(v.screen, text="X", command=cmd.exit_b, height=3, width=5)
    v.Buttons.append(exit_button)
    name_input = tkinter.Text(v.screen, height=1, width=20)
    v.Buttons.append(name_input)
    name_label = tkinter.Label(v.screen, text='Name')
    v.Buttons.append(name_label)
    password_input = tkinter.Text(v.screen, height=1, width=20)
    v.Buttons.append(password_input)
    pass_label = tkinter.Label(v.screen, text='Password')
    v.Buttons.append(pass_label)

    for button in v.Buttons:
        button.pack()
    exit_button.place(x=1874, y=5)

    lx = 850
    ly = 400
    login_button.place(x=lx, y=ly + 130)
    create_button.place(x=lx + 60, y=ly + 130)
    name_input.place(x=lx, y=ly + 50)
    name_label.place(x=lx, y=ly + 20)
    password_input.place(x=lx, y=ly + 100)
    pass_label.place(x=lx, y=ly + 70)
    title_label.place(x=850, y=100)


def login():
    name = name_input.get(1.0, END)
    passw = password_input.get(1.0, END)
    cmd.login(name, passw)


def create():
    name = name_input.get(1.0, END)
    passw = password_input.get(1.0, END)
    cmd.create(name, passw)


screen_setup()
button_Setup()

v.screen.mainloop()
