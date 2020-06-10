from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..")) # adding the project path to environment variables
from POM_UnitTest_HTMLReports_Framework_SDET.PageObjects.LoginPage import LoginPage
import time

class LoginTest(unittest.TestCase):

    demoAppURL = "http://admin-demo.nopcommerce.com"
    chromeDriverPath = "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"
    username = "admin@yourstore.com"
    password = "admin"
    driver=webdriver.Chrome(executable_path=chromeDriverPath)

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.demoAppURL)
        cls.driver.maximize_window()

    def test_Login(self):
        objLogin=LoginPage(self.driver)
        objLogin.setUserName(self.username)
        objLogin.setPassword(self.password)
        objLogin.clickLogin()
        time.sleep(5)
        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "webpage title is not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='C:\\Users\\chaitanya.mohammad\\PycharmProjects\\SDET_SeleniumWithPython\\POM_UnitTest_HTMLReports_Framework_SDET\\Reports'))