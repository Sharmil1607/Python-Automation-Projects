from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#url - https://pypi.org/project/webdriver-manager/
#Open terminal and paste 'pip install webdriver-manager' and enter to install

browser_name = "chrome"

if browser_name == "chrome":
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
elif browser_name == "firefox":
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
elif browser_name == "edge":
    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
else:
    print("Browser name is wrong")
    raise Exception("driver is not found")

driver.get("https://pypi.org/project/webdriver-manager/")
tit=driver.title
print(tit)
driver.close()
