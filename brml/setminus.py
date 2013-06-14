"""
C=SETMINUS(A,B)
C is the set A, without the elements B. C preserves the ordering of A

Python:
diff is the set in A without the elemnts B.
"""
if __name__ == '__main__':
	import numpy as np

def setminus(a,b):
	diff = np.setxor1d(a,b)
	return diff