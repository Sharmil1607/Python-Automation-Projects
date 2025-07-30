from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)

driver.find_element(By.XPATH,"//*[text()='OrangeHRM, Inc']").click()

#Single window
driver.current_window_handle

#Multiple window
driver.window_handles

#for 2 windows
windowids=driver.window_handles
parentwindow=windowids[0]
childwindow=windowids[1]

print(parentwindow)  # Parent window Id
print(childwindow) # Child Window Id
print(driver.title) # Parent window
driver.switch_to.window(childwindow)
print(driver.title) # Child Window

#for more than 2 windows

for winid in windowids:
    driver.switch_to.window(winid)
    print(driver.title)
    if driver.title=="orangehrm":
        driver.switch_to.window()
        driver.close()
