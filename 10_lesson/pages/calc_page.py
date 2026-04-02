from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """
    Класс для работы с веб-калькулятором.
    Реализует паттерн Page Object.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы калькулятора.

        :param driver: экземпляр WebDriver
        """
        self.driver = driver

    def set_delay(self, seconds: int, timeout: int = 20) -> None:
        """
        Устанавливает задержку выполнения вычислений на калькуляторе.

        :param seconds: количество секунд задержки (int)
        :param timeout: таймаут ожидания элемента (int, по умолчанию 20)
        """
        wait = WebDriverWait(self.driver, timeout)
        delay_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def press_button(self, value: str, timeout: int = 10) -> None:
        """
        Нажимает кнопку на калькуляторе (число или оператор).

        :param value: значение кнопки (str)
        :param timeout: таймаут ожидания элемента (int, по умолчанию 10)
        """
        button_xpath = f"//span[text()='{value}']"
        button = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, button_xpath))
        )
        button.click()

    def do_spinner(self, timeout: int = 10) -> None:
        """
        Ожидает исчезновения спиннера (индикатора загрузки).

        :param timeout: таймаут ожидания (int, по умолчанию 10)
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.invisibility_of_element_located((By.ID, "spinner")))

    def get_result(self, timeout: int = 10) -> str:
        """
        Получает результат вычисления с экрана калькулятора.

        :param timeout: таймаут ожидания элемента (int, по умолчанию 10)
        :return: результат вычисления (str)
        """
        result_display = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".screen"))
        )
        return result_display.text.strip()
