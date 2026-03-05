import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

RED_COLOR = "rgba(132, 32, 41, 1)"
GREEN_COLOR = "rgba(15, 81, 50, 1)"


@pytest.fixture(scope='module')
def edge_driver():
    options = Options()
    driver = webdriver.Edge(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.set_script_timeout(10)
    yield driver
    driver.quit()


def test_form_submission(edge_driver):
    driver = edge_driver
    edge_driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "zip-code").send_keys("")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    submit_button = driver.find_element(
        By.CSS_SELECTOR, "button.btn.btn-outline-primary")
    submit_button.click()

    zip_field = driver.find_element(By.ID, "zip-code")
    actual_zip_color = zip_field.value_of_css_property("color")

    assert actual_zip_color == RED_COLOR, (
        f"Поле Zip code должно быть красным."
        f"Ожидался: {RED_COLOR}, получен: {actual_zip_color}"
    )

    green_field_nam = [
        "first-name", "last-name", "address",
        "e-mail", "phone", "city", "country", "job-position", "company"]

    for field_name in green_field_nam:
        element = driver.find_element(By.ID, field_name)
        actual_color = element.value_of_css_property("color")

        assert actual_color == GREEN_COLOR, (
            f"Поле {field_name} должно быть зеленым."
            f"Ожидался {GREEN_COLOR}, получен {actual_color}"
        )
