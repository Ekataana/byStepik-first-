import time

# webdriver this is a set of commands for controlling the browser 
from selenium import webdriver

# import the By class as a way to search for items
from selenium.webdriver.common.by import By

# initialize the browser driver
driver = webdriver.Chrome()
time.sleep(5)

# tell the browser which link we need to open
driver.get("https://stepik.org/lesson/25969/step/12")

# looking for a text input field
textarea = driver.find_elements(BY.CSS_SELECTOR, ".textarea")

# put text(get()) in the found field
textarea.send_keys("get()")
time.sleep(5)

# looking for a submit button
submit_buton = driven.find_elements(BY.CSS_SELECTOR, ("submit-submission"))

# we tell the driver that this button needs to be pressed
submit_button.click()
time.sleep(5)

# close the browser window after all actions are completed
driver.quit()
