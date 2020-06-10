from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import HtmlTestRunner


class OrangeHRMTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chromeDriverPath = "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"
        cls.driver=webdriver.Chrome(executable_path=chromeDriverPath)
        cls.driver.maximize_window()

    def test_homePageTitle(self):
        demoAppURL = "https://opensource-demo.orangehrmlive.com"
        self.driver.get(demoAppURL)
        self.assertEqual("OrangeHRM", self.driver.title, "webpage title is not matching")

    def test_login(self):
        demoAppURL = "https://opensource-demo.orangehrmlive.com"
        self.driver.get(demoAppURL)
        self.driver.find_element(By.NAME, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.NAME, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.NAME, "Submit").click()
        self.assertEqual("OrangeHRM", self.driver.title, "webpage title is not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\chaitanya.mohammad\\PycharmProjects\\SDET_SeleniumWithPython\\POM_UntiTest_HTMLReports_Framework-SDET\\Reports'))