import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class Actual_product_page:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self,product_name):
        title_of_page = self.driver.title
        print(title_of_page)
        assert product_name in title_of_page
        time.sleep(5)

    def add_to_cart(self):
        win_hands = self.driver.window_handles
        self.driver.switch_to.window(win_hands[-1])
        self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]').click()
        time.sleep(5)



