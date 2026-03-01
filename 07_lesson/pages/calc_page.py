from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver

    # Установка задержки
    def set_delay(self, seconds):
        wait = WebDriverWait(self.driver, 20)
        delay_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    # Выполнение вычисления: 7 + 8
    def press_number(self, number):
        button_xpath = f"//span[text()='{number}']"
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, button_xpath))
        )
        button.click()

    def press_operator(self, operator):
        button_xpath = f"//span[text()='{operator}']"
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, button_xpath))
        )
        button.click()

    def do_spinner(self, seconds):
        wait = WebDriverWait(self.driver, seconds)
        wait.until(EC.invisibility_of_element_located((By.ID, "spinner")))

    def get_result(self):
        result_display = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".screen"))
        )
        return result_display.text.strip()
