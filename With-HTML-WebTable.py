# 15: Working with HTMl / WebTable

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# BrowserDriverPaths
chromeDriverPath= "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"

demoAppURL= "file://C://Users//chaitanya.mohammad//PycharmProjects//SDET_SeleniumWithPython//SampleHTMl-or-WebTable.html"

# For Chrome browser
driver= webdriver.Chrome(executable_path= chromeDriverPath)

driver.get(demoAppURL)
driver.maximize_window()
driver.implicitly_wait(5)

rows= len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))      # Count number of rows
cols= len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th"))     # Count number of columns

print(rows)
print(cols)

print("Product"+"   "+"Article"+"  "+"Price")

for r in range(2, rows+1):
     for c in range(1, cols+1):
          value= driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
          print(value, end='  ')
     print()

