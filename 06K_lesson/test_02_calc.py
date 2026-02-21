import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()


def test_calculator_result(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    wait = WebDriverWait(driver, 20)
    delay_input = wait.until(
         EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
    )
    delay_input.clear()
    delay_input.send_keys("45")

    buttons = ["7", "+", "8", "="]
    for btn in buttons:
        xpath = f"//span[text()='{btn}']"
        driver.find_element(By.XPATH, xpath).click()

    wait = WebDriverWait(driver, 50)

    wait.until(EC.invisibility_of_element_located((By.ID, "spinner")))

    element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".screen")))

    assert element.text.strip() == "15", (
        f"Полученный текст {element.text}, ожидается '15'")
