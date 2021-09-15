from selenium.webdriver.common.by import By

from Page_object.home_page import Home_PAge


class Login_page:
    username = (By.NAME, "user-name")
    password = (By.NAME, "password")
    loginbutton = (By.NAME, "login-button")

    def __init__(self, driver):
        self.driver = driver

    def send_user_name(self):
        return self.driver.find_element(*Login_page.username)

    def send_password(self):
        return self.driver.find_element(*Login_page.password)

    def click_login_button(self):
        self.driver.find_element(*Login_page.loginbutton).click()
        home_page_obj = Home_PAge(self.driver)
        return home_page_obj
