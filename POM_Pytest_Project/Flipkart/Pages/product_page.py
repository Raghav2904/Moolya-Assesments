import time

from selenium.webdriver.common.by import By


class Product_page:
    def __init__(self,driver):
        self.driver = driver

    product_locator = "//div[normalize-space()='MOTOROLA g54 5G (Mint Green, 256 GB)']"

    def click_on_product(self):
        self.driver.find_element(By.XPATH,self.product_locator).click()



