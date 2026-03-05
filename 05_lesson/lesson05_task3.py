from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")

time.sleep(2)

input_field = driver.find_element(By.TAG_NAME, 'input')

# Вводим текст "Sky"
input_field.send_keys('Sky')
time.sleep(5)

# Очищаем поле ввода
input_field.clear()

# Вводим новый текст "Pro"
input_field.send_keys('Pro')

time.sleep(3)

driver.quit()
