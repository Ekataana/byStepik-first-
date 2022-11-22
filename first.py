import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(5)

driver.get("https://stepik.org/lesson/25969/step/12")

textarea = driver.find_elements(BY.CSS_SELECTOR, ".textarea")

textarea.send_keys("get()")
time.sleep(5)

submit_buton = driven.find_elements(BY.CSS_SELECTOR, ("submit-submission"))

submit_button.click()
time.sleep(5)

driver.quit()
