from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class InventoryPage:
    """
    Класс для работы со страницей каталога товаров.
    """
    def __init__(self, driver: WebDriver):
        self.driver = driver

    backpack_btn = (
        By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    t_shirt_btn = (
        By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    onesie_btn = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
    cart_icon = (By.CLASS_NAME, 'shopping_cart_link')

    @allure.step("Добавление товаров в корзину")
    def add_items_to_cart(self) -> None:
        """
        Добавляет три товара в корзину.
        :return: None
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.backpack_btn)
            ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.t_shirt_btn)
            ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.onesie_btn)
            ).click()

    @allure.step("Переход к оформлению заказа")
    def proceed_to_checkout(self) -> None:
        """
        Переходит на страницу корзины.
        :return: None
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_icon)
            ).click()
