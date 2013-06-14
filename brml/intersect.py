"""
same as intersect(a,b) in MATLAB
return the intersect set of set1 and set2
"""
import numpy as np

def intersect(a,b):
	a = np.array(a)
	b = np.array(b)
	print "intersect-a:", a.size
	print "intersect-b:", b.size
	print "intersecting..... \n",
	intersect = np.intersect1d(b,a)
	return intersect