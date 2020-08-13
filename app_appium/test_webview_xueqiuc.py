from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class Test_Webview:
    def setup(self):
        des_cap={
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": "com.xueqiu.android.common.MainActivity",
            "noReset": True,
            #"chromedriverExcutable":''
        }
        self.driver= webdriver.Remote("http://127.0.0.1/:4723/wd/hub",des_cap)
        self.driver.implicitly_wait(5)
    def teardown(self):
        pass

    def test_xueqiuwebview(self):
        self.driver.find_element(MobileBy.XPATH,'//*[@text="交易"]').click()




