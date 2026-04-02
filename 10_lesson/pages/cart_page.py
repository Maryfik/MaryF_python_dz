from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class CartPage:
    """
    Класс для работы со страницей корзины.
    """
    def __init__(self, driver: WebDriver):
        self.driver = driver

    checkout_button = (By.ID, 'checkout')

    @allure.step("Переход к оформлению заказа")
    def checkout(self) -> None:
        """
        Нажимает кнопку 'Checkout'.
        :return: None
        """
        self.driver.find_element(*self.checkout_button).click()
