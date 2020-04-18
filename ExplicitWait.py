from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC     # this has to be used for Explict wait
from selenium.webdriver.support.ui import WebDriverWait     # this has to be used for Explicit wait

# BrowserDriverPaths
chromeDriverPath= "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"
# fireFoxDriverPath= "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\geckodriver.exe"
# ieDriverPath= "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\IEDriverServer.exe"

flightAppURL= "https://www.expedia.com/"

driver= webdriver.Chrome(executable_path= chromeDriverPath)
driver.get(flightAppURL)
driver.maximize_window()
driver.implicitly_wait(5)

# Approach 1: for to find the element by direct method find_element_by_id
driver.find_element_by_id("tab-flight-tab-hp").click()

# Approach 2: for to find the element by using By.Attribute (Java - Selenium style)
driver.find_element(By.ID, "tab-flight-tab-hp").click()
driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
driver.find_element(By.ID, "flight-departing-hp-flight").clear()
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("02/07/2020")
driver.find_element(By.ID, "flight-returning-hp-flight").clear()
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("24/07/2020")
driver.find_element(By.XPATH, "//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()

# The below two lines are for Explicitly wait
expliWait= WebDriverWait(driver, 10)
element= expliWait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stopFilter_stops-0']")))
element.click()

driver.quit()




