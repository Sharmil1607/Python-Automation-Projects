#TestCase
#1.Open Browser
#2.Enter URL
#3.Enter UserName and Password and click Login button
#4.Capture title and compare
#5.Close Browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#Using driver location from anywhere in our PC
#service = Service("D:\\TESTING\\PythonAutomationProjects\\Drivers\\chromedriver.exe")
#driver = webdriver.Chrome(service=service)

#Using driver location from Python installation file
#C:\Users\PublicUsers\AppData\Local\Programs\Python\Python313\Scripts

#Browers:
#driver = webdriver.Chrome() # Chrome
#driver = webdriver.Firefox() #Firefox
#driver = webdriver.Edge() #Edge

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//*[@type='submit']").click()
time.sleep(2)
act_title=driver.title
exp_title="OrangeHRM"
if act_title==exp_title:
    print("Test Case Passed")
else:
    print("Test Case Failed")
driver.close()