import os

Buttons = []

# States are as follows:
#     0 = Main Menu
#     1 = Login Screen
#     2 = Create Screen
#     3 = Admin Screen
state = 0


passwords = ['TEST_PASS']
names = ['TEST_NAME']
balance = ['0']
screen = None
home = os.path.expanduser('~')
