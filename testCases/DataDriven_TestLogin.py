import time

from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtilis

class Test_0002_Login:

    path=".//TestData/OpenStore.xlsx"
    Base_Url = ReadConfig.getApplication_URL()

    logger = LogGen.loggen()

    def test_Login(self,setup):
        self.logger.info("********* Test_0002_Login ********")
        self.logger.info("********* Verifying Login ********")
        self.driver = setup
        self.driver.get(self.Base_Url)
        self.lp=Login(self.driver)

        #to get total rows
        self.rows=XLUtilis.getRowCount(self.path, "TestData")

        #empty list to store the result which we gonna compre with actual result
        lst_status = []

        for r in range(2, self.rows+1):
            self.username = XLUtilis.readData(self.path,"TestData", r, 1) #1st column
            self.password = XLUtilis.readData(self.path, "TestData", r, 2) #2nd column
            self.result = XLUtilis.readData(self.path, "TestData", r, 3) #3rd column

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)

            page_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if page_title == exp_title:
                if self.result=="Pass":
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                    self.logger.info("********* Login TestCase Passed ********")
                elif self.result=="Fail":
                    self.lp.clickLogout()
                    lst_status.append("Fail")
                    self.logger.info("********* Login TestCase Failed ********")
            elif page_title != exp_title:
                if self.result=="Pass":
                    lst_status.append("Fail")
                    self.logger.info("********* Login TestCase Failed ********")
                elif self.result=="Fail":
                    lst_status.append("Pass")
                    self.logger.info("********* Login TestCase Passed ********")

        if "Fail" not in lst_status:
            assert True
            self.driver.close()
            self.logger.info("********* Login DataDriven TestCase Passed ********")
        else:
            self.driver.close()
            assert False
            self.logger.info("********* Login DataDriven TestCase Failed ********")

        self.logger.info("********* Test_0002_Login Ended ********")
