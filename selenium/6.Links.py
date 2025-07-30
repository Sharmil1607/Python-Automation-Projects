import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#1.Internal Links - Navigate on same page
#2.External Links - Navigate on different page

links=driver.find_elements(By.XPATH,'//a')
print(len(links)) #print length of the links

for link in links:
    print(link.text) #print all links

#3.Broken link
#need to install requests package from project interpreter

links=driver.find_elements(By.XPATH,'//a')
count = 0
for link in links:
    url=link.get_attribute('href')
    res=requests.head(url)
    if res.status_code>=400:
        print(url, " is broken link")
        count+=1
    else:
        print(url, " is valid link")
print("Total number of broken links ", count)
