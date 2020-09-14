from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser():
    def setup(self):
        desire_cap = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "browserName": "Browser",
            "noReset": True
            # "chromedriverExecutable"="指定driver地址"
        }
        self.driver = webdriver.Remote("127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        sleep(5)
        self.driver.find_element(By.ID, "index-kw").click()
        self.driver.find_element(By.ID, "index-kw").send_keys("appium")
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "index-bn")))
        self.driver.find_element(By.ID, "index-bn").click()

    def test_webview(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "views").click()
        webview = "WebView"
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        f'scrollIntoView(new UiSelector().text("{webview}")'
                                                        '.instance(0));').click()

        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "i has no focus").send_keys("this is a test string")
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "i am a link").click()
        print(self.driver.page_source)
