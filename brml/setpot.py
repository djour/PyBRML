"""
%SETPOT sets array potential variables to specified states
% newpot = setpot(pot,variables,evidstates)
%
% set variables in potential to evidential states in evidstates
% Note that the new potential does not contain the evidential variables
"""
import numpy as np
import copy as copy
from .potential import potential
from ismember import ismember
from setstate import setstate
from intersect import intersect
from setstate import setstate
from setminus import setminus
from myzeros import myzeros
from multpots import multpots
#from brml import *

def setpot(pot,evvariables,evidstates):
#FIXME: data format needed to be unified
	vars = pot.variables
	#vars = np.array(pot.variables) # convert to ndarray format
	#evariables = np.array(evvariables) # convert to ndarray format
	#evidstates = np.array(evidstates) # convert to ndarray format
	print "variables:", vars
	table = pot.table
	nstates = table.shape
	print "number of states:", nstates
	intersection = intersect(vars,evvariables)
	print "number of intersection:", intersection.size
	if intersection.size == 0:
		newpot = copy.copy(pot)
	else:
		newpot = potential(None, None)
		nonevidentialvariables = setminus(vars,evvariables)
		print "non evidential variables=", nonevidentialvariables
		thispotevidentialvariables = intersection
		print "this potevidential variables=", thispotevidentialvariables
#FIXME: only 1 variable is considered, not applicable to multiple variable-evidence
		a,bind = ismember(thispotevidentialvariables,vars)
		print "the potevidential variable's index in vars is:", bind
		tmppot = potential(None, None)
		tmppot.variables = thispotevidentialvariables
		tmppot.table=myzeros(nstates[bind])
#NOTE: use NAN as initial state in Python instead of 0. (Different from MATLAB)
		#tmppot.table[:] = np.nan
		print "the tmppot.variables:", tmppot.variables
		print "the tmppot.table: \n", tmppot.table
		tmppot2 = potential(None, None)
#FIXME: pass value parameters into setpot, not inside the function 
		print "evvariables:", evvariables
		print "evidstates:", evidstates
		print "tmppot2.variables:", tmppot2.variables
		print "tmppot2.table:", tmppot2.table
		tmppot2 = setstate(tmppot,evvariables,evidstates,1)
		print "tmppot2.variables=",tmppot2.variables
		print "tmppot2.table= \n",tmppot2.table
#FIXME: MATLAB:  joint_list = [tmppot2,pot]
		joint_list = [pot,tmppot2]
		print "joint_list:", joint_list
		mp = multpots(joint_list)
		print "mp.variabels=", mp.variables
		print "mp.table= \n", mp.table
		#newpot = sum(multpots([{tmppot2} {pot}]),thispotevidentialvariables);
		#test
		newpot.variables = mp.variables
		newpot.table = np.sum(mp.table,thispotevidentialvariables)
	return newpot