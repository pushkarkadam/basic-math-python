'''
USING CLASSES
'''

from tkinter import *


class BuckysButton:

	def printMessage(self):
		print("Wow, this actually works!")

	def __init__(self, master):		#anytime you see "master" it means the main window
		frame = Frame(master)		#We created a Frame in the main window
		frame.pack()				#display on the screen to place it in there
		'''
		Anytime you want to create a button variable,
		we will set it equal to self
		'''
		self.printButton = Button(frame, text="Print Message", command = self.printMessage) 	#Something that you clikc and it prints something in terminal
		self.printButton.pack(side=LEFT)

		self.quitButton = Button(frame, text="Quit", command = frame.quit)  # frame.quit is already a built in function in tkinter
																			#It breaks the main loop
		self.quitButton.pack(side=LEFT)


root = Tk()
'''
Whenever we want to use something from the class, we need an OBJECT
Object allows us to acess the stuff inside the class
'''
b = BuckysButton(root)		#We pass in the root window which gets treated as "master"

root.mainloop()