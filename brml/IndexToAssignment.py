#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Mingjun Zhou <mingjun.zhou@gmail.com>
# Licence: BSD 3 clause


import numpy as np


def IndexToAssignment(index, dim):
    A = []
    for i, d in enumerate(dim):
        A.append(index / int(np.prod(dim[i+1:])))
        index = index % int(np.prod(dim[i+1:]))
    return A
