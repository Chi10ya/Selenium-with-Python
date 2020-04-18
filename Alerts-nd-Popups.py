# 12: How to handle Alerts / Popups || Switching to Alerts / Popups

from selenium import webdriver
from selenium.webdriver.common.by import By


# BrowserDriverPaths
chromeDriverPath= "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"

# App URL
appURL= "https://testautomationpractice.blogspot.com/"

driver= webdriver.Chrome(executable_path= chromeDriverPath)
driver.maximize_window()
driver.get(appURL)

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
driver.switch_to.alert().accept()  # closes alert window using OK button
#driver.switch_to_alert.dismiss() # closes alert window using cancel button

driver.quit()