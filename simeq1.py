import numpy as np
import matplotlib.pyplot as plt


'''
SOLUTION FOR GRAPH
'''

def my_graph():
	x1 = np.arange(-20,20,0.5)
	y1 = [(c1-(a1*i))/b1 for i in x1]

	x2 = np.arange(-20,20,0.5)
	y2 = [(c2-(a2*j))/b2 for j in x2]

	plt.plot(x1,y1,label='First equation',color='r')
	plt.plot(x2,y2,label='Second equation',color='b')

	plt.xlabel('X')
	plt.ylabel('Y')

	plt.title('Graphical solution for\n{}x + {}y = {}\n{}x + {}y = {}'.format(a1,b1,c1,a2,b2,c2))
	plt.legend()
	plt.grid()
	plt.show()

'''
-------------------------------------------------
FUNCTION ENDS HERE
-------------------------------------------------
'''

print('-----------------------------------------')
print('FIRST EQUATION')
print('-----------------------------------------\n')
a1 = int(input('Enter the coefficient of x:'))
b1 = int(input('\nEnter the coefficient of y:'))
c1 = int(input('\nEnter the RHS:'))

print('\n----------------------------------------')
print('SECOND EQUATION')
print('----------------------------------------\n')
a2 = int(input('Enter the coefficient of x:'))
b2 = int(input('\nEnter the coefficient of y:'))
c2 = int(input('\nEnter the RHS:'))

A = np.array([[a1,b1],[a2,b2]])
B = np.array([c1,c2])

C = np.linalg.solve(A,B)
print('------------------------------------------')
print('x:{}'.format(C[0]))
print('y:{}'.format(C[1]))
print('------------------------------------------')


G = input('Would you like to see Graph[Y/N]:')

if G == 'Y' or G =='y':
	my_graph()