from time import sleep

from selenium.webdriver.common.by import By

from pythoncode.work_weixin_homework.workweixin_2.page.base_page import BasePage


class Mem_Contact(BasePage):
    def import_files(self):
        self.find(By.ID,'js_upload_file_input').send_keys(r'C:\Users\Administrator\PycharmProjects\lagou2QProject\test_selenium\data\work_contact.xls')
        self.find(By.ID,'submit_csv').click()#
        return self.find(By.ID,'reUpload').get_attribute("textContent")

    def del_member(self):
        self.find(By.XPATH,'//*[@id="member_list"]/tr[7]/td[1]').click()
        name = self.find(By.XPATH,'//*[@id="member_list"]/tr[7]/td[2]').get_attribute("title")
        print(name)
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        #self.find(By.CSS_SELECTOR,'.qui_btn ww_btn js_delete').click()
        self.find(By.XPATH,'//*[@id="js_contacts79"]/div/div[2]/div/div[2]/div[3]/div[9]/a[3]').click()
        sleep(5)
        return name

