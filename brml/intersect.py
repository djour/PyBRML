#!/usr/bin/env python

"""
same as intersect(a,b) in MATLAB
return the intersect set of set1 and set2
"""
import numpy as np
from ismember import ismember


def intersect(a,b):
	a = np.array(a)
	b = np.array(b)
	#print "intersect-a:", a.size
	#print "intersect-b:", b.size
	#print "intersecting..... \n",
	intersect = np.intersect1d(b,a)
        dummy, iA = ismember(intersect, a)
        dummy, iB = ismember(intersect, b)
        #print "intersect", intersect
	return intersect, iA, iB
