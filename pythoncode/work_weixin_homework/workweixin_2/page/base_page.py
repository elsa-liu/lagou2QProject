import json
import os
from time import sleep

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

    def get_cookies(self):
        cookies = self.driver.get_cookies()
        with open("cookies.json", 'w') as f:
            json.dump(cookies, f)

    def add_cookie(self):
        with open("cookies.json",'r')as f:
            cookies = json.load(f)
            print(cookies)
            for cookie in cookies:
                if 'expiry' in cookie.keys():
                    del cookie['expiry']
                self.driver.add_cookie(cookie)
            sleep(20)
            self.driver.refresh()
