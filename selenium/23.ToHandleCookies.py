import os
import requests as requests
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

#To capture cookies
cookies1=driver.get_cookies()
print((len(cookies1)))

#print info of cookies
for cook in cookies1:
    print(cook)
    print(cook.get('name'))