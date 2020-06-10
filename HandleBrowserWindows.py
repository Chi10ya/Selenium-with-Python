# 14: How to handle browser windows / Switch between windows ==> driver.current_window, driver.window_handles

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import *

# BrowserDriverPaths
chromeDriverPath= "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"

demoAppURL= "http://demo.automationtesting.in/Windows.html"

# For Chrome browser
driver= webdriver.Chrome(executable_path= chromeDriverPath)

driver.get(demoAppURL)
driver.maximize_window()
driver.implicitly_wait(5)     # 1: Applicable for all the elements on the page to load. 2: Only one time on the page can be used.

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

print(driver.current_window_handle)

handles= driver.window_handles     # returns all the handle values of opened browser windows

for handle in handles:
     driver.switch_to.window(handle)
     print(driver.title)
     if driver.title=="Frames & Windows":
          driver.close() # Close only parent browser

driver.quit()