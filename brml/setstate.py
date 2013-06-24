#!/usr/bin/env python

"""
%SETSTATE set a potential's specified joint state to a specified value
p = setstate(pot,vars,states,val)
All states of the potential that match the given (sub)state are set to val
eg: pot=array([1 2],rand(2,2);
newpot=setstate(pot,1,2,0.5)
then for newpot.table all table entries matching variable 1 in state 2 will be set to value 0.5
"""
import numpy as np
import copy as copy
from ismember import ismember
from subv2ind import subv2ind
#from brml import *

def setstate(pot,vars,state,val):
#FIXME: data format needed to be unified
#FIXME: works only for 1-D
	vars = np.array([vars])
	state = np.array([state])
	print type(vars)
	print "original vars:", vars
	print "input state:", state
	p = copy.copy(pot)
	a,tmp = ismember(vars,pot.variables)
	print "tmp=", tmp
	vars = vars[tmp]
	state = state[tmp]
	print "effective vars:", vars
	dum,iperm = ismember(vars,pot.variables)
	print "original vars item in pot:", pot.variables
	print "original table in pot", pot.table
	print "effective vars' index in pot:", iperm
#FIXME: not consistent with former definition (need fn_size)
	nstates = pot.table.shape
#FIXME: arbitrary setting
	nstates = np.array([2])
	print "effective vars in pot NSTATES:", nstates
#NOTE: use NAN as initial state in Python instead of 0. (Different from MATLAB)
	permstates = np.empty((1,np.size(nstates)))
#FIXME: arbitrary setting
	permstates = np.empty(1)
	permstates[:] = np.nan 
	print "initial effective vars states: \n", permstates
	permstates[iperm] = state
	print "set effective vars states: \n", permstates
	# set effective var-states to val
	print "permstates=", permstates
	print "permstates.all()=", permstates.all()
	# MATLAB: if all(permstates>0) % if the state is unique
	allcondition = np.logical_not(np.isnan(permstates)).all()
	print "allcondition=", allcondition
	if allcondition: # if the state is unique
		print "Before setstate: p.table= \n", p.table
		watch_ndx = np.asarray([subv2ind(nstates,permstates)])
		watch_ndx = np.int8(watch_ndx)
		print "Callback watch_ndx = subv2ind(nstates,permstates)=", watch_ndx
#FIXME: data format need unified
#p.table[subv2ind(nstates,permstates)] = val
		#p.table = p.table.reshape(1,2)
		#print "reshaped p.table: \n", p.table
		print "val= ", val
		p.table[watch_ndx] = val
		#p.table = p.table.reshape(2,1)
		print "After setstate: p.table= \n", p.table
#FIXME: not implemented ELSE case
#	else : # set all states that match the given substate to the given value
#		sub=find(permstates>0);
#		st=ind2subv(nstates,1:prod(nstates));
#		p.table(all(st(:,sub)==repmat(permstates(sub),prod(nstates),1),2))=val;
	
	return p