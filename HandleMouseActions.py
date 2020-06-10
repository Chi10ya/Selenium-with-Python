#: 17, 18: Handle Mouse Actions:  17: Mouse Hover, 18: Double Click, 19: Right Click, 20: Drag and Drop.
#                                        actions=ActionChains(driver)
# 17                                       actions.move_to_element(parent menu name).move_to_element(sub menu name).move_to_element(child menu name).click().perform()
# 18                                       actions.double_click(element).perform()
# 19                                       actions.context_click(element).perform()
# 20                                       actions.drag_and_drop(sourceElement, targetElement).perform()
# 21: How to upload a file.
# 22: How to download files using Chrome browser
# 23:
# 24 : How to read data from MS-Excel using OpenPyXL | Data Driven testing.



from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.chrome.options import Options

# Tut 22: How to download files using Chrome browser. The below chromeOptions lines are for
# downloading the file at my desired location by changing the download location in chrome browser.

chromeOptions = Options()
chromeOptions.add_experimental_option("pref", {"download.default_directory": "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\SDET_SeleniumWithPython"})

# Tut 23: How to download files using FireFox browser. The below lines are for
# Downloading the file at my desired location by changing the download location in FireFox browser.
# FireFox options / preferences settings.

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf") # Mime type
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\SDET_SeleniumWithPython")
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("pdfjs.disabled", True)

# ------------------------------------------------------------------------------------------------------------------

# ***************** Tut 17: Mouse Hover

# BrowserDriverPaths
chromeDriverPath = "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"

demoAppURL = "https://opensource-demo.orangehrmlive.com"

# For Chrome browser
driver = webdriver.Chrome(executable_path = chromeDriverPath)

driver.get(demoAppURL)
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
print(driver.title)

adminMenu = driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
usrMgmtMenu = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
usersMenu = driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")

# Mouse Hover
actions = ActionChains(driver)
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

# ****************** Tut 19: Handle Mouse Actions | Right Click Action

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
assert "LoginPage" in driver.title

sourceElement= driver.find_element_by_xpath("//*[@id='box3']")
targetElement= driver.find_element_by_xpath("//*[@id='box103']")

actions= ActionChains(driver)
actions.drag_and_drop(sourceElement, targetElement).perform()       # For drag and drop
time.sleep(5)

driver.quit()

# **************** Tut 21: How to upload a file.

# BrowserDriverPaths
chromeDriverPath= "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"

demoAppURL= "https://testautomationpractice.blogspot.com/"

# For Chrome browser
driver= webdriver.Chrome(executable_path= chromeDriverPath)

driver.get(demoAppURL)
driver.maximize_window()
driver.implicitly_wait(5)
print(driver.title)

driver.switch_to.frame("frame-one1434677811")
driver.find_element_by_id("RESULT_FileUpload-10").send_keys("C:\\Users\\chaitanya.mohammad\\Desktop\\python_selenium_file_upload.txt")

# *****************Tut 22: How to download files using Chrome browser

# Downloading at default location.
# BrowserDriverPaths
chromeDriverPath= "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"

demoAppURL= "http://demo.automationtesting.in/FileDownload.html"

# For Chrome browser
driver= webdriver.Chrome(executable_path= chromeDriverPath)

driver.get(demoAppURL)
driver.maximize_window()
driver.implicitly_wait(5)
print(driver.title)

# Download Text File
driver.find_element_by_id("textbox").send_keys("Testing the download feature text file")
driver.find_element_by_id("createTxt").click() # Generate File button
driver.find_element_by_id("link-to-download").click() # Download link

# Download PDF file
driver.find_element_by_id("pdfbox").send_keys("testing pdf")
driver.find_element_by_id("createPdf").click()  # Generate File Button
driver.find_element_by_id("pdf-link-to-download").click() # Download link


# Downloading the file at my desired location by changing the download location in chrome browser.

# BrowserDriverPaths
chromeDriverPath= "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"

demoAppURL = "http://demo.automationtesting.in/FileDownload.html"

# For Chrome browser
driver = webdriver.Chrome(executable_path= chromeDriverPath, chrome_options=chromeOptions)

driver.get(demoAppURL)
driver.maximize_window()
driver.implicitly_wait(5)
print(driver.title)

# Download Text File
driver.find_element_by_id("textbox").send_keys("Testing the download feature text file")
driver.find_element_by_id("createTxt").click() # Generate File Button
driver.find_element_by_id("link-to-download").click()

# Download PDF file
driver.find_element_by_id("pdfbox").send_keys("testing pdf")
driver.find_element_by_id("createPdf").click() # Generate File Button
driver.find_element_by_id("pdf-link-to-download").click()


# *****************Tut 23: How to download files using FireFox browser

# Downloading the file at my desired location by changing the download location in FireFox browser.

# BrowserDriverPaths
fireFoxDriverPath = "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\geckodriver.exe"

demoAppURL= "http://demo.automationtesting.in/FileDownload.html"

# For FireFox browser
driver = webdriver.Firefox(executable_path= fireFoxDriverPath, firefox_profile=fp)

driver.get(demoAppURL)
driver.maximize_window()
driver.implicitly_wait(5)
print(driver.title)

# Download Text File
driver.find_element_by_id("textbox").send_keys("Testing the download feature text file")
driver.find_element_by_id("createTxt").click() # Generate File Button
driver.find_element_by_id("link-to-download").click()

# Download PDF file
driver.find_element_by_id("pdfbox").send_keys("testing pdf")
driver.find_element_by_id("createPdf").click() # Generate File Button
driver.find_element_by_id("pdf-link-to-download").click()







