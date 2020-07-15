import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCookie:
    def setup(self):
        self.driver = webdriver.Chrome()
        #self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def test_get_cookie(self):
        time.sleep(10)
        cookies = self.driver.get_cookies()
        with open("cookie.json", "w") as f:
            json.dump(cookies, f)

    def test_cookie_login(self):
        cookies = json.load(open("cookie.json"))
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                del cookie['expiry']
            self.driver.add_cookie(cookie)
        while True:
            self.driver.refresh()
            res = WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable
                                                ((By.ID,"menu_index")))
            if res is not None:
                break
        #expected_condition.xx()  都是需要传入一个数组
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable
                                            ((By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(2)')))
        self.driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(2)').click()
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located
                                            ((By.ID,"js_upload_file_input")))
        self.driver.find_element(By.ID,"js_upload_file_input")\
            .send_keys(r"C:\Users\Administrator\PycharmProjects\lagou2QProject\test_selenium\data\work_contact.xls")
        res = self.driver.find_element(By.ID,'upload_file_name').text
        time.sleep(3)
        assert res=="work_contact.xls"
    def teardown(self):
        self.driver.quit()
