from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
            ).click()
