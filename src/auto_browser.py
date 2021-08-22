from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import datetime
import os 

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('window-size=1366x768')
options.add_experimental_option("excludeSwitches", ['enable-automation'])

CHROME_PROFILE = os.environ.get("chrome_profile")
if CHROME_PROFILE:
    options.add_argument(f'--user-data-dir={CHROME_PROFILE}')

driver = webdriver.Chrome(executable_path=os.environ.get("chrome_driver_path"),options=options)

URL = os.getenv("access", "https://github.com")
driver.get(URL)
driver.maximize_window()
driver.implicitly_wait(10)

if "teams" not in os.getenv("access"):
    print("Access to other than teams")
    driver.close()


if "https://login.live.com/" in driver.current_url:
    print("Login in")
    passwd = driver.find_element_by_id("passwd")
    passwd.send_keys(os.getenv("ms_password"))
    passwd.send_keys(Keys.ENTER)
    breakpoint()
    

message_body = driver.find_elements_by_class_name('message-body')
if message_body:
    today = datetime.date.today()
    today_str = today.strftime("%m/%d") if today.strftime("%m/%d")[0] != "0" else today.strftime("%m/%d")[1:]
    print(today_str)
    for i in message_body:
        print(i.text)
    driver.close()

else:
    print("Cannot find message_body")