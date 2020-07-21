from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Test_Login:
    def test_debug_login(self):
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=option)
        # driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
