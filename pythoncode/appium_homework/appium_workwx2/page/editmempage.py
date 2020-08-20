from selenium.webdriver.common.by import By

from pythoncode.appium_homework.appium_workwx2.page.basepage import BasePage
#from pythoncode.appium_homework.appium_workwx2.page.contactpage import ContactPage


class EditmemPage(BasePage):
    def del_member(self):
        from pythoncode.appium_homework.appium_workwx2.page.contactpage import ContactPage
        #_del_text="删除成员"
        _sure_ele=(By.XPATH,'//*[@text="确定"]')
        #self.scroll_find_click(_del_text)
        _del_ele=(By.XPATH,'//*[@text="删除成员"]')
        self.find_click(_del_ele)
        self.find_click(_sure_ele)
        return ContactPage(self.driver)

