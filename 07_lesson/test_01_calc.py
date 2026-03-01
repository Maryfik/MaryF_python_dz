import pytest
from selenium import webdriver
from pages.calc_page import CalculatorPage


@pytest.fixture(scope="module")
def driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()


def test_calculator_result(driver):
    calc_page = CalculatorPage(driver)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Установка задержки
    calc_page.set_delay(45)

    # Выполнение вычисления: 7 + 8
    calc_page.press_number(7)
    calc_page.press_operator('+')
    calc_page.press_number(8)
    calc_page.press_operator('=')

    calc_page.do_spinner(50)

    # Получение результата
    result = calc_page.get_result()

    # Проверка результата
    assert result.strip() == "15", (
        f"Полученный текст {result}, ожидается '15'")
