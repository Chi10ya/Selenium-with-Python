import unittest

from BatchTesting_Package1.TC1_LoginTest import *
from BatchTesting_Package1.TC2_SignUpTest import *

from BatchTesting_Package2.TC1_PaymentTest import *
from BatchTesting_Package2.TC2_PaymentReturnsTest import *

# Get all tests from LoginTest, SignUpTest, PaymentTest and PaymentReturnsTest
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

# Creating test suites
sanityTestSuite = unittest.TestSuite([tc1, tc2])
functionalTestSuite = unittest.TestSuite([tc2, tc4])

unittest.TextTestRunner(verbosity=2).run(sanityTestSuite)