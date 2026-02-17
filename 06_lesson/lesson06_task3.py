from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

done_element = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
)

images = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
)

third_image = images[3]
image_src = third_image.get_attribute("src")
print(image_src)

driver.quit()
