import numpy as np 
import math
import matplotlib.pyplot as plt 

fs = 100
f = 2

x = np.arange(fs)

print(x)

y = [np.sin(2*np.pi*f * (i/fs)) for i in np.arange(fs)]

print(y)

plt.plot(x,y)
plt.grid()

plt.show()