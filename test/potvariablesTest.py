#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Mingjun Zhou <mingjun.zhou@gmail.com>
# Licence: BSD 3 clause


import unittest
import sys
sys.path.append("..")
from brml.potvariables import potvariables
from brml.potential import potential
import numpy as np


class potvariablesTestCase(unittest.TestCase):
    #def setUp(self):
    #    return

    #def tearDown(self):
    #    return

    def testEmptyPot(self):
        pot = []
        self.assertRaises(NameError, potvariables, pot)

    """def testNoneTable(self):
        pot = [potential([1], np.zeros(0))]
        self.assertRaises(ValueError, potvariables, pot)
    """

    def testNoneVariables(self):
        pot = [potential(np.array([]), np.zeros(3))]
        self.assertRaises(ValueError, potvariables, pot)

    def testDiffVaTa(self):
        pot = [potential(np.array([1, 2]), np.zeros((3, 2, 2)))]
        self.assertRaises(ValueError, potvariables, pot)

    def testMismatchPot(self):
        """mismatch dimension in pot"""
        pot = [potential() for i in range(4)]
        pot[0].variables = np.array([0])
        pot[0].card = np.array([2])
        pot[0].table = np.zeros(2)

        pot[1].variables = np.array([1])
        pot[1].card = np.array([3])
        pot[1].table = np.zeros(3)

        pot[2].variables = np.array([2, 0, 1])
        pot[2].card = np.array([4, 3, 3])
        pot[2].table = np.zeros((4, 3, 3))

        pot[3].variables = np.array([3, 1])
        pot[3].card = np.array([3, 1])
        pot[3].table = np.zeros((2, 2))

        v, ns, con, convec = potvariables(pot)
        #pot.dispose()
        pot = None
        self.assertEqual(v, [0, 1, 2, 3])
        self.assertEqual(ns, [2, 3, 4, 2])
        self.assertEqual(con, 0)
        self.assertEqual(convec, [0, 0, 1, 1])

    def testMatchPot(self):
        """all variables's dimensions are match in pot"""
        pot = [potential() for i in range(4)]
        pot[0].variables = np.array([0])
        pot[0].card = np.array([2])
        pot[0].table = np.zeros(2)

        pot[1].variables = np.array([1])
        pot[1].card = np.array([3])
        pot[1].table = np.zeros(3)

        pot[2].variables = np.array([2, 0, 1])
        pot[2].card = np.array([4, 2, 3])
        pot[2].table = np.zeros((4, 2, 3))

        pot[3].variables = np.array([3, 1])
        pot[3].card = np.array([3])
        pot[3].table = np.zeros((2, 3))

        v, ns, con, convec = potvariables(pot)
        #pot.dispose()
        pot = None
        self.assertEqual(v, [0, 1, 2, 3])
        self.assertEqual(ns, [2, 3, 4, 2])
        self.assertEqual(con, 1)
        self.assertEqual(convec, [1, 1, 1, 1])


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(potvariablesTestCase("testEmptyPot"))
    #suite.addTest(potvariablesTestCase("testNoneTable"))
    suite.addTest(potvariablesTestCase("testNoneVariables"))
    suite.addTest(potvariablesTestCase("testDiffVaTa"))
    suite.addTest(potvariablesTestCase("testMismatchPot"))
    suite.addTest(potvariablesTestCase("testMatchPot"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
