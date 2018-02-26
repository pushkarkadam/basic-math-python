from tkinter import *			# * stands for importing everything

root = Tk()			#root object is going to be equal to Tk()==> tkinter class
					#So, everytime you see root think of a blank window
thelabel = Label(root, text="This is too easy") 
					#basic text is called "label", Label() object is used
					#first parameter : where to put this label i.e. Blank window
					#second parameter : what you want to write i.e. Text
thelabel.pack()  	#wherever it is pack it in the first place you see it
root.mainloop()		#root is the tkinter object which holds all your widgets
'''
Whenever you have a GUI application you need that window continuously
on screen before you close it
what mainloop() does is that it puts it in a continuos loop 
unless you press the close button
'''