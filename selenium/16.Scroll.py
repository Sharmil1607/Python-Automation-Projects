from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
time.sleep(5)

#1.Scroll by pixel value
driver.execute_script("window.scrollBy(0,3000)", "")
value=driver.execute_script("return window.pageYOffSet;")
print(value) #3000

#2.Scroll by element
target=driver.find_element(By.XPATH,"")
driver.execute_script("arguments[0].scrollIntoView();",target)
value=driver.execute_script("return window.pageYOffSet;")
print(value)

#3.scroll till end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffSet;")
print(value)

#4.scroll to start from end of the page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffSet;")
print(value)
