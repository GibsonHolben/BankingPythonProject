import os
import tkinter
from tkinter import *
import Variables as v
import ButtonClicks as cmd
import file_managr as fm


def profile_page(index):
    v.Buttons = []

    print(v.names[index])
    v.state = 0

    path = v.home + '/Documents/PythonBank/'

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

    screen_setup()
    button_Setup(index)


def screen_setup():
    v.screen = Tk()
    v.screen.overrideredirect(True)
    v.screen.geometry("{0}x{1}+0+0".format(v.screen.winfo_screenwidth(), v.screen.winfo_screenheight()))
    v.screen.overrideredirect()


def button_Setup(index):
    exit_button = Button(v.screen, text="X", command=cmd.exit_b, height=3, width=5)
    v.Buttons.append(exit_button)
    name_display = tkinter.Label(v.screen, text=v.names[index], font=("Arial", 20))
    v.Buttons.append(name_display)
    for button in v.Buttons:
        button.pack()

    exit_button.place(x=1874, y=5)
    name_display.place(x=0, y=0)
