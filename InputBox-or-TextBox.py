# 8: Working with Input Box / Text Box
# 9: Working with Radio button / check boxes
# 10: Working with Dropdown list box: Selecting an option from dopdown, Count number of options / list items,  Capture all the options and print them as output

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# BrowserDriverPaths
chromeDriverPath= "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"

# App URL
appURL= "https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407"

driver= webdriver.Chrome(executable_path= chromeDriverPath)
driver.get(appURL)
driver.maximize_window()

totEditBoxes= driver.find_elements(By.CLASS_NAME, 'text_field')
print(len(totEditBoxes))

# Approach 1 - Find Element(By.ID)
fName= driver.find_element(By.ID, 'RESULT_TextField-1')
lName= driver.find_element(By.ID, 'RESULT_TextField-2')
print("Is First Name Enabled", fName.is_enabled())
fName.send_keys("Chaitanya")
print("Is Last Name Enabled", lName.is_enabled())
lName.send_keys("Mohammad")

# Approach 2 - find_element_by_id
# Approach 2 - find_element_by_id
driver.find_element_by_id("RESULT_TextField-3").send_keys("123456789")

# Dropdown list box.
drpDownOptions= driver.find_element_by_id("RESULT_RadioButton-9")
drp= Select(drpDownOptions)

# Select by Visible text
drp.select_by_visible_text('Morning')

# Select by Index
drp.select_by_index(2) # Afternoon

# Select by Value
drp.select_by_value("Radio-2")

# Count number of options / list items
print(len(drp.options))

# Capture all the options and print them as output
all_options= drp.options

for option in all_options:
     print(option.text)

# Radio Button
rdbtnStatus=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print("Radio Button Status is : ", rdbtnStatus)
driver.find_element_by_id("RESULT_RadioButton-7_0").click()           # Here click is not working.

# Check boxes
driver.find_element_by_id("RESULT_CheckBox-8_0").click()
driver.find_element_by_id("RESULT_CheckBox-8_6").click()
chkBoxStatus=driver.find_element_by_id("RESULT_CheckBox-9_0").is_selected()
print("Check Box status is : ", chkBoxStatus)

driver.quit()







