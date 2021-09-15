from selenium.webdriver.common.by import By


class Check_Out_Page:
    inventory_item = (By.CLASS_NAME, "inventory_item_name")
    checkout_button = (By.NAME, "checkout")
    firstname = (By.NAME, "firstName")
    lastname = (By.NAME, "lastName")
    postal_code = (By.NAME, "postalCode")

    continue_button = (By.NAME, "continue")
    total_price = (By.CLASS_NAME, "summary_total_label")
    finish_button = (By.NAME, "finish")

    def __init__(self, driver):
        self.driver = driver

    def get_inventory_item_name(self):
        return self.driver.find_element(*Check_Out_Page.inventory_item).text

    def click_checkout(self):
        return self.driver.find_element(*Check_Out_Page.checkout_button)

    def get_name(self):
        return self.driver.find_element(*Check_Out_Page.firstname)

    def get_lastname(self):
        return self.driver.find_element(*Check_Out_Page.lastname)

    def get_postal_code(self):
        return self.driver.find_element(*Check_Out_Page.postal_code)

    def click_continue_button(self):
        return self.driver.find_element(*Check_Out_Page.continue_button)

    def get_total_price(self):
        return self.driver.find_element(*Check_Out_Page.total_price).text

    def click_finish_button(self):
        return self.driver.find_element(*Check_Out_Page.finish_button)
