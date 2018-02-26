'''
In this problem the graph is like y = sin(x)
I need to find the values of:
-----------------------------
5 * sin(theta) + 3 = 0
-----------------------------
'''



import numpy as np 
import math
import matplotlib.pyplot as plt 

theta = math.asin(-3/5)
'''
old_theta_deg = math.fabs(theta*(180/math.pi))
'''

old_theta_deg = math.fabs(math.degrees(theta))
print(old_theta_deg)
theta_1 = old_theta_deg + 180

theta_2 = 360 - old_theta_deg

t_1 = float("{0:.3f}".format(theta_1))
t_2 = float("{0:.3f}".format(theta_2))

print("Hence the value for theta from 0 to 360 is {} deg. or {} deg.".format(t_1, t_2))

'''
The code for the graph
I am trying to plot the graph which will ensure that I plot the values properly.
This will be achieved by creating the angles like in previous problem.

'''

angles = np.linspace(0,360)

x = [math.radians(j) for j in angles]

y = [5*math.sin(i) + 3 for i in x]

plt.plot(angles,y)
plt.grid()
plt.show()