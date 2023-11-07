from selenium.webdriver.common.by import By


class Home_page:
    def __init__(self,driver):
        self.driver = driver

    searchbar_locator = "//input[@class='Pke_EE']"
    search_button_locator = "//button[@title='Search for Products, Brands and More']//*[name()='svg']"

    def search_product(self,product_name):
        self.driver.find_element(By.XPATH,self.searchbar_locator).send_keys(product_name)
        self.driver.find_element(By.XPATH,self.search_button_locator).click()


    #
    # def get_searchbar(self):
    #     return self.driver.find_element(By.XPATH,self.searchbar_locator)

    # def get_search_button(self):
    #     return self.driver.find_element(By.XPATH,self.search_button_locator)
    #
    # def send_keys_in_searchbar(self,product_name):
    #     self.get_searchbar().send_keys(product_name)
    #
    # def click_on_search_button(self):
    #     self.get_search_button().click()






    # def searching_product(self,product):
    #     self.driver.find_element(By.XPATH, "//input[@class='Pke_EE']").send_keys(product)
    #     self.driver.find_element(By.XPATH, "//button[@class='_2iLD__']").click()