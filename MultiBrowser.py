# Tutorials

# 3: Basic methods: driver.title, driver.current_url, driver.close(), driver.quit()
# 4: Navigational commands: driver.back(), driver.forward()
# 5: Conditional Commands is_displayed, is_enabled, is_selected
# 6 & 7: Waits : Implicit Wait, Explicit Wait. Implicit wait is on time based. Explicit wait is on condition not on time. It should be applied on the element which is taking time
# 8: Working with Input Box / Text Box
# 9: Working with Radio button / check boxes
# 10: Working with dropdown list box.
# 11: Working with links: How many links present (Count), Print all available links, Clicking on the link
# 12: How to handle Alerts / Popups || Switching to Alerts / Popups
# 13: How to handle Frames | IFrame | Switch between frames ==> # driver.switch_to.frame("frame name"),  # driver.switch_to.default_content()
# 14: How to handle browser windows / Switch between windows ==> driver.current_window, driver.window_handles
# 15: Working with HTMl / WebTable
# 16: How to scroll webpages in selenium : Page by pixel => driver.execute_script("window.scrollBy(0, 500)", "")
#                                          Page till element found => driver.execute_script("arguments[0].scrollIntoView();", Element)
#                                          Scroll to end of the page => driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
#: 17, 18: Handle Mouse Actions:  17: Mouse Hover, 18: Double Click, 19: Right Click, 20: Drag and Drop.
#                                        actions=ActionChains(driver)
# 17                                       actions.move_to_element(parent menu name).move_to_element(sub menu name).move_to_element(child menu name).click().perform()
# 18                                       actions.double_click(element).perform()
# 19                                       actions.context_click(element).perform()
# 20                                       actions.drag_and_drop(sourceElement, targetElement).perform()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# BrowserDriverPaths
chromeDriverPath= "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"
fireFoxDriverPath= "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\geckodriver.exe"
ieDriverPath= "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\IEDriverServer.exe"

flightAppURL= "http://newtours.demoaut.com"
demoAppURL= "http://demo.automationtesting.in/Windows.html"

# For Chrome browser
driver= webdriver.Chrome(executable_path= chromeDriverPath)

# For FireFox browser
#driver= webdriver.Firefox(executable_path= fireFoxDriverPath)

# For IE browser
#driver= webdriver.Ie(executable_path= ieDriverPath)

driver.get(flightAppURL)
driver.maximize_window()
driver.implicitly_wait(5)     # 1: Applicable for all the elements on the page to load. 2: Only one time on the page can be used.

print(driver.title)
assert "Welcom: Mercury Tours" in driver.title    # Assert statement
print(driver.current_url)


# This button resides in demoAppURL application
# xPath of the button //*[@class='btn btn-info'] or "//*[@id='Tabbed']/a/button"
#driver.find_element_by_xpath("//*[@class='btn btn-info']").click()    # This button resides in demoAppURL application

# The below code is for Flight Demo Application

userName= driver.find_element_by_name("userName")
print("Is Username Editbox Displayed", userName.is_displayed())
print("Is Username Editbox Enabled", userName.is_enabled())

password= driver.find_element_by_name("password")
print("Is Password edit box Displayed", password.is_displayed())
print("Is Password edit box Enabled", password.is_enabled())

userName.send_keys("mercury")
password.send_keys("mercury")
driver.find_element_by_name("login").click()

print(driver.title)

rbtnRoundTrip= driver.find_element_by_css_selector("input[value=roundtrip]")
print("Is radio button Round trip Selected", rbtnRoundTrip.is_selected())

rbtnOneWayTrip= driver.find_element_by_css_selector("input[value=oneway]")
print("Is radio button Oneway Selected", rbtnOneWayTrip.is_selected())

# driver.back() ==> driver.back() is not functioning. Instead use the below code.
driver.execute_script("window.history.go(-1)")

#driver.forward()


# driver.close()    # It closes only the currently focused browser window
driver.quit()       # It closes all the browser windows






