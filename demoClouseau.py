#!/usr/bin/env python

# Python implementation of BRMLtoolbox
# Author: Jiuding Duan
# License: GNU license
# def demoClouseau():
"""
	DEMOCLOUSEAU inspector clouseau example
"""
print __doc__

import numpy as np
from brml.potential import potential
from brml.variable import variable
# from brml import *
from brml.multpots import multpots
from brml.dag import dag
from brml.setpot import setpot
from brml.condpot import condpot


# Define number of variables(nodes)
N = 3   
butler=2; maid=1; knife=0 # Variable order is arbitary (3,2,1 for MATLAB)	
# Define states, starting from 0. (from 1 for MATLAB)
murderer=0; notmurderer=1
used=0; notused=1

""" 
The following definitions of variable are not necessary for computation,
but are useful for displaying table entries:
"""
# Create empty list for variable, len(variable) = N
variable = [ variable(None, None) for i in range(N)] 
print "variable list created as variable[knife, maid, butler] \n"
variable[butler].name='butler'; variable[butler].domain = ['murderer','not murderer']
variable[maid].name='maid'; variable[maid].domain =['murderer','not murderer']
variable[knife].name='knife'; variable[knife].domain=['used','not used']

"""
Three potential since p(butler,maid,knife)=p(knife|butler,maid)p(butler)p(maid).
potential numbering is arbitary
"""
# Create empty list for potential, len(variable) = N
pot = [potential(None, None) for i in range(N)]
print "pot list created as pot[knife, maid, butler] \n"

pot[butler].variables=butler
table = np.zeros((2))
table[murderer] =0.6
table[notmurderer] =0.4
pot[butler].table = table
print "butler created at:", pot[butler]

pot[maid].variables=maid
table = np.zeros((2))
table[murderer] =0.2
table[notmurderer] =0.8
pot[maid].table = table
print "maid created at:", pot[maid]

pot[knife].variables=[knife,butler,maid] # define array below using this variable order
table = np.zeros((2,2,2))
table[used, notmurderer, notmurderer]=0.3
table[used, notmurderer, murderer]   =0.2
table[used, murderer,    notmurderer]=0.6
table[used, murderer,    murderer]   =0.1
pot[knife].table = table
pot[knife].table[notused][:][:]=1-pot[knife].table[used][:][:] # due to normalisation
print "knife created at:", pot[knife]

jointpot = multpots(pot) # joint distribution
#FIXME: arbitrary set order and swaped
jointpot.variables = [0,1,2]
jointpot.table = np.swapaxes(jointpot.table,0,2)
print "jointpot.variables:", jointpot.variables
print "joint distribution generated as: jointpot \n", jointpot.table 

sum = jointpot.table.sum()
print "knife = ", variable[knife].domain[used], "maid = ", variable[maid].domain[murderer], "butler = ", variable[butler].domain[murderer]

DAG = dag(pot) # Generate the DAG adjacency matrix
print "DAG adjacency matrix: \n", DAG

evidencedpot = setpot(jointpot,knife,used)
#FIXME: arbitrary setting
evidencedpot.variables = evidencedpot.variables[1:]
print "................................................"
print "evidencedpot.variables:", evidencedpot.variables
print "evidencedpot.table: \n", evidencedpot.table

conditionedpot = condpot(evidencedpot,butler)
print "conditionedpot.variables:", conditionedpot.variables
print "conditionedpot.table: \n", conditionedpot.table
# jointpot = multpots(pot); % joint distribution

#drawNet(dag(pot),variable);
#disp('p(butler|knife=used):')
#disptable(condpot(setpot(jointpot,knife,used),butler),variable);
	
	
