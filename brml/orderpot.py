#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Mingjun Zhou <mingjun.zhou@gmail.com>
# Licence: BSD 3 clause


import numpy as np
import copy
from IndexToAssignment import IndexToAssignment
from potential import potential


def orderpot(pot, varargin):
    """
    Return potential with variables reordered according to orderpot. If order
    is missing or empty, the variables are sorted (low to high).
        newpot = orderpot(pot, <order>)

    Parameters
    ----------

    pot: brml.potential.potential object
        An object with fileds variables and table.
        pot.variables is a list of integer that indicates variables's name.
        pot.table is a np.ndarray of probability distribution.

    varargin: array_like (optional)
        An array_like of new orders.
        If varagin is missing or empty, the variables are sorted (low to high)

    Returns
    -------

    newpot: brml.potential.potential
        the new potential object
    """
    if not pot:
        return

    oldvs = list(pot.variables)
    oldta = pot.table
    oldns = list(oldta.shape)

    if not varargin:  # varargin is empty or missing
        varargin = copy.deepcopy(oldvs)
        varargin.sort()

    newvs = list(varargin)
    newta = copy.deepcopy(oldta)
    newta.resize(np.prod(oldns))
    newns = copy.deepcopy(oldns)

    newInold_idx = []
    oldInnew_idx = []
    for i, v in enumerate(newvs):
        idx = oldvs.index(v)
        newInold_idx.append(idx)
        oldInnew_idx.append(newvs.index(oldvs[i]))
        newns[i] = oldns[idx]

    for i in range(np.prod(oldns)):
        newass = IndexToAssignment(i, newns)

        oldass = [newass[j] for j in oldInnew_idx]
        newta[i] = oldta[tuple(oldass)]

    newta.resize(newns)
    newpot = potential(None, None)
    newpot.variables = newvs
    newpot.table = newta

    return newpot
