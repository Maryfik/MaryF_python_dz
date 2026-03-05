from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")


# Поиск полей для ввода имени пользователя и пароля
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")

# Ввод значений
username_input.send_keys("tomsmith")
password_input.send_keys("SuperSecretPassword!")

# Кнопка входа
login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()

# Ждём появления зелёной плашки с успешным результатом
success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "flash.success"))
    )

print(success_message.text.strip())


driver.quit()
