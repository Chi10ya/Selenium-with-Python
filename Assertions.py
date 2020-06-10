# ********** Tutorial 33: Assertions | AssertEqual || AssertNotEqual
# ********** Tutorial 34: Assertions | AssertTrue || AssertFalse
# ********** Tutorial 35: Assertions | AssertIsNone || AssertIsNotNone
# ********** Tutorial 36: Assertions | AssertIn || AssertNotIn
# ********** Tutorial 37: Assertions | Relational Comparision || assertGreater , assertGreaterEqual, assertLess, assertLessEqual

# Assertion is nothing but the checkpoint or you can say it as verification for the test case to evaluate some item on the execution
# If we do not provide any assesrtion inside a test case then there is no way to know whether a test case is failed or not
# Assertion helps in report generation, based on the assertions the test execution report will be generated.
# There are few assertion which will accept all the values and few assertions with accept only numberic values

# Two types of Assertions
#       1: assertEqual : assertEqual compare the first parameter with the second parameter, if both matches the unitest will continue with the remaining execution
#           but the both the values are different then unit tests fails the test case.

#       2: assertNotEqual : assertNotEqual method compares the given two parameters, if both parameter are not same then unittest passes the test case but if both
#           parameter are same then unittest fails the test case.

#       3: assertTrue : When we have only two parameter we can use assertEqual method to check whether both are same or not, but if we have more than two parameters,
#           comparing values with assertEqual method become more difficult.

#           assertTrue method checks whether given parameter is true or not, if value is true then test is passed otherwise test is failed.
#       4: assertFalse : assertFalse method compares whether given value or expression results in false or not

#           If the result or value is False then unittest passes the testcase but if the result or value is True then unittest fails the test case.
#       5: assertIsNone : assertIsNone method verifies whether give values or expression results in None or not, if the result is none then python uniitest will pass
#           the test case otherwise fails the test case.

#       6: assertIsNotNone : assertIsNotNone method verifies whether give values is not None, if the value is None then the test case will be failed.

#       7: assertIn : method verifies whether the first element is present in the second element. If element is present in the second element then test is passed otherwise test is failed

#       8: assertNotIn : method verifies whether the first element is not present in the second element or not, if first element is present the test will be failed otherwise test is passed.
#  Note: These two mnethods (7 & 8) will be helpful when you want to verify presence of a value in a List, Tuple, Set and Dictionary.

#       9: assertGreater : verifies whether first values if greater than second value or not

#       10: assertGreaterEqual : verifies whether first parameter is greater or equal to the second parameter

#       11: assertLess : verifies whether first parameter is lesser than second parameter or not

#       12: assertLessEqual : verifies whether first parameter is lesser or equal to the second parameter.

import unittest
from selenium import webdriver

chromeDriverPath = "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"
flightAppURL = "http://newtours.demoaut.com"
googleURL = "http://www.google.com"

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path= chromeDriverPath)
        self.assertIsNone(driver)
        self.assertIsNotNone(driver)

        driver.get(flightAppURL)
        titleOfWebPage = driver.title
        self.assertEqual("Google", titleOfWebPage, "webpages titles are not same")
        #self.assertNotEqual("Google", titleOfWebPage)
        self.assertTrue(titleOfWebPage == "Google")
        #self.assertFalse(titleOfWebPage == "Google")

        # Tut 36: 7 & 8
        mylist= ["python", "selenium", "java"]
        print(mylist)
        print(f"List Type is : {type(mylist)}")
        self.assertIn("python", mylist)
        self.assertNotIn("Ruby", mylist)
        self.assertGreater(100, 10)
        self.assertGreaterEqual(100, 100)
        self.assertLess(10, 100)
        self.assertLessEqual(100, 100)


if __name__ == "__main__":
    unittest.main()