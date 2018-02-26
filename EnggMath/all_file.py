from tkinter import *

import lineq
import quadeq
import polar_plot as pp
import singraph as sg
import cartes

print("""
Select the following choice:
1. Linear Equation
2. Quadratic Equation
3. Polar plot 
4. Wave graphs: Sine, Cosine, Tangent
5. Cartesian & Polar co-ordinates
	""")

ip = int(input('>> '))

if ip == 1:
	lineq.linsol()
elif ip == 2:
	quadeq.quadsol()
elif ip == 3:
	pp.polar_function()
elif ip == 4:
	sg.waveGraph()
elif ip == 5:
	cartes.all_fun()