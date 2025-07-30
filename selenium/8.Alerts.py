from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(3)

ele=driver.find_element(By.XPATH, "//*[text()='Click for JS Prompt']")
ele.click()
time.sleep(3)

alert=driver.switch_to.alert

#simple alert
alert.accept()

#confirm alert
alert.dismiss()

#promt alert
print(alert.text)
alert.send_keys("sharmil")
alert.dismiss()