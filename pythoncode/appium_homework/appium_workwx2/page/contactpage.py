from selenium.webdriver.support.wait import WebDriverWait

from pythoncode.appium_homework.appium_workwx2.page.basepage import BasePage
from pythoncode.appium_homework.appium_workwx2.page.meminvitepage import MemInvitePage
from pythoncode.appium_homework.appium_workwx2.page.persondataspage import PersondatasPage


class ContactPage(BasePage):
    def goto_addmember(self):
        _find_text="添加成员"
        #滚动查找“添加成员”
        # self.driver.find_element_by_android_uiautomator(
        #     'new UiScrollable(new UiSelector().scrollable(true)\
        #     .instance(0)).scrollIntoView(new UiSelector().\
        #     text("添加成员").instance(0));').click()
        self.scroll_find_click(_find_text)
        return MemInvitePage(self.driver)

    def click_name(self,_name):
        self.scroll_find_click(_name)
        return PersondatasPage(self.driver)

    def if_memberhere(self,_name):
        result = WebDriverWait(self.driver, 15).until_not(lambda x:x.find_element_by_xpath(f'//*[@text="{_name}"]'))
        return result



