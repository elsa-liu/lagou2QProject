from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():
    _url = ''
    def __init__(self,driver_basepage:WebDriver = None):
        if driver_basepage == None:
            self.driver = webdriver.Chrome()
        else:
            self.driver = driver_basepage
        if self._url != '':
            self.driver.get(self._url)
        self.driver.implicitly_wait(10)

    def find(self,by,location):
        return self.driver.find_element(by,location)
