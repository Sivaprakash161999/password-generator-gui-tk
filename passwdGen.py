# import tkinter module for gui
from tkinter import *
# importing pyperclip module to use it to copy our generated
# password to clipboard
import pyperclip
# import random module for password generation
import random

# initializing tkinter
root = Tk()

# setting width and height of the gui
root.geometry("400x400")

# declaring variable of string type and this will be
# used to store the password generated
passstr = StringVar()

# declaring a varilable of integer type which will be
# used to store the length of the password entered by the user
passlen = IntVar()

# setting the length of the password to zero initially
passlen.set(0)

# function to generate the Password
def generate():
    # storing the keys in a list which will be used
    # to generate the password
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    Alpha = alpha.upper()
    numerals = '0123456789'
    special_char = '!@#$%^&*()'
    pass1 = list(alpha) + list(Alpha) + \
            list(numerals) + list(special_char)
    # print(pass1)

    # declaring the empty string
    password = ""

    # loop to generate the random password of the length
    # entered by the user
    for x in range(passlen.get()):
        password = password + random.choice(pass1)

    # setting the password to the entry widget
    passstr.set(password)

# function to copy to clipboard
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)


### Designing our gui layout

# creating a text label widget for header
Label(root, text = "Password Generator Application",
        font = "Calibri 20 bold").pack()

# creating a text label widget for asking user input for
# password length
Label(root, text = "Enter password length").pack(pady = 3)

# creating a entry widget to take password length entered by the
# user
Entry(root, textvariable = passlen).pack(pady = 3)

# button to call the generate function
Button(root, text = 'Generate Password',
            command = generate).pack(pady = 7)

# Entry widget to show the generated password
Entry(root, textvariable = passstr).pack(pady = 3)

# button to call the copytoclipboard function
Button(root, text = "Copy to clipboard", command = copytoclipboard).pack()

# mainloop() is an infinite loop used to run the application when
# it's in ready state
root.mainloop()
