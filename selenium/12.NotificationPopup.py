from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#To Handle Notification Popup
ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://whatmylocation.com/")
time.sleep(5)




