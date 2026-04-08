from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckoutPage:
    """
    Класс для работы со страницей оформления заказа.
    """
    def __init__(self, driver: WebDriver):
        self.driver = driver

    first_name_input = (By.ID, 'first-name')
    last_name_input = (By.ID, 'last-name')
    postal_code_input = (By.ID, 'postal-code')
    continue_button = (By.ID, 'continue')
    total_amount_label = (By.CLASS_NAME, 'summary_total_label')

    @allure.step("""Заполнение формы доставки:
                 first_name='{first_name}',
                 last_name='{last_name}',
                 postal_code='{postal_code}'""")
    def fill_form(
         self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму доставки.
        :param first_name: имя (str)
        :param last_name: фамилия (str)
        :param postal_code: почтовый индекс (str)
        :return: None
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name_input)
            ).send_keys(first_name)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.last_name_input)
            ).send_keys(last_name)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.postal_code_input)
            ).send_keys(postal_code)

    @allure.step("Завершение оформления заказа")
    def complete_order(self) -> None:
        """
        Нажимает кнопку 'Continue'.
        :return: None
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_button)
            ).click()

    @allure.step("Получение итоговой суммы заказа")
    def get_total_amount(self) -> float:
        """
        Возвращает итоговую сумму заказа.
        :return: итоговая сумма (float)
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.total_amount_label)
        )
        text = element.text
        return float(text.split('$')[1])
