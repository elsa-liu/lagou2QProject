from selenium.webdriver.common.by import By

from web_selenium.Page_Object.page.base_page import BasePage
from web_selenium.Page_Object.page.register import Register


class Login(BasePage):
    def login(self):
        pass

    def register(self):
        self.find(By.CSS_SELECTOR,".login_registerBar_link")
        return Register(self._driver)

