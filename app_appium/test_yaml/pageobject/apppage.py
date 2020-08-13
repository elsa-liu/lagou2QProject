from appium import webdriver
from app_appium.test_yaml.pageobject.basepage import BasePage
from app_appium.test_yaml.pageobject.mainpage import Main


class App(BasePage):
    def start(self):
        _package= "com.xueqiu.android"
        _activity= ".view.WelcomeActivityAlias"
        desire_cap={
        "platformName": "Android",
        "deviceName": "127.0.0.1:7555",
        "appPackage": _package,
        "appActivity": _activity,
        "noReset": True
    }
        if self._driver is None:
            self._driver = webdriver.Remote("127.0.0.1:4723/wd/hub",desire_cap)
            self._driver.implicitly_wait(10)
        else:
            self._driver.start_activity(_package,_activity)
        #为什么要return self
        return self

    def main(self):
        return Main(self._driver)
        #错误的方式 括号中没有 self._driver传入参数 如return Main() 则会报错“AttributeError: 'NoneType' object has no attribute 'find_element'”

