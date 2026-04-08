import pytest
import allure
from selenium import webdriver
from pages.calc_page import CalculatorPage


@pytest.fixture(scope="module")
def driver():
    """
    Фикстура для управления драйвером браузера.
    """
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()


@allure.feature("Функциональность калькулятора")
@allure.title("Проверка вычисления суммы 7 + 8")
@allure.description("""Тест проверяет корректность работы калькулятора
                    при сложении двух чисел с задержкой.""")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_result(driver):
    """
    Основной тестовый сценарий.
    """
    calc_page = CalculatorPage(driver)

    with allure.step("Открытие страницы калькулятора"):
        driver.get(
            "https://bonigarcia.dev/selenium"
            "-webdriver-java/slow-calculator.html")

    @allure.step("Установка задержки вычислений на 45 секунд")
    def step_set_delay():
        calc_page.set_delay(45)

    @allure.step("Ввод первого числа '7'")
    def step_press_number_7():
        calc_page.press_button('7')

    @allure.step("Выбор оператора '+'")
    def step_press_operator_plus():
        calc_page.press_button('+')

    @allure.step("Ввод второго числа '8'")
    def step_press_number_8():
        calc_page.press_button('8')

    @allure.step("Нажатие кнопки '=' для выполнения вычисления")
    def step_press_operator_equals():
        calc_page.press_button('=')

    @allure.step("Ожидание завершения загрузки (исчезновения спиннера)")
    def step_wait_spinner():
        calc_page.do_spinner(50)

    @allure.step("Получение результата вычисления")
    def step_get_result():
        return calc_page.get_result()

    # Выполнение шагов теста
    step_set_delay()
    step_press_number_7()
    step_press_operator_plus()
    step_press_number_8()
    step_press_operator_equals()
    step_wait_spinner()

    result = step_get_result()

    # Проверка результата (разметка через контекстный менеджер)
    with allure.step("Проверка результата вычисления"):
        assert result == "15", f"Ожидалось '15', но получено '{result}'"
