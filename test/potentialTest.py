#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Mingjun Zhou <mingjun.zhou@gmail.com>
# Licence: BSD 3 clause


import unittest
import sys
sys.path.append("..")
from brml.potential import potential
import numpy as np


class potentialTestCase(unittest.TestCase):
    def setUp(self):
        self.pot = potential()
        self.pot.variables = np.array([2, 1])
        self.pot.card = np.array([2, 2])
        self.pot.table = np.array([[0.2, 0.6], [0.8, 0.4]])

    def tearDown(self):
        self.pot = None

    def assertTwoPot(self, pa, pb):
        assert np.allclose(pa.variables, pb.variables)
        assert np.allclose(pa.card, pb.card)
        assert np.allclose(pa.table, pb.table)

    def testMultEmpty(self):
        newpot = self.pot * potential()
        self.assertTwoPot(newpot, self.pot)
        newpot = None

        newpot = potential() * self.pot
        self.assertTwoPot(newpot, self.pot)

    def testMult(self):
        otherpot = potential()
        otherpot.variables = np.array([3])
        otherpot.card = np.array([3])
        otherpot.table = np.array([0.1, 0.4, 0.5])
        answerpot = potential()
        answerpot.variables = np.array([1, 2, 3])
        answerpot.card = np.array([2, 2, 3])
        answerpot.table = np.array([[[0.02, 0.08, 0.1],
                                     [0.08, 0.32, 0.4]],
                                    [[0.06, 0.24, 0.3],
                                     [0.04, 0.16, 0.2]]])
        self.assertTwoPot(self.pot * otherpot, answerpot)

        otherpot = potential()
        otherpot.variables = np.array([3, 1])
        otherpot.card = np.array([3, 2])
        otherpot.table = np.array([[0.2, 0.3], [0.2, 0.2], [0.6, 0.5]])
        answerpot = potential()
        answerpot.variables = np.array([1, 2, 3])
        answerpot.card = np.array([2, 2, 3])
        answerpot.table = np.array([[[0.04, 0.04, 0.12],
                                     [0.16, 0.16, 0.48]],
                                    [[0.18, 0.12, 0.3],
                                     [0.12, 0.08, 0.2]]])
        self.assertTwoPot(self.pot * otherpot, answerpot)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(potentialTestCase("testMultEmpty"))
    suite.addTest(potentialTestCase("testMult"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
