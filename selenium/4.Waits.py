
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

#1.Python wait
time.sleep(5) #Seconds

#2.Implicit Wait
driver.implicitly_wait(10) #Seconds

#3.Explicit Wait
ele=driver.find_element(By.XPATH, "")
wait=WebDriverWait(driver, 10)
clickop=wait.until(EC.presence_of_element_located(ele))
clickop=wait.until(EC.visibility_of_element_located())
clickop=wait.until(EC.visibility_of_all_elements_located())
clickop=wait.until(EC.text_to_be_present_in_element())
clickop=wait.until(EC.element_to_be_clickable())
clickop=wait.until(EC.element_to_be_selected())
clickop=wait.until(EC.alert_is_present())
clickop=wait.until(EC.title_is())
clickop=wait.until(EC.title_contains())
clickop=wait.until(EC.url_to_be())
clickop=wait.until(EC.url_contains())
clickop=wait.until(EC.number_of_windows_to_be())
clickop=wait.until(EC.element_located_to_be_selected())

clickop.click()

#To ignore some expections
wait=WebDriverWait(driver, 10, ignored_exceptions=[NoSuchElementException,
                                                    ElementNotVisibleException,
                                                    ElementNotSelectableException])
clickop=wait.until(EC.element_to_be_clickable())
clickop.click()