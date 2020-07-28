import json
import os
from time import sleep

from selenium.webdriver.common.by import By

from pythoncode.work_weixin_homework.workweixin_2.page.base_page import BasePage
from pythoncode.work_weixin_homework.workweixin_2.page.loginpage import Login_Page


class Main(BasePage):
    _url = "https://work.weixin.qq.com/"
    #_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def goto_login(self):
        self.find(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
        # if os.path.exists("cookies.json") is False:
        #     print("请添加cookies")
        #     self.get_cookies()
        # else:
        #     self.add_cookie()

        return Login_Page(self.driver)