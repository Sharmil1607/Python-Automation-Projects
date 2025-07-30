from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("")
time.sleep(3)

driver.switch_to.frame("name")
driver.switch_to.frame("id")
driver.switch_to.frame("WebElement")
driver.switch_to.frame(0)

driver.switch_to.default_content() # To come out of frame

#InnerFrame

Outerframe=driver.find_element(By.XPATH,"")
driver.switch_to(Outerframe)

Innerframe=driver.find_element(By.XPATH,"")
driver.switch_to(Innerframe)

driver.switch_to.parent_frame() #direct to the outer frame

driver.switch_to.default_content() #direct to the webpage