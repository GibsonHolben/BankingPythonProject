import turtle
from turtle import Screen
from tkinter import *
import Variables as v
import ButtonClicks as cmd

screen = Screen()
screen.setup(width=1.0, height=1.0)
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)

# Buttons
login_button = Button(canvas.master, text="Login", command=cmd.login, height=5, width=40)
v.Buttons.append(login_button)
exit_button = Button(canvas.master, text="X", command=cmd.exit_b, height=3, width=5)
v.Buttons.append(exit_button)

for button in v.Buttons:
    button.pack()
    
login_button.place(x=250, y=500)
exit_button.place(x=1850, y=0)

turtle.mainloop()
