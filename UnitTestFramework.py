# ********** Tutorial 30: Python Unit Test Framework


import unittest
from selenium import webdriver

chromeDriverPath = "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"
flightAppURL = "http://newtours.demoaut.com"
googleURL = "http://www.google.com"


class SearchEnginesTest(unittest.TestCase):
    def test_FirstTest(self):
        print("This is my first unit test case")

    def test_flight_app_url(self):
        self.driver = webdriver.Chrome(executable_path=chromeDriverPath)
        self.driver.get(flightAppURL)
        print("Title of the page is : "+self.driver.title)
        self.driver.close()

    def test_bing(self):
        self.driver = webdriver.Chrome(executable_path=chromeDriverPath)
        self.driver.get(googleURL)
        print("Title of the page is : " + self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()



