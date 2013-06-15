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

def condpot(pot,varargin):
#FIXME: only 1 varargin supported , use *arg in further development
	newpot = potential(None, None)
	y = []
	x = varargin
	print "pot.variables:", pot.variables
	print "pot.table: \n", pot.table
	print "x:", x
	print "pot.variables:", pot.variables
	intersection = intersect(x,pot.variables)
	print "intersection=", intersection
	newpot.variables = intersection
	axis_intersection = pot.variables.index(varargin)
	print "axis_intersection=", axis_intersection
	newpot.table = np.sum(pot.table,axis_intersection)
	print "newpot.variables:", newpot.variables
	print "newpot.table: \n", newpot.table
	#newpot = divpots(newpot,brml.sumpot(newpot))
	
	return newpot