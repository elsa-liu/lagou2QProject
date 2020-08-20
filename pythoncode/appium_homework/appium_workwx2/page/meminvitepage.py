from selenium.webdriver.common.by import By

from pythoncode.appium_homework.appium_workwx2.page.addmempage import AddMemPage
from pythoncode.appium_homework.appium_workwx2.page.basepage import BasePage


class MemInvitePage(BasePage):
    def addmember_manual(self):
        _find_ele=(By.XPATH,'//*[@text="手动输入添加"]')
        #self.driver.find_element_by_xpath('//*[@text="手动输入添加"]').click()
        self.find_click(_find_ele)
        return AddMemPage(self.driver)


    def get_result(self):
        #toast_text = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        result=self.get_toast()
        return result
