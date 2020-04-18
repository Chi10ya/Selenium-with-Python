#: 17: Handle Mouse Actions:  Mouse Hover, Double Click, Right Click, Drag and Drop.

from selenium import webdriver
from selenium.webdriver import ActionChains
import time

# BrowserDriverPaths
chromeDriverPath= "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"

demoAppURL= "https://opensource-demo.orangehrmlive.com"

# For Chrome browser
driver= webdriver.Chrome(executable_path= chromeDriverPath)

driver.get(demoAppURL)
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
print(driver.title)

adminMenu= driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
usrMgmtMenu= driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
usersMenu= driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")

# ***************** Tut 17: Mouse Hover

actions= ActionChains(driver)
actions.move_to_element(adminMenu).move_to_element(usrMgmtMenu).move_to_element(usersMenu).click().perform()

driver.quit()

# ****************** Tut 18: Double Click

# BrowserDriverPaths
chromeDriverPath= "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"

demoAppURL= "https://testautomationpractice.blogspot.com/"

# For Chrome browser
driver= webdriver.Chrome(executable_path= chromeDriverPath)

driver.get(demoAppURL)
driver.maximize_window()
driver.implicitly_wait(5)
print(driver.title)

btnCopyText= driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

actions=ActionChains(driver)
actions.double_click(btnCopyText).perform()              # For Double click
copiedText= driver.find_element_by_xpath("//*[@id='field2']")
print(copiedText.get_attribute('value'))

driver.quit()

# ****************** Tut 19: Double Click

# BrowserDriverPaths
chromeDriverPath= "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"

demoAppURL= "http://swisnl.github.io/jQuery-contextMenu/demo.html"

# For Chrome browser
driver= webdriver.Chrome(executable_path= chromeDriverPath)

driver.get(demoAppURL)
driver.maximize_window()
driver.implicitly_wait(5)
print(driver.title)

btnRightClickMe= driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")

actions=ActionChains(driver)
actions.context_click(btnRightClickMe).perform()       # For right click

driver.quit()

# ****************** Tut 20: Drag and Drop element

# BrowserDriverPaths
chromeDriverPath= "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"

demoAppURL= "http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"

# For Chrome browser
driver= webdriver.Chrome(executable_path= chromeDriverPath)

driver.get(demoAppURL)
driver.maximize_window()
driver.implicitly_wait(5)
print(driver.title)

sourceElement= driver.find_element_by_xpath("//*[@id='box3']")
targetElement= driver.find_element_by_xpath("//*[@id='box103']")

actions=ActionChains(driver)
actions.drag_and_drop(sourceElement, targetElement).perform()       # For drag and drop
time.sleep(5)

driver.quit()