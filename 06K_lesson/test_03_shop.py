import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="module")
def driver():
    firefox_options = Options()
    driver = webdriver.Firefox(
        options=firefox_options, service=webdriver.firefox.service.Service(
            GeckoDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.set_script_timeout(10)
    yield driver
    driver.quit()


def test_shopping_flow(driver):

    driver.get('http://www.saucedemo.com/')
    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys('standard_user')
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('secret_sauce', Keys.ENTER)

    WebDriverWait(driver, 10).until(EC.url_contains('/inventory.html'))
    backpack_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']"))
    )
    backpack_btn.click()

    t_shirt_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))
    )

    t_shirt_btn.click()
    onesie_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']"))
    )
    onesie_btn.click()

    # Корзина
    cart_icon = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_icon.click()

    # Оформляем заказ
    checkout_button = driver.find_element(By.ID, 'checkout')
    checkout_button.click()

    # Заполняем данные
    first_name_input = driver.find_element(By.ID, 'first-name')
    first_name_input.send_keys('Мария')
    last_name_input = driver.find_element(By.ID, 'last-name')
    last_name_input.send_keys('Французова')
    postal_code_input = driver.find_element(By.ID, 'postal-code')
    postal_code_input.send_keys('12345')
    continue_button = driver.find_element(By.ID, 'continue')
    continue_button.click()

    # Получаем итоговую сумму
    total_amount_text = driver.find_element(
        By.CLASS_NAME, 'summary_total_label').text
    total_amount = float(total_amount_text.split('$')[1])

    # Проверяем итоговую сумму
    assert total_amount == 58.29, (
        f"Итоговая сумма должна быть $58.29, но указана {total_amount}"
    )
