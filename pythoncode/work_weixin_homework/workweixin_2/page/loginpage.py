from selenium.webdriver.common.by import By

from pythoncode.work_weixin_homework.workweixin_2.page.base_page import BasePage
from pythoncode.work_weixin_homework.workweixin_2.page.mem_contact_page import Mem_Contact


class Login_Page(BasePage):
    def goto_importmembers(self):
        self.find(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(2)').click()
        return Mem_Contact(self.driver)

    def goto_membercontact(self):
        self.find(By.ID,"menu_contacts").click()
        return Mem_Contact(self.driver)

