"""
same as myzeros() in MATLAB
MYZEROS same as zeros(x) but if x is a scalar interprets as zeros([x 1])
"""
import numpy as np

def myzeros(x):
	print "x =", x
	x = np.array(x)
	if x.size > 1:
		out=np.zeros(x)
	else:
		out=np.zeros((x,1))
	return out
