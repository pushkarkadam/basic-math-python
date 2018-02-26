'''
************ IMPORTANT NOTE ON PLOTTING SINE OR COSINE GRAPH *************
Whenever you are trying to loop i through the array of 't' 
ensure that in the equation, you have the final limit of t divided by the 
value of current t in which the loop in running on.

e.g.

t = np.linspace(0,T)

v = [np.sin(2*math.pi * (i/T)) for i in t]

check out (i/T)

This is very much important
So, whenever you are working with trigonometric waveform, ensure that
'i' which you are running through 't'(values on x axis) 
it is always divided by T

'''



import numpy as np 
import math
import matplotlib.pyplot as plt 


v = 240
v_max = math.sqrt(2)*v  #Fundamental voltage having an rms value of 240V
						#has a maximum value. or amplitude of sqrt(2)*v

f = 50
w = 2*math.pi*f 		#Angular velocity

T = 1/f 				#The time for one cycle of fundamental is given by T = 1/f
						#Value of T is given in milli-seconds
T_ms = T*1000			#converting seconds to milli-seconds
t = np.linspace(0,T_ms)

V1 = [v_max*np.sin(w*(i/T_ms)) for i in t]

'''
The third harmonic has an amplitude equal to 20% of v_max
The frequency of third harmonic is 3*f
Thus the angular velocity = (2*pi*(3*f)) rad/s
'''

v_max_3 = 0.2*v_max
f3 = 3*f
w3 = 2*math.pi*f3

V2 = [v_max_3*np.sin(w3*(i/T_ms) - (3*math.pi)/4) for i in t]

V = [v_max*np.sin(w*(i/T_ms)) + v_max_3*np.sin(w3*(i/T_ms) - (3*math.pi)/4) for i in t]

plt.plot(t,V1,'b--',label='First Harmonic')
plt.plot(t,V2,'b--',label='Third Harmonic')
plt.plot(t,V,label='Voltage',color='r')

plt.legend()
plt.title('Complex Waveform')
plt.xlabel('Time t (ms)')
plt.ylabel('Voltage\nv(V)')
plt.grid()
plt.show()