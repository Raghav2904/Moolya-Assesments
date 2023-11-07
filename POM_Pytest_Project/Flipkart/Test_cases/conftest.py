import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope='class')
def setup(request):
    driver=webdriver.Chrome()
    driver.get('https://www.flipkart.com/')
    driver.maximize_window()
    driver.find_element(By.XPATH, "//span[@class='_30XB9F']").click()
    request.cls.driver=driver
    yield
    driver.close()