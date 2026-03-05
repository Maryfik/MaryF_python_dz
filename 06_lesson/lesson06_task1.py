from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/ajax")


blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
blue_button.click()

waiter = WebDriverWait(driver, 20)
green_panel = waiter.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
)
green_panel_text = green_panel.text

if green_panel_text.strip() == "Data loaded with AJAX get request.":
    print(green_panel_text)
else:
    print(f'Ошибка: Ожидался текст "{green_panel_text}"')

driver.quit()
