import sys
import Variables as v


def login():
    v.state = 1
    input_name = v.screen.textinput('NamePrompt', "Please enter your name")


def create():
    v.state = 2


def exit_b():
    sys.exit(0)
