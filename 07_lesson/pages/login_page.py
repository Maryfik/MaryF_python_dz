from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Селекторы элементов
    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def open(self):
        """Открывает страницу"""
        self.driver.get("https://www.saucedemo.com/")

    def fill_credentials(self, username: str, password: str):
        """Заполняет форму авторизации"""
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)

    def submit_login(self):
        """Нажимает кнопку 'Log In'"""
        self.driver.find_element(*self.login_button).click()
