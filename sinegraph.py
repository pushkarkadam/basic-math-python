import math
import matplotlib.pyplot as plt
import numpy as np
from numpy import *

x1 = np.arange(100)

y1 = [np.sin(i) for i in np.arange(len(x1))]

x2 = np.arange(100)

y2 = [np.cos(j) for j in np.arange(len(x2))]

plt.plot(x1,y1,label='sine wave')
#plt.stem(x1,y1,'r')
plt.plot(x2,y2,label='cosine wave')
plt.title('Wave graphs')
plt.grid()
plt.show()
