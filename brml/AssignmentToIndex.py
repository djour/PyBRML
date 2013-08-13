#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Mingjun Zhou <mingjun.zhou@gmail.com>
# Licence: BSD 3 clause


import numpy as np


def AssignmentToIndex(assignment, dim):
    I = 0
    for i, a in enumerate(assignment):
        I += a * int(np.prod(dim[i+1:]))
    return I
