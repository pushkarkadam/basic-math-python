import numpy as np 
import matplotlib.pyplot as plt 
import math

def quadgraph(a,b,c):
	#Graph function goes here
	x = np.linspace(-20,20,1000)
	y = [a*(i**2) + b*i + c for i in x]

	plt.plot(y,x,color='r')

	plt.xlabel('X')
	plt.ylabel('Y')

	plt.title('Graphical solution for\n {}x^2 + {}x + c = 0'.format(a,b,c))
	#plt.legend()
	plt.grid()
	plt.show()

def quadsol():
	print('-----------------------------------------------')
	print('ENTER VALUES for [x^2 + x + c = 0]')
	print('-----------------------------------------------\n')
	a = int(input('Enter the co-efficient of x^2: '))
	b = int(input('Enter the co-eeficient of x: '))
	c = float(input('C: '))

	x1 = (-b + math.sqrt((b**2)-(4*a*c)))/(2*a)
	x2 = (-b - math.sqrt((b**2)-(4*a*c)))/(2*a)

	print('-----------------------------------------------')
	print('x1: {}'.format(x1))
	print('x2: {}'.format(x2))
	print('-----------------------------------------------')

	G = input('Would you like to see Graph[Y/N]:')

	if G == 'Y' or G =='y':
		quadgraph(a,b,c)