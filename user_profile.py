import os
import turtle
from turtle import Screen
from tkinter import *
import Variables as v
import ButtonClicks as cmd
import file_managr as fm

canvas = None


def login(index):
    v.Buttons = []
    turtle.Screen().bye()

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
    button_Setup()

def screen_setup():
    global canvas
    v.screen = Screen()
    v.screen.setup(width=1.0, height=1.0)
    canvas = v.screen.getcanvas()
    root = canvas.winfo_toplevel()
    root.overrideredirect(1)

def button_Setup():
    exit_button = Button(canvas.master, text="X", command=cmd.exit_b, height=3, width=5)
    v.Buttons.append(exit_button)

    for button in v.Buttons:
        button.pack()

    exit_button.place(x=1874, y=5)