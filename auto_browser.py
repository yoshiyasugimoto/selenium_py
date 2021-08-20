from selenium import webdriver

import os 

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation'])
CHROME_PROFILE = os.environ.get("chrome_profile")
if CHROME_PROFILE:
    options.add_argument(f'--user-data-dir={CHROME_PROFILE}')

driver = webdriver.Chrome(executable_path=os.environ.get("chrome_driver_path"),options=options)

URL = os.getenv("access", "https://github.com")
driver.get(URL)