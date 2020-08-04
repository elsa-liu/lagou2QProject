import time

import pytest
from appium import webdriver
from hamcrest import *


class Test_appium():
  def setup(self):
    desire_cap ={
      "platformName": "Android",
      "deviceName": "127.0.0.1:7555",
      "appPackage": "com.xueqiu.android",
      "appActivity": ".view.WelcomeActivityAlias",
      "noReset": True
    }

    # self.driver = webdriver.Remote("127.0.0.1:4723/wd/hub",desire_cap)
    # self.driver.implicitly_wait(10)

  @pytest.mark.skip
  def test_findel(self):
    el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
    el1.click()
    el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
    el2.click()
    el2.send_keys("alibaba")
    time.sleep(5)
    el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]")
    el3.click()

  def test_hamcrest(self):
    assert_that(10 , equal_to(10),"这是一个提示")
    assert_that(11.1 , close_to(9,2))
