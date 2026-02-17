from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.CSS_SELECTOR, 'input.form-control')
input_field.send_keys('SkyPro')

button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
button.click()

waiter = WebDriverWait(driver, 10)
updated_button = waiter.until(EC.text_to_be_present_in_element(
    (By.CSS_SELECTOR, "button.btn.btn-primary"), "SkyPro")
)

txt = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").text
print(txt)

driver.quit()
