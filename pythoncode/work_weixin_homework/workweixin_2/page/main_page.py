from selenium.webdriver.common.by import By

from pythoncode.work_weixin_homework.workweixin_2.page.base_page import BasePage
from pythoncode.work_weixin_homework.workweixin_2.page.loginpage import Login_Page


class Main(BasePage):
    _url = "https://work.weixin.qq.com/"

    def goto_login(self):
        self.find(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
        return Login_Page(self.driver)