import numpy as np 
import math
import matplotlib.pyplot as plt 
from fractions import Fraction

print("---------------------------------")
print("COMPLEX WAVEFORM")
print("---------------------------------")

f = float(Fraction(input('Enter frequency: ')))

w = 2*math.pi*f
T = 100

t = np.linspace(0,T)

v1 = [100*np.sin(w*(i/T)) for i in t]

v2 = [30*np.sin(3*w*(i/T)) for i in t]

v3 = [100*np.sin(w*(i/T)) + 30*np.sin(3*w*(i/T)) for i in t]

plt.plot(t,v1,label='First term',color='blue')
plt.plot(t,v2,label='Second term',color='purple')
plt.plot(t,v3,label='Final term',color='red')

plt.legend()
plt.grid()
plt.title('Complex Waveform')
plt.show()
