"""
%SETPOT sets array potential variables to specified states
% newpot = setpot(pot,variables,evidstates)
%
% set variables in potential to evidential states in evidstates
% Note that the new potential does not contain the evidential variables
"""
if __name__ == '__main__':
	import numpy as np
	import copy as copy
	from brml import *

def setpot(pot,evvariables,evidstates):
	vars = pot.variables
	print "variables:", vars
	table = pot.table
	nstates = table.shape
	print "number of states:", nstates
	intersection = intersect(vars,evvariables)
	if intersection.size == 0
		newpot = copy.copy(pot)
	else
		nonevidentialvariables = setminus(vars,evvariables)
		print "non evidential variables=", nonevidentialvariables
		thispotevidentialvariables = intersection
		print "this potevidential variables=", thispotevidentialvariables
		[a bind]=ismember(thispotevidentialvariables,vars)
		tmppot=potential(None, None)
		tmppot.variables=thispotevidentialvariables;
		tmppot.table=myzeros(nstates(bind));
		tmppot2=setstate(tmppot,evvariables,evidstates,1);
		newpot = sum(multpots([{tmppot2} {pot}]),thispotevidentialvariables);
	return newpot