import numpy as np 
import math
from numpy import *
import matplotlib.pyplot as plt 
from fractions import Fraction 


def waveGraph():
	print('-------------------------------------')
	print('Graph for y = A.sin(p.x)')
	print('-------------------------------------')

	'''
	This will work only for int input.
	I haven't yet figured out a method to input fraction
	Once I figure out, I need to make changes at various places
	'''

	a = float(Fraction(input('Enter the value of A: ')))
	p = float(Fraction(input('Enter the value of p: ')))

	print('''Choose
1. Time in seconds
2. Angle	''')

	ch = int(input('>> '))

	if ch == 1:
		x = int(input('Enter final value of range: '))
		rad = x
		t = np.linspace(0,x)
		x_lab = 'Time in seconds'
	else:
		x = int(input('Enter the final angle in the range: '))
		rad = x * (math.pi/180)
		t = np.linspace(0,rad)
		x_lab = 'Angles in radians'

	print('''
Select:
1. Sine
2. Cosine
3. Tangent
		''')

	ch2 = int(input('>> '))

	if ch2 == 1:
		y = [a*np.sin(p*(i/rad)) for i in t]
		lab = 'Sine wave'
		v = 'sin'
	elif ch2 == 2:
		y = [a*np.cos(p*(i/rad)) for i in t]
		lab = 'Cosine wave'
		v = 'cos'
	else:
		y = [a*np.tan(p*(i/rad)) for i in t]
		lab = 'Tangent'
		v = 'tan'
	'''
	PLOTTING THE GRAPH
	'''

	plt.plot(t,y,label=lab)
	plt.title('Wave Graph:\n y = {}.{}({}.x)'.format(a,v,p))
	plt.grid()
	plt.legend()
	plt.xlabel(x_lab)
	plt.ylabel('Amplitude')
	plt.show()