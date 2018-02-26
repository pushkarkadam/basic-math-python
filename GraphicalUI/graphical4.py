'''
GRID LAYOUT
'''

from tkinter import *

root = Tk()

label_1 = Label(root,text='Name')
label_2 = Label(root,text='Password')
entry_1 = Entry(root)   #It tells the user what it needs, basically, it's like taking an i/p
						#It takes the parameter root, because we want it in the main window
entry_2 = Entry(root)

'''
Everything works like EXCEL
there are rows and columns
Thus, we don't use .pack()
instead we will be using .grid()
.grid(row='', column='') takes two parameters

columnspan=2 ==> it will take two columns

column is by defaut 0

PARAMETER: 
sitcky='E'
E = East
W = West
N = North
S = South
'''

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)

entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

c = Checkbutton(root, text='Keep me logged in')
c.grid(columnspan=2)

root.mainloop()