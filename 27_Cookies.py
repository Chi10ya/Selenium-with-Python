# ***************  27: Working with cookies
# cookies = driver.get_cookies()
# driver.add_cookie(cookie)

# ***************  28: Capture Screen shots
    #  save_screenshot('filename')
    # get_screenshot_as_file('filename')

# ************** 29: Logging | Generate Log File

"""
    Operations on Cookies
        1: Capture all cookies from browser -- driver.get_cookies()
        2: Count number of cookies
        3: Read cookies pairs
        4: Adding new cookies
        5: Deleting specific cookies by using name of cookie
        6: Deleting all the cookies
"""

from selenium import  webdriver
import time
import logging

chromeDriverPath = "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"
flightAppURL = "http://newtours.demoaut.com"


driver = webdriver.Chrome(executable_path= chromeDriverPath)
driver.get(flightAppURL)

# Capture all cookies from browser
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# ------------------ Adding a new cookie to the browser

print("******** Adding a new cookie to the browser")
cookie = {'name':'Chi10yaCookie', 'value':'7224212224'}

driver.add_cookie(cookie)
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# ----------------- Deleting Cookie
print("******** Deleting a cookie to the browser")
driver.delete_cookie(cookie)
time.sleep(3)
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# ----------------- Deleting all cookies

print("******** Deleting all cookies to the browser")
driver.delete_all_cookies()
time.sleep(3)
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# ***************  28: Capture Screen shots

driver.get(flightAppURL)
time.sleep(4)
driver.save_screenshot("C:\\ScreenShots-nd-Logs\\home.png") # this method supports any format
driver.get_screenshot_as_file("C:\\ScreenShots-nd-Logs\\homePage2.png") # This method only supports .png format


# **************** 29: Logging | Generate Log file
# Approach 1 - without creating an object
logging.basicConfig(
                    filename = "C:\\ScreenShots-nd-Logs\\test.log",
                    format = '%(asctime)s: %(levelname)s: %(message)s',
                    datefmt = '%d-%m-%Y %I:%M:%S %p',
                    level=logging.DEBUG
                    )

logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")

# Approach 2 - by creating an object
# Refer LoggingUtil.py file


driver.quit()




