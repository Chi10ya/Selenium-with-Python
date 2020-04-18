# 11: Working with links: How many links present (Count), Print all available links, Clicking on the link

from selenium import webdriver
from selenium.webdriver.common.by import By


# BrowserDriverPaths
chromeDriverPath= "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"

# App URL
flightAppURL= "http://newtours.demoaut.com"

driver= webdriver.Chrome(executable_path= chromeDriverPath)
driver.maximize_window()
driver.get(flightAppURL)
print(driver.title)

# To display total # of links present
totLinks= driver.find_elements(By.TAG_NAME, "a")
print("Number of links present : ", len(totLinks))

# For to print all the available links text
for link in totLinks:
     print(link.text)

# Clicking on the link by LINK TEXT
driver.find_element(By.LINK_TEXT, "REGISTER").click()
print(driver.title)

# driver.back() ==> driver.back() is not functioning. Instead use the below code.
driver.execute_script("window.history.go(-1)")
print(driver.title)

# Clicking on the link by PARTIAL LINK TEXT
driver.find_element(By.PARTIAL_LINK_TEXT, "CONTACT").click()
driver.execute_script("window.history.go(-1)")
print(driver.title)
driver.execute_script("window.history.go(1)")
print(driver.title)

driver.quit()






