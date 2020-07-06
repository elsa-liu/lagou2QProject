from time import sleep

from selenium import webdriver

from test_selenium.base import Base


class Test_windows(Base):
    def test_windows(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_xpath("//*[@id='u1']/a[2]").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').send_keys("username")
        sleep(3)
        # self.driver.find_element_by_xpath()
