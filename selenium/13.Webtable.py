from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)

#1.Count number of rows and columns

NoOfRows=driver.find_elements(By.XPATH,"//*[@name='BookTable']/tbody/tr")
NoOfColumns=driver.find_elements(By.XPATH,"//*[@name='BookTable']/tbody/tr[1]/th")
print(NoOfRows)
print(NoOfColumns)

#2.Read specific row and column data

element=driver.find_elements(By.XPATH,"//*[@name='BookTable']/tbody/tr[3]/th[2]")
print(element)

#3.Read all rows and columns data

for r in range(2,NoOfRows+1): #mention start and end value of rows
    for c in range(1,NoOfColumns+1):
        element=driver.find_elements(By.XPATH,"//*[@name='BookTable']/tbody/tr["+str(r)+"]/th["+str(c)+"]").text
        print(element)
        print(element,end='      ')  #it will give space between columns
        print() #it will give space between rows

#4.Read data based on conditions

for r in range(2,NoOfRows+1): #mention start and end value of rows
    author = driver.find_elements(By.XPATH, "//*[@name='BookTable']/tbody/tr["+str(r)+"]/th[2]").text
    if author=="Mukesh":
        bookname = driver.find_elements(By.XPATH, "//*[@name='BookTable']/tbody/tr[" + str(r) + "]/th[1]").text
        print(bookname)