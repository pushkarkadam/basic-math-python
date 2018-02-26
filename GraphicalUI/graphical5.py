'''
BINDING FUNCTIONS TO LAYOUTS:

Let's make the the widgets actually interact with the computer programme
It is called binding a function to the widget
What it does is:
You click a button and it calls the function in the computer programme
'''

from tkinter import *

root = Tk()

def printName():
	print('Hello my name is Bond, James Bond')

'''
new PARAMETER:
command=function #Whenever using function, don't use parenthesis ()
Whenever I click this button, run a certain function

Button(root, text='',command=function)
'''

button_1 = Button(root, text='Print my name', command=printName)

button_1.pack()

root.mainloop()