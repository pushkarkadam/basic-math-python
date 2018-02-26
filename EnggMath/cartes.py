import cart2pol as c2p 
import pol2cart as p2c 


def all_fun():
	print('''
Select:
1) Cartesian to Polar
2) Polar to Cartesian
		''')

	c = int(input(">> "))

	if c == 1:
		c2p.cart_pol()
	else:
		p2c.pol_cart()