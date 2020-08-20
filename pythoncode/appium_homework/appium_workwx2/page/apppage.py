from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from pythoncode.appium_homework.appium_workwx2.page.basepage import BasePage
from pythoncode.appium_homework.appium_workwx2.page.mainpage import MainPage


class App(BasePage):
    driver:WebDriver
    def start(self):
        des_cap={
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": "com.tencent.wework.launch.WwMainActivity",
            "noReset": True
        }
        if self.driver == None:
            self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",des_cap)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(10)

        return self

    def restart(self):

        pass



    def goto_mainpage(self):
        return MainPage(self.driver)



