import matplotlib.pyplot as plt
x1 = [1,2,3]
y1 = [5,7,4]

x2 = [1,2,3]
y2 = [11,7,12]

plt.plot(x1,y1,label='First plot')
plt.plot(x2,y2,label='Second plot')

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.title('Graph No.1\nFirst Graph')
plt.legend()
plt.grid()

print('Hey, this should come up in the terminal')
plt.show()
