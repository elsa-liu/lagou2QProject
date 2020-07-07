from web_selenium.selenium_js.base import Base

class Test_file(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_id("stfile").send_keys()