from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def checkout(self):
        checkout_button = self.driver.find_element(By.ID, 'checkout')
        checkout_button.click()
