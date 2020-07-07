from time import sleep

from web_selenium.selenium_js.base import Base


class Test_js(Base):
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("selenium 测试")
        self.driver.find_element_by_id("su").click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]").click()
        sleep(3)
        for code in ['return document.title','return JSON.stringify(performance.timing)']:
            print(self.driver.execute_script(code))

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script('return document.getElementById("train_date").removeAttribute("readonly")')

        # self.driver.execute_script("time_ele.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        sleep(5)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
