from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pythoncode.appium_homework.appium_workwx2.page.basepage import BasePage
from pythoncode.appium_homework.appium_workwx2.page.contactpage import ContactPage


class MainPage(BasePage):
    driver: WebDriver

    def goto_message(self):
        pass

    def goto_contactlist(self):
        _address_ele=(By.XPATH,'//android.view.ViewGroup//*[@text="通讯录"]')
        #进入通讯录 并点击
        #self.driver.find_element(By.XPATH,'//android.view.ViewGroup//*[@text="通讯录"]').click()
        self.find_click(_address_ele)
        return ContactPage(self.driver)

    def goto_workplatform(self):
        pass