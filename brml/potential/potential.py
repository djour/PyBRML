#!/usr/bin/env python

"Basic Class: potential"
if __name__ == '__main__':
    print 'PotentialClass is running by itself'
else:
    print 'PotentialClass is imported as module'

import numpy as np
import copy
from brml.intersect import intersect
from brml.ismember import ismember
from brml.IndexToAssignment import IndexToAssignment


class potential:
    def __init__(self, variables=np.array([]), card=np.array([]),
                 table=np.array([])):
        self.variables = variables
        self.card = card
        self.table = table

    def __mul__(self, other):
        # check for empty potential
        if self.variables.size == 0:
            return other
        if other.variables.size == 0:
            return self

        commonitem = np.intersect1d(self.variables, other.variables)
        idx1 = np.in1d(self.variables, commonitem).nonzero()
        idx2 = np.in1d(other.variables, commonitem).nonzero()
        if commonitem.size > 0:
            assert np.allclose(self.card[idx1], other.card[idx2])

        newpot = potential()
        #FIX ME: dimension consistency not checked
        #FIX ME: only 1-D multiply considered

        newpot.variables = np.union1d(self.variables, other.variables)
        # sorted union of input arrays
        dummy, mapA = ismember(self.variables, newpot.variables)
        dummy, mapB = ismember(other.variables, newpot.variables)

        newpot.card = np.zeros(newpot.variables.size, 'int8')
        newpot.card[mapA] = list(self.card)
        newpot.card[mapB] = list(other.card)

        newpot.table = np.zeros(tuple(newpot.card))
        for i in range(np.prod(newpot.card)):
            assignment = IndexToAssignment(i, newpot.card)
            assign1 = np.array(assignment)[mapA]
            assign2 = np.array(assignment)[mapB]
            newpot.table[tuple(assignment)] = self.table[tuple(assign1)] *\
                other.table[tuple(assign2)]

        return newpot

    def __div__(self, other):
        #FIXME: works only 1-D considered, not completed
        newpot = copy.copy(self)
        newpot.variables = intersect(self.variables, other.variables)
        print "current divided newpot.variables=", newpot.variables
        newpot.table = self.table/other.table
        print "current divided table: \n", newpot.table
        return newpot

    def size(self):
        var = self.variables
        table = np.array(self.table)
        dim = table.ndim
        if dim == 0:
            print "ERRRRRRRRRRRRRRRRRR"
        elif dim > len(var):
            size = np.array(table.shape).size
            print "adjusted!!!!!!"

        return size  # np.array format
