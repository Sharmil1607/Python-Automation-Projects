from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/datepicker/")
time.sleep(5)

#Method 1

month="March"
year="2023"
date="31"

driver.find_element(By.XPATH,"").click()

#select month and year
while True:
    mon=driver.find_element(By.XPATH,"").text
    yr = driver.find_element(By.XPATH, "").text

    if mon==month and yr==year:
        break;
    else:
        driver.find_element(By.XPATH,"next arrow").click()

#select date

    dates=driver.find_element(By.XPATH,"").text

for ele in dates:
    if ele==date:
        ele.click()
        break

#Method 2
#URL- https://www.dummyticket.com/dummy-ticket-for-visa-application/
month=Select(driver.find_element(By.XPATH,""))
month.select_by_visible_text()

year=Select(driver.find_element(By.XPATH,""))
year.select_by_visible_text()

dates=driver.find_element(By.XPATH,"").text

for ele in dates:
    if ele=="31":
        ele.click()
        break