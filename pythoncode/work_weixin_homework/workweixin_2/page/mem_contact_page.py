from time import sleep

from selenium.webdriver.common.by import By

from pythoncode.work_weixin_homework.workweixin_2.page.base_page import BasePage


class Mem_Contact(BasePage):
    def import_files(self):
        self.find(By.CSS_SELECTOR,'.qui_btn ww_btn ww_fileInputWrap').send_keys(r'test_selenium\data\work_contact.xls')
        self.find(By.ID,'submit_csv').click()
        self.driver.refresh()
        return self.find(By.ID,'reUpload').get_attribute("textContent")

    def del_member(self):
        self.find(By.XPATH,'//*[@id="member_list"]/tr[7]/td[1]').click()
        name = self.find(By.XPATH,'//*[@id="member_list"]/tr[7]/td[2]').get_attribute("title")
        print(name)
        self.find(By.CSS_SELECTOR,'.qui_btn ww_btn js_delete').click()
        sleep(10)
