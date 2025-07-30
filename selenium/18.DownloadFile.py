from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
#Mostly we won't use download in automation
def chrome_setup():
    # Set up ChromeDriver service
    serv_obj = Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
    preferences = {
        "download.default_directory": r"C:\Users\admin\PycharmProjects\PythonSelenium\day22"
    }
    driver = webdriver.Chrome(service=serv_obj)
    return driver

def edge_setup():
    # Set up ChromeDriver service
    serv_obj = Service("C:\\Drivers\\chromedriver_win32\\edgedriver.exe")
    preferences = {
        "download.default_directory": r"C:\Users\admin\PycharmProjects\PythonSelenium\day22"
    }
    driver = webdriver.Edge(service=serv_obj)
    return driver

# Launch Chrome with custom download directory
driver = chrome_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()

# Click the download link for the first DOC file in the table
driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()

# Optional: wait for download to complete
time.sleep(5)

driver.quit()