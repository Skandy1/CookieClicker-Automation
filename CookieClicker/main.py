import datetime
from playsound import playsound
from selenium import webdriver
import time

import_file = open("import.txt").read()
print(import_file)
chrome_driver_path = # YOUR CHROME DRIVER PATH
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url="https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)
options_button = driver.find_element_by_id("prefsButton")
options_button.click()
time.sleep(2)
import_button = driver.find_element_by_link_text("Import save")
import_button.click()
time.sleep(2)
text_aread = driver.find_element_by_id("textareaPrompt")
text_aread.send_keys(import_file)
time.sleep(2)
load_button = driver.find_element_by_id("promptOption0")
load_button.click()
time.sleep(2)
close_button = driver.find_element_by_css_selector("#menu .menuClose")
close_button.click()
is_on = True
counter = 0
get_cookie = driver.find_element_by_id("bigCookie")
while is_on:
    if counter <= 5000:
        get_cookie.click()
        counter += 1
    else:
        playsound('notification.mp3')
        print("Buy Something!", datetime.datetime.now())
        time.sleep(10)
        print("Clicking Started ", datetime.datetime.now())
        counter = 0
driver.quit()
