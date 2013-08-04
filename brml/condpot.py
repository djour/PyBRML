#!/usr/bin/env python

"""
%CONDPOT Return a potential conditioned on another variable
% newpot = condpot(pot,x,y)
% condition the potential to return potential with distribution p(x|y), summing over
% remaining variables. If y is empty (or missing), return the marginal p(x)
% If both x and y are missing, just return the normalised table
"""
import numpy as np
from .potential import potential
from intersect import intersect
from setminus import setminus

def condpot(pot,varargin):
#FIXME: only 1 varargin supported , use *arg in further development
	newpot = potential()
	y = []
	x = varargin
	#print "pot.variables:", pot.variables
	#print "pot.table: \n", pot.table
	#print "x:", x
	#print "pot.variables:", pot.variables
# convert variable to idx (not consistent in Python other than MATLAB)
	intersection, ix, ipot = intersect(x, pot.variables)
	#print "intersection=", intersection
	newpot.variables = intersection
        #print "pot.variables:", pot.variables
	FULL_axis = np.arange(pot.variables.size)
        #print pot.variables
        #print intersection
	axis_intersection = ipot
        #.index(intersection)
	other_axis = setminus(FULL_axis,axis_intersection)
	#print "axis_intersection=", axis_intersection
	#print "other_axis=", other_axis
        #print "Full_axis:", FULL_axis
        #print "other_axis:", other_axis
        newpot.table = np.apply_over_axes(np.sum, pot.table, other_axis)
	#print "newpot.variables:", newpot.variables
	#print "newpot.table: \n", newpot.table
	
	SUM = potential()
	SUM.variables = np.array([])
	SUM.table = np.sum(newpot.table)
        #print "newpot.table:", newpot.table
        #print "SUM.table:", SUM.table
	newpot = newpot/SUM
	
	return newpot
