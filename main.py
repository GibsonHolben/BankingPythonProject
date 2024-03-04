import os
import turtle
from turtle import Screen
from tkinter import *
import Variables as v
import ButtonClicks as cmd
import file_managr as fm

canvas = None
v.state = 0
home = os.path.expanduser('~')

path = home + '/Documents/PythonBank/'
v.users = fm.read_file(home + '/Documents/PythonBank/users.bank').split(',')
v.passwords = fm.read_file(home + '/Documents/PythonBank/pass.bank').split(',')
v.balance = fm.read_file(home + '/Documents/PythonBank/bal.bank  ').split(',')

if v.names[0] == '':
    v.names[0] = 'DEFAULT_USER'
if v.passwords[0] == '':
    v.passwords[0] = 'DEFAULT_PASS'
if v.balance[0] == '':
    v.balance[0] = '0'

# Check if the folder exists
if not os.path.isdir(path):
    # if not make one
    os.makedirs(path)


def screen_setup():
    global canvas
    v.screen = Screen()
    v.screen.setup(width=1.0, height=1.0)
    canvas = v.screen.getcanvas()
    root = canvas.winfo_toplevel()
    root.overrideredirect(1)


def button_Setup():
    login_button = Button(canvas.master, text="Login", command=cmd.login, height=5, width=40)
    v.Buttons.append(login_button)
    exit_button = Button(canvas.master, text="X", command=cmd.exit_b, height=3, width=5)
    v.Buttons.append(exit_button)

    for button in v.Buttons:
        button.pack()

    login_button.place(x=250, y=500)
    exit_button.place(x=1850, y=0)


screen_setup()
button_Setup()

turtle.mainloop()
