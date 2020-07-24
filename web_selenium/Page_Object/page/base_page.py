from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    #声明一个空的 保护类变量，作为要访问的网址
    _base_url=''
    #对类进行初始化，并且定义参数driver
    def __init__(self,driver:WebDriver=None):
        if driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver
        if self._base_url != '':
            self._driver.get(self._base_url)
    def find(self,by,locator):
        return self._driver.find_element(by,locator)
