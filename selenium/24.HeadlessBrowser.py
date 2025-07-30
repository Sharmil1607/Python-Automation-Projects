import time
from selenium import webdriver

#Chrome
def headlesschrome():
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless=new")  # ✅ Recommended for Chrome 109+
    ops.add_argument("--disable-gpu")  # ✅ Safe fallback for headless
    ops.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=ops)
    return driver

#Firefox
def headlessfirefox():
    ops = webdriver.FirefoxOptions()
    ops.add_argument("--headless")  # ✅ Correct flag for Firefox
    ops.add_argument("--width=1920")  # Optional: set size
    ops.add_argument("--height=1080")
    driver = webdriver.Firefox(options=ops)
    return driver

#Edge
def headlessedge():
    ops = webdriver.EdgeOptions()
    ops.add_argument("--headless=new")  # ✅ Recommended for Chrome 109+
    ops.add_argument("--disable-gpu")  # ✅ Safe fallback for headless
    ops.add_argument("--window-size=1920,1080")
    driver = webdriver.Edge(options=ops)
    return driver

driver = headlessfirefox()
print("firefox")
driver.get("https://www.facebook.com/")
time.sleep(1)
ti=driver.title
ur=driver.current_url
print(ti)
print(ur)
driver.quit()
