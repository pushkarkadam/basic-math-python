import numpy as np 
import math
import matplotlib.pyplot as plt 
from fractions import Fraction

T = 40
t = np.linspace(0,T)


#print(t)

v = [ 340*math.sin(50*math.pi*(i/T) - 0.541) for i in t]

v1 = [340*math.sin(50*math.pi*(i/T)) for i in t]

#print(v)
#print(v1)

print('Determine the voltage:')

V = float(Fraction(input(">> ")))

t_new = (math.asin(V/340)+0.541)/(50*math.pi)

t_ms = t_new * 1000

print("The time at voltage {}V is: {} (ms)".format(V,t_ms))

plt.plot(t,v,'b')
plt.plot(t,v1,'r--')

plt.grid()

plt.show()