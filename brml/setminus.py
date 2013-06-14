"""
C=SETMINUS(A,B)
C is the set A, without the elements B. C preserves the ordering of A

Python:
diff is the set in A without the elemnts B.
"""
import numpy as np

def setminus(a,b):
	a = np.array(a)
	b = np.array(b)
	intersect = np.intersect1d(a,b)
	diff = np.setxor1d(a,intersect)
	return diff