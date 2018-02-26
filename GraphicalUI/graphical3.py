'''
FITTING WIDGETS IN YOUR LAYOUT
'''
from tkinter import * 

root =Tk()

one = Label(root,text="One",bg="red",fg="white")		#bg ==> Background (Background with red on the label)
														#fg ==> Foreground (text with white on the label)
one.pack()
two = Label(root,text="Two",bg="green",fg="black")
two.pack(fill=X)			#Right now we have a label and by default it's going to be the size
							#If we put X and if we change the window size, it will grow
three = Label(root,text="Three",bg="blue",fg="white")
three.pack(side=LEFT, fill=Y)

root.mainloop()