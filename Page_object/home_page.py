from selenium.webdriver.common.by import By


# find_element_by_xpath("parent::a/parent::div/parent::div/div[2]/div").text
# self.driver.find_element_by_id("add-to-cart-sauce-labs-fleece-jacket").click()

#         self.driver.find_element_by_class_name("shopping_cart_link").click()
from Page_object.check_out_page import Check_Out_Page


class Home_PAge:
    products = (By.XPATH, "//div[@class='inventory_item_name']")
    price_of_product = (By.CSS_SELECTOR, ".inventory_item_price")
    adding_to_cart = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    cart = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def get_all_products(self):
        return self.driver.find_elements(*Home_PAge.products)

    def product_price(self):
        return self.driver.find_elements(*Home_PAge.price_of_product)

    def add_to_cart(self):
        return self.driver.find_element(*Home_PAge.adding_to_cart)

    def cart_link(self):
        self.driver.find_element(*Home_PAge.cart).click()
        check_out_obj = Check_Out_Page(self.driver)
        return check_out_obj

