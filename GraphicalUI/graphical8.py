'''
CREATING DROP DOWN MENUS
'''

from tkinter import *

def doNothing():
	print("okay okay, I won't...")

root = Tk()

menu = Menu(root)			#Menu() is the class in tkinter
							#We put root in Menu() because we want menu to be in the main window
root.config(menu=menu)		#Well, what is the menu? It is just the parameter name
							#It says that we are configuring a menu for this piece of software we are making and that is menu
							#tkinter knows where to put the Menu
subMenu = Menu(menu)		#We created a menu option inside the menu
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo",command=doNothing)


root.mainloop()