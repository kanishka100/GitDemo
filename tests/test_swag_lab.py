import pytest

from Page_object.login_page import Login_page
from test_data.home_page_data import Test_Data
from utilities.bAse_class import Base_Class


class Test_Sauce(Base_Class):
    def test_sauce_website(self, get_login_data, get_homepage_data, get_checkout_data):
        url = 'https://www.saucedemo.com/'
        log = self.get_logger()

        self.driver.get(url)
        login_obj = Login_page(self.driver)
        log.info("Entering values in the homepage")
        login_obj.send_user_name().send_keys(get_login_data['username'])
        login_obj.send_password().send_keys(get_login_data['password'])
        # home page object is made in the login page file and is returned to the testcase
        home_page_obj = login_obj.click_login_button()

        # second page
        log.info("Getting all the products")
        products = home_page_obj.get_all_products()
        price, price_list, i = 0, [], -1
        for product in products:
            # NOTE: starting index =0
            i = i + 1
            if product.text == get_homepage_data['product_name']:

                # find all the elements individually as done here (find elements) not a single element but multiple then u can use index to move
                price = home_page_obj.product_price()[i].text
                log.info(f"Product selected: {product.text} and original price: {price}")
                price_list = price.split("$")
                home_page_obj.add_to_cart().click()
        # object of the checkout page

        check_out_obj = home_page_obj.cart_link()

        # 3rd page-checkout page
        print(check_out_obj.get_inventory_item_name())

        log.info(f"The item name selected {get_homepage_data['product_name']}")
        assert check_out_obj.get_inventory_item_name() == get_homepage_data['product_name']
        check_out_obj.click_checkout().click()

        log.info("Entering checkout details")
        check_out_obj.get_name().send_keys(get_checkout_data['first_name'])
        check_out_obj.get_lastname().send_keys(get_checkout_data['last_name'])
        check_out_obj.get_postal_code().send_keys(get_checkout_data['postal_code'])

        check_out_obj.click_continue_button().click()
        price_got = check_out_obj.get_total_price()
        print(price)

        log.info(f"The total price of product (price+tax) : {str(float(price_list[1]) + 4.00)}")
        assert price_got.split()[1].split("$")[1] == str(float(price_list[1]) + 4.00)
        check_out_obj.click_finish_button().click()

    @pytest.fixture(params=Test_Data.test_login_data)
    def get_login_data(self, request):
        return request.param

    @pytest.fixture(params=Test_Data.test_home_page_data)
    def get_homepage_data(self, request):
        return request.param

    @pytest.fixture(params=Test_Data.check_out_data)
    def get_checkout_data(self, request):
        return request.param
