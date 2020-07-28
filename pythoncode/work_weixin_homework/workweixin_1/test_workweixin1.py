import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_Login():
    def test_debuglogin(self):
        option = Options()
        option.debugger_address="127.0.0.1:9222"
        driver = webdriver.Chrome(options=option)
        driver.get("https://work.weixin.qq.com/")
        driver.find_element(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()

    def test_getcookie(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(10)
        #换成显示等待
        # WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
        #     (By.CSS_SELECTOR,'.login_stage_title_text')))
        cookies = self.driver.get_cookies()
        with open("cookies.json",'w') as f:
            json.dump(cookies,f)

    def test_cookielogin(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        with open("cookies.json",'r')as f:
            cookies = json.load(f)
            for cookie in cookies:
                if 'expiry' in cookie.keys():
                    del cookie['expiry']
                self.driver.add_cookie(cookie)
            sleep(10)
            self.driver.refresh()
            #sleep(5) 换成显示等待
            while True:
                self.driver.refresh()
                res = WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.ID,'menu_index')))
                if res is not None:
                    break
    def teardown(self):
        pass
        #self.driver.quit()

