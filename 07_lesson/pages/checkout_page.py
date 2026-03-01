from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    first_name_input = (By.ID, 'first-name')
    last_name_input = (By.ID, 'last-name')
    postal_code_input = (By.ID, 'postal-code')
    continue_button = (By.ID, 'continue')
    total_amount_label = (By.CLASS_NAME, 'summary_total_label')

    # Заполнение полей адреса доставки
    def fill_form(self, first_name: str, last_name: str, postal_code: str):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(
            *self.postal_code_input).send_keys(postal_code)

    # Завершение оформления заказа
    def complete_order(self):
        self.driver.find_element(*self.continue_button).click()

    # Получает итоговую стоимость заказа
    def get_total_amount(self):
        return float(self.driver.find_element(
            *self.total_amount_label).text.split('$')[1])
