import os

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.save_screenshot("save path\\name.jpg") #Anywhere in local pc

driver.save_screenshot(os.getcwd()+"\\name.jpg") # save screenshot in the package

driver.get_screenshot_as_file(os.getcwd()+"\\name.jpg") # save screenshot in the package