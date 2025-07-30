from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

#ID
ele=driver.find_element(By.ID, "elementId")
ele.click()

#ClassName
ele=driver.find_element(By.CLASS_NAME, "className")
ele.click()

#Name
ele=driver.find_element(By.NAME, "elementName")
ele.click()

#TagName
ele=driver.find_element(By.TAG_NAME, "a")
ele.click()

#LinkText
ele=driver.find_element(By.LINK_TEXT, "Click Here")
ele.click()

#Partial LinkText
ele=driver.find_element(By.PARTIAL_LINK_TEXT, "click")
ele.click()

#Xpath
ele=driver.find_element(By.XPATH, " ")
ele.click()

#CSS
ele=driver.find_element(By.CSS_SELECTOR, " ")
ele.click()

#CSS Selectors
#1.Tag and ID (Tag is optional)
driver.find_element(By.CSS_SELECTOR, "input#name")
driver.find_element(By.CSS_SELECTOR, "#name")

#2.Tag and Class (Tag is optional)
driver.find_element(By.CSS_SELECTOR, "input.classname")
driver.find_element(By.CSS_SELECTOR, ".classname")

#3.Tag and Attribute (Tag is optional)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='search-stroe']")
driver.find_element(By.CSS_SELECTOR,"[placeholder='search-stroe']")

#4.Tag, Class and Attribute (Tag is optional)
driver.find_element(By.CSS_SELECTOR, "input.classname[placeholder='search-stroe']")
driver.find_element(By.CSS_SELECTOR, ".classname[placeholder='search-stroe']")

#Xpath - Customized Locators

#Absolute Xpath (Full Path)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea")

#Relative Xpath (Partial Xpath)

#Using Single Attribute
driver.find_element(By.XPATH, "//*[@id='APjFqb']")

#using multiple attributes
driver.find_element(By.XPATH, "//*[@id='APjFqb'][@placeholder='search']")

#Using and operator
driver.find_element(By.XPATH, "//*[@id='APjFqb' and @placeholder='search']")

#Using or operator
driver.find_element(By.XPATH, "//*[@id='APjFqb' or @placeholder='search']")

#Using inner text
driver.find_element(By.XPATH, "//*[text()='name']")

#To Find Dynamic Elements

#Using contains
driver.find_element(By.XPATH, "//*[contains(@placeholder,'search')]")

driver.find_element(By.XPATH, "//*[contains(text(),'search')]")

#Using starts-with
driver.find_element(By.XPATH, "//*[starts-with(@placeholder,'search')]")

#Using Chained Xpath - Combination of Absolute and Relative Xpath
driver.find_element(By.XPATH, "//*[@id='APjFqb']/a/img")

#Xpath Axes
#1. Self - Select the current node
driver.find_element(By.XPATH, "//a[contains(text(),'value')]/self::a")

#2. Parent - Select the parent of the current node
driver.find_element(By.XPATH, "//input[@id='email']/parent::div")

#3. Child - Select all children of the current node
driver.find_element(By.XPATH, "//div/child::p")

#4. Descendants - All descendants (children, grandchildren, etc.)
driver.find_element(By.XPATH, "//div[@id='main']/descendant::a")

#5. Descendants or Self - Current node + all descendants
driver.find_element(By.XPATH, "//div[@id='main']/descendant-or-self::div")

#6. Ancestors - All ancestors (parent, grandparent, etc.)
driver.find_element(By.XPATH, "//input[@id='pass']/ancestor::form")

#7. Ancestors or Self - Current node + all ancestors
driver.find_element(By.XPATH, "//input[@id='pass']/ancestor-or-self::form")

#8. Following - Everything in the DOM after the current node
driver.find_element(By.XPATH, "//h2/following::p")

#9. Following-sibling - Only the next siblings at the same level
driver.find_element(By.XPATH, "//label[@for='username']/following-sibling::input")

#10. Preceding - All nodes before the current node
driver.find_element(By.XPATH, "//input[@id='search']/preceding::div")

#11. Preceding-sibling - Only the previous siblings at the same level
driver.find_element(By.XPATH, "//li[@id='item3']/preceding-sibling::li")

