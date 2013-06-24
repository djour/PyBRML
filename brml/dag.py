#!/usr/bin/env python

"""
DAG Return the adjacency matrix (zeros on diagonal) for a Belief Newtork
A=dag(pot)

Assumes that pot{i} contains the distribution p(i|pa(i))
"""
import numpy as np
	 
def dag(pot):
	vars = np.array([])
	for p in range(len(pot)):
		vars = np.append(vars, pot[p].variables)
	print "variables:", vars
#FIX ME in MATLAB version in case the index are not [1,2,....]
	N = len(np.unique(vars))
	print "number of variables:", N
	A = np.zeros((N,N))
	print "empty DAG matrix: \n", A
	for p in range(len(pot)):
		A[pot[p].variables,p] = 1
	eye = np.identity(N)
	A = A - A*eye;
	return A