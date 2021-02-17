# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def test_EquilateralB(self):
        self.assertEqual(classifyTriangle(2,2,2), 'Equilateral', '(2,2,2) is Equilateral')

    def test_Isosceles(self):
        self.assertEqual(classifyTriangle(1,2,1), 'Isosceles', '(1,2,1) is Isosceles')

    def test_Scalene(self):
        self.assertEqual(classifyTriangle(7,12,15), 'Scalene', '(7,12,15) is Scalene')

    def test_Invalid(self):
        self.assertEqual(classifyTriangle(300,300,600), 'InvalidInput', 'That Input is Invalid')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

