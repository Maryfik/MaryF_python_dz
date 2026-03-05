import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


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
    # Авторизация
    login_page = LoginPage(driver)
    login_page.open()
    login_page.fill_credentials("standard_user", "secret_sauce")
    login_page.submit_login()

    # Добавление товаров в корзину
    inventory_page = InventoryPage(driver)
    inventory_page.add_items_to_cart()
    inventory_page.proceed_to_checkout()

    # Оформление заказа
    cart_page = CartPage(driver)
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Иван", "Иванов", "12345")
    checkout_page.complete_order()

    # Проверка итоговой суммы
    total_amount = checkout_page.get_total_amount()
    assert total_amount == 58.29, (
        f"Итоговая сумма должна быть $58.29, но указана {total_amount}"
        )
