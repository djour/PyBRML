#!/usr/bin/env python

"""
% ndx = subv2ind(siz,sub)
%
% state to index : return the linear index of a state vector sub based on an array of size siz
% If sub is a matrix, each row is taken as a state vector and the linear index returned in the
% corresponding row of ndx. 
% This function is the inverse of ind2subv.m
"""
import numpy as np
#FIXME: not quite clear about this function
def subv2ind(siz,sub):
	print "siz=", siz
	print "sub=", sub
	k = np.array([0])
	print "k=", k
	k = np.append(k, np.cumprod(siz[0:-1]))
	print "k=", k
# MATLAB: 	ndx=sub*k.T-k.sum()+1
	ndx=sub*k.T-k.sum()
	print "ndx=", ndx

	return ndx