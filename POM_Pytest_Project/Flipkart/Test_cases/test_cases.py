import time
import pytest
from selenium.webdriver.common.by import By
from Flipkart.Pages.actual_product_page import Actual_product_page
from Flipkart.Pages.flipkart_home_page import Home_page
from Flipkart.Pages.product_page import Product_page


@pytest.mark.usefixtures('setup')
class Test_Flipkart:

    def test_get_title(self):
        if 'Flipkart' in self.driver.page_source:
            self.driver.save_screenshot(".\\Screen_shots\\Home_page.png")
        else:
            print("Flipkart is not present")

    def test_searching_product(self):
        hp = Home_page(self.driver)
        hp.search_product("MOTOROLA g54 5G (Mint Green, 256 GB)")

    def test_verify_product_name(self):
        pn = Product_page(self.driver)
        pn.click_on_product()

    def test_product_page(self):
         pp = Actual_product_page(self.driver)
         pp.get_title('MOTOROLA G54 5G')
         pp.add_to_cart()

    def test_get_cart_product(self):
        if 'MOTOROLA g54 5G (Mint Green, 256 GB)' in self.driver.page_source:
            self.driver.save_screenshot(".\\Screen_shots\\Cart_page.png")
        else:
            print("Flipkart is not present")














