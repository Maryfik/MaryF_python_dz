from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    backpack_btn = (
        By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    t_shirt_btn = (
        By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    onesie_btn = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
    cart_icon = (By.CLASS_NAME, 'shopping_cart_link')

    def add_items_to_cart(self):
        self.driver.find_element(*self.backpack_btn).click()
        self.driver.find_element(*self.t_shirt_btn).click()
        self.driver.find_element(*self.onesie_btn).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self.cart_icon).click()
