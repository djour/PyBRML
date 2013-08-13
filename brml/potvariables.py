#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Mingjun Zhou <mingjun.zhou@gmail.com>
# Licence: BSD 3 clause


import numpy as np


def potvariables(pots):
    """Returns information about all variables in a set of potentials

    Return the variables and their number of states.
    If there is a dimension mismatch in the table then return con = 0.
    convec(i)=0 reports that variable i has conflicting dimension.

    Args:
        pots: a set of potentials

    Returns:
        variables: A list of all variables in pots
        nstates: A list of integers. nstates[idx] = number of dimension of
                 variables[idx]
        con: con = 0 if there is a dimension mismatch in the table;
             con = 1 otherwise
        convect: convec(i) = 0 reports that variable i has conflicting
                dimensions

    Raises:
        NameError: An error occured accessing a None set of potentials
        ValueError: An error occurred accessing pots with None field or
                    deffernt size in table and variables field
    """
    if not pots:
        raise NameError('potentials should not be None')

    """if not isinstance(pots, list):
        raise TypeError('pots should be list Type')
    """

    for i, pot in enumerate(pots):
        #if not isinstance(pot.variables, list):
        #    raise TypeError('No.%d field of variables should be list type')
        if pot.variables.size == 0:
            raise ValueError('No.%d field of variables should not be None', i)
        #if not isinstance(pot.table, np.ndarray):
        #    raise TypeError('No.%d field of variables shoud be np.ndarray\
        #                    type', i)
        if len(pot.table) is 0:
            raise ValueError('No.%d field of table should not be None', i)
        if len(pot.variables) != len(pot.table.shape):
            raise ValueError('No.%d field of table and variables should not\
                                be different size', i)

    variables = list(pots[0].variables)
    nstates = list(pots[0].table.shape)
    con = 1
    convec = list(np.ones(len(variables), 'int8'))

    for pot in pots[1:]:
        vs = pot.variables
        ns = list(pot.table.shape)
        for i, v in enumerate(vs):
            if v in variables:
                idx_va = variables.index(v)
                if ns[i] != nstates[idx_va]:
                    convec[idx_va] = 0
                    con = 0
            else:
                variables.append(v)
                nstates.append(ns[i])
                convec.append(1)

    return variables, nstates, con, convec
