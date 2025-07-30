from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://text-compare.com/")
time.sleep(5)

input1=driver.find_element(By.XPATH,"")
input1.send_keys("")
input2=driver.find_element(By.XPATH,"")

act=ActionChains(driver)

#In multiple lines
act.key_down(Keys.CONTROL) #to press
act.send_keys("a")
act.key_up(Keys.CONTROL) #to release
act.perform()

#In single line
act.key_down(Keys.CONTROL).send_keys("c").key_up().perform()

act.send_keys(Keys.TAB).perform()

act.key_down(Keys.CONTROL).send_keys("v").key_up().perform()