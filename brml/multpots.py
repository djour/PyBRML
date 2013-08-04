#!/usr/bin/env python

"""
MULTPOTS Multiply potentials into a single potential
newpot = multpots(pots)

multiply potentials : pots is a cell of potentials
potentials with empty tables are ignored
if a table of type 'zero' is encountered, the result is a table of type
'zero' with table 0, and empty variables.
"""


def multpots(pots):
    # import copy
    newpot = pots[0]
    for i in range(1, len(pots)):  # loop over all the potentials
        #FIX ME: did not check dimension consistency
        newpot = newpot*pots[i]
    return newpot
