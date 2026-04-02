from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
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
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)

    @allure.step("Нажатие кнопки 'Log In'")
    def submit_login(self) -> None:
        """
        Нажимает кнопку входа.
        :return: None
        """
        self.driver.find_element(*self.login_button).click()
