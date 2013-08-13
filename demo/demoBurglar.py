#!/usr/bin/env python

# Python implementation of BRMLtoolbox
# Author: Mingjun Zhou
# License: GNU License

"""
DEMOBURGLAR DEMO: was it the burglar example?
"""
print __doc__

import numpy as np
import sys
sys.path.append("..")
from brml.variable import variable
from brml.potential import potential
from brml.multpots import multpots
from brml.potvariables import potvariables
from brml.setpot import setpot
from brml.condpot import condpot
from brml.dag import dag


burglar, earthquake, alarm, radio = range(4)  # Variable order is arbitary
yes = 0
no = 1

variable = [variable(None, None) for i in range(4)]

variable[burglar].name = 'burglar'
variable[burglar].domain = ['yes', 'no']

variable[earthquake].name = 'earthquake'
variable[earthquake].domain = ['yes', 'no']

variable[alarm].name = 'alarm'
variable[alarm].domain = ['yes', 'no']

variable[radio].name = 'radio'
variable[radio].domain = ['yes', 'no']

pot = [potential() for i in range(4)]

pot[burglar].variables = np.array([burglar])
pot[burglar].card = np.array([2])
table = np.zeros(2)
table[yes] = 0.01
table[no] = 0.99
pot[burglar].table = table

pot[earthquake].variables = np.array([earthquake])
pot[earthquake].card = np.array([2])
table = np.zeros(2)
table[yes] = 0.000001
table[no] = 1 - table[yes]
pot[earthquake].table = table

pot[alarm].variables = np.array([alarm, burglar, earthquake])
pot[alarm].card = np.array([2, 2, 2])
table = np.zeros((2, 2, 2))
table[yes, yes, yes] = 0.9999
table[yes, yes, no] = 0.99
table[yes, no, yes] = 0.99
table[yes, no, no] = 0.0001
table[no][:][:] = 1 - table[yes][:][:]
pot[alarm].table = table

pot[radio].variables = np.array([radio, earthquake])
pot[radio].card = np.array([2, 2])
table = np.zeros((2, 2))
table[yes, yes] = 1
table[no, yes] = 0
table[yes, no] = 0
table[no, no] = 1
pot[radio].table = table

#va = potvariables(pot)
jointpot = multpots(pot)
#print "jointpot.variables:", jointpot.variables
#print "jointpot.card:", jointpot.card
#print "jointpot.table:", jointpot.table

#print jointpot.variables
DAG = dag(pot) # Generate the DAG adjacency matrix
print "DAG adjacency matrix: \n", DAG

evidencedpot = setpot(jointpot, alarm, yes)
#FIXME: arbitrary setting
#evidencedpot.variables = evidencedpot.variables[1:]
#print "................................................"
#print "evidencedpot.variables:", evidencedpot.variables
#print "evidencedpot.table: \n", evidencedpot.table

#print "evidencepot.variables:", evidencedpot.table
conditionedpot = condpot(evidencedpot, burglar)
print "p(burglar|alarm=yes)"
print "conditionedpot.variables:", conditionedpot.variables
print "conditionedpot.table: \n", conditionedpot.table
# jointpot = multpots(pot); % joint distribution

evidencedpot = setpot(jointpot, [alarm, radio], [yes, yes])
conditionedpot = condpot(evidencedpot, burglar)
print "p(burglar|alarm=yes, radio=yes):"
print "conditionedpot.variables:", conditionedpot.variables
print "conditionedpot.table: \n", conditionedpot.table
#print "type:", (conditionedpot.table).dtype
