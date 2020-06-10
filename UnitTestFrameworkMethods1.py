# **************Tutorial 31:  Python unittest framework methods
"""
    The available methods are:
        setUp : It executes every time before all test methods
        tearDown: It executes every time after all test methods
        setUpClass: It executes only once when the class starts / started
        tearDownClass,: It executes only once when the class ends / completed.
        setUpModule,: will be executed before executing any class or any method present in the test class
        tearDownModule: will be executed after completing everything present in the python module.

        Note: setUpModule and tearDownModule should be created outside of the class

    The available decorators are:
        @classmethod

"""

import unittest

def setUpModule():
    print("Setup Module")

def tearDownModule():
    print("Tear down module")


class unitTestFramework_demo1(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("Setup  : > This is login test")

    @classmethod
    def tearDown(self):
        print("TearDown : > This is logout test")

    @classmethod
    def setUpClass(cls):
        print("SetupClass : > Open Application : Connect to DB")

    @classmethod
    def tearDownClass(cls):
        print("TearDownClass : > Close Application : End Connect to DB")


    def test_search(self):
        print(" 1 This is search page")

    def test_advance_search(self):
        print("2 This is advance search")

    def test_prepaid_recharge(self):
        print("3 This is prepaid recharge")

    def test_postpaid_recharge(self):
        print("4 This is postpaid recharge")


if __name__ == '__main__':
    unittest.main()