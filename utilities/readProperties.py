import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():

    @staticmethod
    def getApplication_URL():
        url=config.get("Common Info", "Base_Url")
        return url

    @staticmethod
    def getApplication_Username():
        username = config.get("Common Info", "User_Name")
        return username

    @staticmethod
    def getApplication_Password():
        password = config.get("Common Info", "Password")
        return password
