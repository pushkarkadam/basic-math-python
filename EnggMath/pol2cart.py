import numpy as np 
import math
from fractions import Fraction 


def pol_cart():
	r = float(Fraction(input("r: ")))

	print('''
-----------------------------------
Select:
1) Degree
2) Radians	
-----------------------------------''')

	c = int(input(">> "))

	if c == 1:
		theta_in = float(input("theta (degrees): "))
		theta = theta_in * (math.pi/180)
	else:
		theta_in = float(input("theta (radians): "))
		theta = theta_in

	x = r*math.cos(theta)
	y = r*math.sin(theta)

	x = float("{0:.3f}".format(x))
	y = float("{0:.3f}".format(y))

	print('''Hence, ({}, {} degrees) in polar corresponds to ({},{}) 
in Cartesian co-ordinates.'''.format(r, theta_in, x, y))