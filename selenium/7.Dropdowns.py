import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

countrylist=driver.find_element(By.XPATH,"")
country=Select(countrylist)

country.select_by_index(18)
country.select_by_value("13")
country.select_by_visible_text("India")

#To capture all options and print length and print text

alloption=country.options
print("All country list", len(alloption))
for option in alloption:
    print(option.text)

#To select dropdown without using select

for option in alloption:
    if option.text=="India":
        option.click()
        break
