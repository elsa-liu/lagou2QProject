import json
import time

from selenium import webdriver


class TestCookie:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")

    def test_get_cookie(self):
        # time.sleep(10)
        cookies = self.driver.get_cookies()
        with open("cookie.json", "w") as f:
            json.dump(cookies, f)

    def test_cookie_login(self):
        cookies = json.load(open("cookie.json"))
        for cookie in cookies:
            # 遍历整个cookies列表,拿到里面的字典,把cookie键值对一个一个塞入浏览器中
            self.driver.add_cookie(cookie)
        time.sleep(10)
        self.driver.refresh()

    def teardown(self):
        self.driver.quit()
