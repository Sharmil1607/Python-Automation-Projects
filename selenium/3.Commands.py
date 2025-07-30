
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

#Applicational Commands
driver.get("URL") # To Open Url
driver.title # To Get title
driver.current_url # To capture the current Url of thr page
driver.page_source # To capture the source of the page

#Conditional Commands
ele=driver.find_element(By.XPATH, "")
ele.is_enabled() # Checks if the element is enabled
ele.is_selected() # Checks if the element is selected
ele.is_displayed() # Checks if the element is visible on the page

#Element Interaction Commands
ele.click() # To click the button or link
ele.send_keys() # To enter a values
ele.clear() # To clear the values in textbox

#Browser Commands
driver.close() # Close current page
driver.quit() # Close the browser

#Navigational Commands
driver.back() # Navigate to previous page
driver.forward() # Navigate to next page
driver.refresh() # To refresh the page

#Difference b/w FindElement and FindElements
ele1 = driver.find_element() # Returns single webelement
ele2 = driver.find_elements() # Returns multiple webelements
print(len(ele2)) # To get length
print(ele2[0].text) # To print the value using index
for e in ele2:
    print(e.text) # To print all the values

#Text vs Attribute
ele.text # To get the innertext from the tag
ele.get_attribute('value') # To get text in textbox using attribute
