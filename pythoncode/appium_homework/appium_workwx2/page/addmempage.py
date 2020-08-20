from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pythoncode.appium_homework.appium_workwx2.page.basepage import BasePage
# from pythoncode.appium_homework.appium_workwx2.page.meminvitepage import MemInvitePage


class AddMemPage(BasePage):
    def edit_name(self,_add_name):

        _addname_ele=(By.XPATH,"//*[contains(@text,'姓名')]/../android.widget.EditText")
        #self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../"
                                          #"android.widget.EditText").send_keys(_add_name)
        self.find_send(_add_name,_addname_ele)

        return self

    def edit_gender(self,_mem_gender):
        _gender_ele=(By.XPATH,'//*[@text="性别"]/../android.widget.RelativeLayout')
        self.find_click(_gender_ele)
        #self.driver.find_element_by_xpath('//*[@text="性别"]/../android.widget.RelativeLayout').click()
        if _mem_gender == "男":
            WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((By.XPATH, '//*[@text="男"]')))
            self.driver.find_element_by_xpath('//*[@text="男"]').click()
        else:
            self.driver.find_element_by_xpath('//*[@text="女"]').click()

        return self

    def edit_phonenum(self,_mem_phonenum):
        _phonenum_ele=(By.XPATH,'//*[@text="手机号"]')
        self.find_send(_mem_phonenum,_phonenum_ele)
        #self.driver.find_element_by_xpath('//*[@text="手机号"]').send_keys(_mem_phonenum)

        return self

    def click_save(self):
        _save_ele=(By.XPATH,'//*[@text="保存"]')
        self.find_click(_save_ele)
        #self.driver.find_element_by_xpath('//*[@text="保存"]').click()
        from pythoncode.appium_homework.appium_workwx2.page.meminvitepage import MemInvitePage
        return MemInvitePage(self.driver)

