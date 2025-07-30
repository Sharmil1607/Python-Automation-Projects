from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/basic_auth")
time.sleep(3)

#Authentication popup

#syntax - http://username:password@gmail.com
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")