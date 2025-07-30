import os
import requests as requests
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

#It will open in new tab - Selenium 3
reglink=Keys.CONTROL+Keys.ENTER
driver.find_element(By.XPATH).send_keys(reglink)

#Open link in new tab and auto switch to new tab using selenium 4
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.switch_to.new_window('tab')
driver.get("https://www.google.com/") #driver will be in this window

#Open link in new window and auto switch to new window  using selenium 4
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.switch_to.new_window('window')
driver.get("https://www.google.com/") #driver will be in this window