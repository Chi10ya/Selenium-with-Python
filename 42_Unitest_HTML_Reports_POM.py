#  ********************* 42:  Unitest + HTML Reports + Page Object Model

# Python unitest HTML TestRunner reports

    # For HTML reports, we need to have the plugin html-testRunner

       #cmd : pip install html-testRunner
    # Note: if you run the program in general way Ctrl+Shift+F10,  which is having a HTML testrunner it'll not generated the HTML report.
            # You need to execute through command prompt / terminal by the command >> python <filename.py>

# Test Case : Orange HRM Login test
#----------------------------------
#1: Launch browser
#2: Verify home page title
#3: Verify login
#4: close browser

# Selenium python test case using Unit test, HTML reports
# Selenium python project | Unit test, POM, HTML reports


import unittest
import HtmlTestRunner
from selenium import webdriver

chromeDriverPath = "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"
appURL = "https:\\opensource-demo.orangehrmlive.com"
htmlReportsPath = "C:\\ScreenShots-nd-Logs\\htmlReports"

class OrangeHRMTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver= webdriver.Chrome(executable_path= chromeDriverPath)
        cls.driver.maximize_window()

    def test_homePageTitle(self):
        self.driver.get(appURL)
        self.assertEqual("OrangeHRM", self.driver.title, "webpage title is not matching")

    def test_login(self):
        self.driver.get(appURL)
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        self.assertEqual("OrangeHRM", self.driver.title, "webpage titel is not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main(testRunner= HtmlTestRunner.HTMLTestRunner(output=htmlReportsPath))




