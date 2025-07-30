import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#Chrome
options = webdriver.ChromeOptions()
options.accept_insecure_certs = True
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

#Firefox
options = webdriver.FirefoxOptions()
options.accept_insecure_certs = True
service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)
driver.maximize_window()

#Edge
options = webdriver.EdgeOptions()
options.accept_insecure_certs = True
service = EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service, options=options)
driver.maximize_window()

driver.get("https://expired.badssl.com/")
time.sleep(2)
driver.close()