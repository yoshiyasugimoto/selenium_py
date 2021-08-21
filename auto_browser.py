from selenium import webdriver

import os 
import time
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation'])
CHROME_PROFILE = os.environ.get("chrome_profile")
if CHROME_PROFILE:
    options.add_argument(f'--user-data-dir={CHROME_PROFILE}')

driver = webdriver.Chrome(executable_path=os.environ.get("chrome_driver_path"),options=options)

URL = os.getenv("access", "https://github.com")
driver.get(URL)
time.sleep(5)
messageBody1 = driver.find_element_by_id("messageBody")
messageBody2 = driver.find_element_by_id("messageBody")
messageBody3 = driver.find_element_by_id("messageBody")

