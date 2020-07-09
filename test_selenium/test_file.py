from time import sleep

from test_selenium.base import Base


class Test_File(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        self.driver.find_element_by_id("stfile").send_keys(
            r"C:\Users\liuyu\Desktop\python\lagou2Q\image\1594042299(1).jpg")
        sleep(10)
