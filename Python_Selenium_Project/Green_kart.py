import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.maximize_window()
print(driver.title)

driver.find_element(By.XPATH,"//input[@type='search']").send_keys('ca')
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div/div[1]/div[3]/button').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div/div[2]/div[3]/button').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div/div[3]/div[3]/button').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div/div[4]/div[3]/button').click()

driver.find_element(By.XPATH,'//*[@id="root"]/div/header/div/div[3]/a[4]/img').click()

driver.find_element(By.XPATH,'//*[@id="root"]/div/header/div/div[3]/div[2]/div[2]/button').click()
time.sleep(5)

value = driver.find_elements(By.XPATH,"//table[@class='cartTable']//tbody/tr/td[5]")
b=0
for i in value:
    b=b+int(i.text)

total_value=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/span[1]')
x=total_value.text

if str(b)==x:
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/button').click()


dd = Select(driver.find_element(By.XPATH,'//select[@style="width: 200px;"]'))
dd.select_by_visible_text('India')
driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/input').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/button').click()

if "Thank you" in driver.page_source:
    print('Test completed')


