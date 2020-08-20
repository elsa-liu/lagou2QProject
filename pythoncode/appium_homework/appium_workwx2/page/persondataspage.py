from selenium.webdriver.common.by import By

from pythoncode.appium_homework.appium_workwx2.page.basepage import BasePage
from pythoncode.appium_homework.appium_workwx2.page.editmempage import EditmemPage


class PersondatasPage(BasePage):
    def goto_selector(self):
        _selector_ele=(By.ID,"com.tencent.wework:id/hjz")
        _editmember_ele=(By.XPATH,'//*[@text="编辑成员"]')
        self.find_click(_selector_ele)
        self.find_click(_editmember_ele)
        return EditmemPage(self.driver)