from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        # self.driver.get("http://sahitest.com/demo/clicks.htm")
        # self.driver.get("https://www.baidu.com/")
        # self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        self.driver.get("http://sahitest.com/demo/label.htm")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        element_click = self.driver.find_element_by_xpath('/html/body/form/input[3]')
        element_doubleclick = self.driver.find_element_by_xpath("//*[@value='dbl click me']")
        element_contextclick = self.driver.find_element_by_xpath("//*[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_doubleclick)
        action.context_click(element_contextclick)
        sleep(3)
        action.perform()
        sleep(3)

    def test_movetoelement(self):
        # self.driver.get("https://www.baidu.com/")
        element = self.driver.find_element_by_xpath("//*[@id='s-usersetting-top']")
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()
        sleep(3)

    def test_dragdrop(self):
        drag_ele = self.driver.find_element_by_xpath("//*[@id='dragger']")
        drop_ele = self.driver.find_element_by_xpath("/html/body/div[2]")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_ele, drop_ele).perform()
        sleep(3)

    def test_keys(self):
        self.driver.find_element_by_xpath("/html/body/label[1]/input").click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(2)
        action.send_keys(Keys.SPACE).pause(2)
        action.send_keys("tom")
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)
