import pytest
import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

with open ("datas/member.yml","r",encoding='UTF-8') as f:
    datas=yaml.safe_load(f)
    print(datas)
    addlist = datas["add"]
    dellist = datas["del"]

class Test_Member:
    def setup_class(self):
        des_cap={
            "platformName":"Android",
            "deviceName":"127.0.0.1:7555",
            "appPackage":"com.tencent.wework",
            "appActivity":"com.tencent.wework.launch.WwMainActivity",
            "noReset":True
             }

        self.driver=webdriver.Remote("127.0.0.1:4723/wd/hub",des_cap)
        self.driver.implicitly_wait(5)
    def teardown_class(self):
        self.driver.quit()

#添加联系人
    @pytest.mark.parametrize('add_name,mem_gender,mem_phonenum',addlist,ids=["a","b","c","d"])
    def test_addmember(self,add_name,mem_gender,mem_phonenum):
    #def test_addmember(self):
        # add_name="test1"
        # mem_gender="男"
        # mem_phonenum=13222222223
        #1.点击通讯录
        self.driver.find_element(By.XPATH,'//android.view.ViewGroup//*[@text="通讯录"]').click()
        #2.滚动查找“添加联系人按钮”
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true)\
            .instance(0)).scrollIntoView(new UiSelector().\
            text("添加成员").instance(0));').click()
        #3.点击“手动输入添加”
        self.driver.find_element_by_xpath('//*[@text="手动输入添加"]').click()
        #4.输入姓名 性别 电话
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../"
                                          "android.widget.EditText").send_keys(add_name)
        self.driver.find_element_by_xpath('//*[@text="性别"]/../android.widget.RelativeLayout').click()
        if mem_gender=="男":
            WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@text="男"]')))
            self.driver.find_element_by_xpath('//*[@text="男"]').click()
        else:
            self.driver.find_element_by_xpath('//*[@text="女"]').click()
        self.driver.find_element_by_xpath('//*[@text="手机号"]').send_keys(mem_phonenum)
        self.driver.find_element_by_xpath('//*[@text="保存"]').click()
        toast_text=self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        assert toast_text=="添加成功"
        self.driver.back()

#删除联系人
    @pytest.mark.parametrize('del_name',dellist)
    def test_delmember(self,del_name):
        #del_name = "test1"
        #1.点击通讯录
        self.driver.find_element(By.XPATH,'//android.view.ViewGroup//*[@text="通讯录"]').click()
        #2.滚动查找需要删除的人名
        self.driver.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true)\
            .instance(0)).scrollIntoView(new UiSelector().\
            text("{del_name}").instance(0));').click()
        # 3.点击右上角选择属性
        self.driver.find_element_by_id('com.tencent.wework:id/hjz').click()
        #4.点击“编辑成员”
        self.driver.find_element_by_xpath('//*[@text="编辑成员"]').click()
        #5.点击“删除成员”
        self.driver.find_element_by_xpath('//*[@text="删除成员"]').click()
        self.driver.find_element_by_xpath('//*[@text="确定"]').click()
        #6.等待成员信息消失
        result = WebDriverWait(self.driver,15).until_not(lambda x:x.find_element_by_xpath(f'//*[@test={del_name}]'))
        print(result)



