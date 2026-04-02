from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure


class LoginPage:
    """
    Класс для работы со страницей авторизации.
    """
    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы.
        :param driver: экземпляр WebDriver
        """
        self.driver = driver

    # Селекторы элементов
    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_button = (By.ID, "login-button")

    @allure.step("Открытие страницы авторизации")
    def open(self) -> None:
        """
        Открывает страницу авторизации.
        :return: None
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("""Заполнение формы авторизации:
                 username='{username}',
                 password='{password}'""")
    def fill_credentials(self, username: str, password: str) -> None:
        """
        Заполняет поля логина и пароля.
        :param username: имя пользователя (str)
        :param password: пароль (str)
        :return: None
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_field)
            ).send_keys(username)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_field)
            ).send_keys(password)

    @allure.step("Нажатие кнопки 'Log In'")
    def submit_login(self) -> None:
        """
        Нажимает кнопку входа.
        :return: None
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
            ).click()
