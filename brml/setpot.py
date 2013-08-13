#!/usr/bin/env python

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
from IndexToAssignment import IndexToAssignment
from AssignmentToIndex import AssignmentToIndex


def setpot(pot, evvariables, evidstates):
    #FIXME: data format needed to be unified
    vars = pot.variables
    #vars = np.array(pot.variables) # convert to ndarray format
    #evariables = np.array(evvariables)
    # convert to ndarray format
    #evidstates = np.array(evidstates) # convert to ndarray format
    #print "variables:", vars
    table = pot.table
    nstates = pot.card
    #print "number of states:", nstates
    #print "vars:", vars
    #print "evvariables:", evvariables
    intersection, iv, iev = intersect(vars, evvariables)
    #iv = np.array(iv)
    #iev = np.array(iev)
    #print "intersection:", intersection
    #print "iv:", iv
    #print "iev:", iev
    #print "iv type:", type(iv)
    #print "number of intersection:", intersection.size
    if intersection.size == 0:
        newpot = copy.copy(pot)
    else:
        newvar = setminus(vars, intersection)
        dummy, idx = ismember(newvar, vars)
        newns = nstates[idx]
        newpot = potential()
        newpot.variables = newvar
        newpot.card = newns
        newpot.table = np.zeros(newns)
        #print "idx:", idx
        #print "iv:", iv
        for i in range(np.prod(newns)):
            newassign = IndexToAssignment(i, newns)
            oldassign = np.zeros(nstates.size, 'int8')
            oldassign[idx] = newassign
            oldassign[iv] = evidstates
            #print "newpot.table.shape:", newpot.table.shape
            #print "newassign:", newassign
            #print "newassign type:", type(newassign)
            newpot.table[tuple(newassign)] = pot.table[tuple(oldassign)]

    return newpot
