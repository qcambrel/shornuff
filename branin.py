import numpy as np

def branin(x):
	a = 1
	b = 5.1/(4*np.pi**2)
	c = 5/np.pi
	r = 6
	s = 10
	t = 1/(8*np.pi)
	return a*(x[1] - b*x[0]**2 + c*x[0] - r)**2 + s*(1-t)*np.cos(x[0]) + s