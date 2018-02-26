import numpy as np 
import math
from fractions import Fraction


def cart_pol():
	a = float(Fraction(input("x: ")))
	b = float(Fraction(input("y: ")))

	x = math.fabs(a)
	y = math.fabs(b)

	r = math.sqrt(x**2 + y**2)
	theta = math.atan(y/x)

	if a > 0 and b > 0:
		theta = theta + 0
	elif a < 0 and b > 0:
		theta = math.pi - theta
	elif a < 0 and b < 0:
		theta = math.pi + theta
	else:
		theta = 2*math.pi - theta

	theta_deg = theta * (180/math.pi)

	r = float("{0:.3f}".format(r))
	theta = float("{0:.3f}".format(theta))
	theta_deg = float("{0:.3f}".format(theta_deg))

	print("The polar co-ordinates are ({}, {} rad)\n OR".format(r,theta))

	print("The polar co-ordinates are ({}, {} deg)".format(r, theta_deg))