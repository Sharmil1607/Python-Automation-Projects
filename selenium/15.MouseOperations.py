from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/datepicker/")
time.sleep(5)

#Action Code
act=ActionChains()

#MouseHover
act.move_to_element().click().perform()

#Right Click
act.context_click()

#Double click
act.double_click()

#Drag and Drop
source=driver.find_element(By.XPATH,"")
target=driver.find_element(By.XPATH,"")
act.drag_and_drop(source,target).perform()

#Slider bar
source=driver.find_element(By.XPATH,"")
target=driver.find_element(By.XPATH,"")
print(source.location) #xaxis=100, yaxis=200
print(target.location) #xaxis=500, yaxis=200
act.drag_and_drop_by_offset(source,140,200).perform()
act.drag_and_drop_by_offset(target,-50,200).perform()