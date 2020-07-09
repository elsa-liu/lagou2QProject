from selenium import webdriver
from selenium.webdriver.common.by import By

from web_selenium.Page_Object.page.base_page import BasePage
from web_selenium.Page_Object.page.login import Login
from web_selenium.Page_Object.page.register import Register


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    def goto_register(self):
        self.find(By.CSS_SELECTOR,".index_head_info_pCDownloadBtn").click()
        return Register(self._driver)

    def goto_login(self):
        self.find(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
        return Login(self._driver)