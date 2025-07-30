
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

checkboxes =driver.find_elements(By.XPATH,"//*[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))

#To select all the checkboxes

#Approach 1
for i in range(len(checkboxes)):
    checkboxes[i].click()

#Approach 2
for checkbox in checkboxes:
    checkbox.click()

#To select multiple checkboxes

for checkbox in checkboxes:
    weekname=checkbox.get_attribute('id')
    if weekname=="Monday" or weekname=="Friday":
        checkbox.click()

#To select last 2 checkboxes

for i in range(len(checkboxes)-2,len(checkboxes)): #(5,7)
    checkboxes[i].click()

#To select first 2 checkboxes

for i in range(len(checkboxes)):
    if i < 2:
        checkboxes[i].click()

#Clear the selected checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
