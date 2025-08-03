import pytest
from selenium import webdriver
from selenium.webdriver.ie.webdriver import WebDriver
from pageObjects.LoginPage import Login

class Test_0001_Login:

    Base_Url = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    User_Name = "admin@yourstore.com"
    Password = "admin"

    def test_HomePageTitle(self,setup):
        self.driver = setup
        #self.driver = webdriver.Chrome()
        self.driver.get(self.Base_Url)
        app_title = self.driver.title

        if app_title=="nopCommerce demo store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_HomePageTitle.png")
            self.driver.close()
            assert False


    def test_Login(self,setup):
        self.driver = setup
        #self.driver = webdriver.Chrome()
        self.driver.get(self.Base_Url)
        self.lp=Login(self.driver)
        self.lp.setUserName(self.User_Name)
        self.lp.setPassword(self.Password)
        self.lp.clickLogin()
        page_title = self.driver.title
        self.lp.clickLogout()

        if page_title=="Dashboard / nopCommerce administration":
            assert  True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.driver.close()
            assert  False
