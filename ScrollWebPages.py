# 16: How to scroll webpages in selenium :
# 1: Page by pixel => driver.execute_script("window.scrollBy(0, 500)", "")
# 2: Page till element found => driver.execute_script("arguments[0].scrollIntoView();", Element)
# 3: Scroll to end of the page => driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import *

# BrowserDriverPaths
chromeDriverPath= "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"

demoAppURL= "https://www.countries-ofthe-world.com/flags-of-the-world.html"

# For Chrome browser
driver= webdriver.Chrome(executable_path= chromeDriverPath)

driver.get(demoAppURL)
driver.maximize_window()
driver.implicitly_wait(5)

# 1: Page by pixel => driver.execute_script("window.scrollBy(0, 500)","")
driver.execute_script("window.scrollBy(0, 1000)", "")   # From 0 pixel to 1000 pixel of the page.
driver.execute_script("window.scrollBy(1000, 0)", "")   # From 1000 pixel to 0 pixel of the page.

# 2: Page till element found => driver.execute_script("arguments[0].scrollIntoView();", Element)
IRLFlag= driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[90]/td[1]/img")
flagName= driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[90]/td[1]/img").get_attribute("alt")
print("Country Name : ", flagName)
driver.execute_script("arguments[0].scrollIntoView();", IRLFlag)

# 3: Scroll to end of the page => driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

driver.quit()