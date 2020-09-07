# -*- encoding:utf-8 -*-
#! /usr/local/bin/python

'''
Created on 2015-1-28

@author: ldq
'''
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import unittest


def testAll():
    #1 discover test cases
    this_dir = os.path.dirname(__file__)
    package_tests = unittest.defaultTestLoader.discover(this_dir)
    #2 add test cases to suite
    suite = unittest.TestSuite()
    suite.addTests(package_tests)
    return suite


if __name__ == "__main__":
    print("start")
    suite = testAll()
    #3 run test cases
    unittest.TextTestRunner(verbosity=2).run(suite)