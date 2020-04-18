# 13: How to handle Frames | IFrame | Switch between frames

# driver.switch_to.frame("frame name")
# driver.switch_to.default_content()

from selenium import webdriver
from selenium.webdriver.common.by import By


# BrowserDriverPaths
chromeDriverPath= "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"

# App URL
appURL= "https://seleniumhq.github.io/selenium/docs/api/java/index.html"

driver= webdriver.Chrome(executable_path= chromeDriverPath)
driver.maximize_window()
driver.get(appURL)

# packageListFrame
driver.switch_to.frame("packageListFrame")   # First Frame
driver.find_element_by_link_text("org.openqa.selenium").click()

driver.switch_to.default_content()      # This is for to switch back to the main frame

driver.switch_to.frame("packageFrame")  # Second Frame
driver.find_element_by_link_text("WebDriver").click()

driver.switch_to.default_content()      # This is for to switch back to the main frame

driver.switch_to.frame("classFrame")    # Third Frame
driver.find_element_by_xpath("html/body/div[1]/ul/li[5]").click()

driver.current_window_handle()

driver.quit()

