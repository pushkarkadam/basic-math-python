import numpy as np 
import matplotlib.pyplot as plt 
import math
pi = math.pi

theta = np.linspace(0,2*pi)

def first_function():
	print('-----------------------------------------------------------------')
	print('Enter the values for |C + A.sin(B*theta)| OR |C + A.cos(B*theta)|')
	print('-----------------------------------------------------------------')
	c = int(input('C: '))
	a = int(input('A: '))
	b = int(input('B: '))
	d = int(input('1. Sine\n2. Cosine\n>> '))
	if d == 1:
		r = [c + a*math.sin(b*i) for i in theta]
	else:
		r = [c + a*math.cos(b*i) for i in theta]

	ax = plt.subplot(111, projection='polar')
	ax.plot(theta,r)
	ax.grid(True)
	plt.show()

def square_function():
	print('-----------------------------------------------------------------')
	print('Enter the values for |A.(sin(B*theta))^n| OR |A.(cos(B*theta))^n|')
	print('-----------------------------------------------------------------')

	a = int(input('A: '))
	b = int(input('B: '))
	n = int(input('n: '))
	d = int(input('1. Sine\n2. Cosine\n>> '))

	if d == 1:
		r = [a*(math.sin(b*i))**2 for i in theta]
	else:
		r = [a*(math.cos(b*i))**2 for i in theta]

	ax = plt.subplot(111, projection='polar')
	ax.plot(theta,r)
	ax.grid(True)
	plt.show()

def polar_function():
	print('''
Select the following choices
--------------------------------------------------------------------------
1. Power of one
	|C + A.sin(B*theta)| OR |C + A.cos(B*theta)| 
--------------------------------------------------------------------------
2. Square functions
	|A.(sin(B*theta))^n| OR |A.(cos(B*theta))^n|
--------------------------------------------------------------------------
		''')
	x = int(input('>> '))

	if x == 1:
		first_function()
	else:
		square_function()