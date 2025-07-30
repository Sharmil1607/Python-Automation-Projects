import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

countrylist=driver.find_element(By.XPATH,"list of all elements")

for country in countrylist:
    if country.text=="India":
        country.click()
        break
