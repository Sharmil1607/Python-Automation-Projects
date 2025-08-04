from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_0001_Login:

    Base_Url = ReadConfig.getApplication_URL()
    User_Name = ReadConfig.getApplication_Username()
    Password = ReadConfig.getApplication_Password()

    #To run in terminal
    #pytest -v -s testCases/Test_Login.py --browser Chrome

    #To run parallel in terminal
    #pytest -v -s -n=2 testCases/Test_Login.py --browser Chrome

    # To run parallel in terminal and generate report
    # pytest -v -s -n=2 --html=Reports\report.html testCases/Test_Login.py --browser Chrome

    logger = LogGen.loggen()

    def test_HomePageTitle(self,setup):
        self.logger.info("********* Verifying Home Page Title ********")
        self.driver = setup
        self.driver.get(self.Base_Url)
        app_title = self.driver.title

        if app_title=="nopCommerce demo store. Login":
            assert True
            self.driver.close()
            self.logger.info("********* Home Page Title TestCase Passed ********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_HomePageTitle.png")
            self.driver.close()
            assert False
            self.logger.error("********* Home Page Title TestCase Failed ********")


    def test_Login(self,setup):
        self.logger.info("********* Test_0001_Login ********")
        self.logger.info("********* Verifying Login ********")
        self.driver = setup
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
            self.logger.info("********* Login TestCase Passed ********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.driver.close()
            assert  False
            self.logger.error("********* Login TestCase Failed ********")