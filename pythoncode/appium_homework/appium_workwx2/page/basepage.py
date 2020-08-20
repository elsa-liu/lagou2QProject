from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self,driver:WebDriver=None):
        self.driver = driver

    def find(self,locator):
        #传入元组 locator=(By.ID,"XXXXX")
        ele=self.driver.find_element(*locator)
        return ele

    def find_click(self,locator):
        self.find(locator).click()

    def find_send(self,text,locator):
        self.find(locator).send_keys(text)

    def scroll_find_click(self,text):
        self.driver.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true)\
            .instance(0)).scrollIntoView(new UiSelector().\
            text("{text}").instance(0));').click()

    def get_toast(self):
        toast_text=self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        return toast_text

    def back(self,num=1):
        for i in range(num):
            self.driver.back()

    def close(self):
        self.driver.quit()

