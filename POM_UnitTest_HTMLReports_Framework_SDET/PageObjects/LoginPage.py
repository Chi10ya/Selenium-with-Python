from selenium.webdriver.common.by import By


class LoginPage():
    # Locators of all the elements on login page
    txtBox_username_id = "Email"
    txtBox_password_id = "Password"
    btn_login_xpath = "//input[@value='Log in']"
    link_welcome_linkText = "welcome"
    link_logout_linkText = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.txtBox_username_id).clear()
        self.driver.find_element(By.ID, self.txtBox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.txtBox_password_id).clear()
        self.driver.find_element(By.ID, self.txtBox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def clickLogOut(self):
        self.driver.find_element(By.XPATH, self.link_logout_linkText).click()