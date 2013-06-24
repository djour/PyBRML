#!/usr/bin/env python

"""
same as ismember() in MATLAB
tf: TRUE or FALSE
index: the index for each A in B
"""
import numpy as np

def ismember(a, b):
	print "judge ismember......"
#FIXME: data format needed to be unified
	aa = a
	a = np.array(a)
	b = np.array(b)
	print "a:", a
	print "b:", b
	print "unifying the format......"
	print "a.ndim =", a.ndim
	print "b.ndim =", b.ndim
	if a.ndim != b.ndim:
		a = np.array([aa])
	print "a:", a
	print "b:", b
	tf = np.in1d(a,b) # for newer versions of numpy(v1.4+)
	# tf = np.array([i in b for i in a]) # for older versions of numpy
	u = np.unique(a[tf])
	index = np.array([(np.where(b == i))[0][-1] if t else 0 for i,t in zip(a,tf)])
	return tf, index
