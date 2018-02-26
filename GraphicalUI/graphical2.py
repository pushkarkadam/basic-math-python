'''
from tkinter import * 

root =Tk() 			#We will need the main window

//[Some code will be coming here]//

root.mainloop()			#We will need the display on screen

These commands are going to be the basic framework for GUI

'''

from tkinter import * 

root = Tk()    #we will need main window

'''
A Frame:
Think of  a frame as an invisible layout in which you could
put things in.
'''
topFrame = Frame(root)	#It's like saying I am going to make an invisible window and
						#it's going to go in the main window
topFrame.pack()			#Anytime we want to display, we need to pack it in
						#something like saying "Place it in the main window somewhere"
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)		#However there is parameter that says where you want to pack it
									#in main window

button1 = Button(topFrame, text='Button 1',fg='red')		#Object name is Button() to create buttons
															#it is going to take some parameter
															#First parameter ==> position i.e. where the button needs to be placed, either in top or bottom frame
															#Second parameter ==> text i.e. the value of the button, the text represented on the button
															#Third parameter ==> color. It is optional. It gives color to the button [On MAC OS I haven't been able to see colour]
button2 = Button(topFrame, text='Button 2',fg='blue')
button3 = Button(topFrame, text='Button 3',fg='green')
button4 = Button(bottomFrame, text='Button 4',fg='purple')

'''
Creating a GUI is a two step process:
1. you need to create them i.e. button1 = Button()
2. you need to display them
'''
button1.pack(side=LEFT)			#By default, whenever you pack things, they get packed on top of each other
								#Parameter side=LEFT ==> It says that pack the button1 on the far left as possible
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop() #We will need display on the screen