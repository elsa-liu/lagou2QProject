import yaml
from appium.webdriver.webdriver import WebDriver

from selenium.webdriver.common.by import By


class BasePage:
    black_lists=[(By.ID,"image_cancel"),(By.ID,"com.xueqiu.android:id/tv_skip")]
    _params={}
    _error_count = 0
    _error_max = 10
    def __init__(self,driver:WebDriver=None):
        self._driver = driver


    #封装找元素的方法，并且处理弹窗异常情况
    def find(self,by,locator=None):
        try:
            #三目表达式
            element = self._driver.find_elements(*by) if isinstance(by,tuple) else self._driver.find_element(by,locator)
            self._error_count = 0
            return element
        #处理弹窗问题
        except Exception as e:
            self._error_count +=1
            if self._error_count >= self._error_max:
                raise e
            for black_list in self.black_lists:
                # if len(black_list)>0:
                #     self.find(black_list).click()
                # 是否可以 self.find(black_list)
                #find_elements 返回的是列表 没有找到元素则返回空列表
                elements = self._driver.find_elements(*black_list)
                if len(elements) > 0:
                    elements[0].click()
                    # 下一步：如果弹窗处理成功 再接着去find相关元素，怎么操作？？
                    return self.find(by,locator)
            raise e

    def send(self,by,locator,value):
        try:
            self.find(by,locator).send_keys(value)
            self._error_count = 0
        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            for black_list in self.black_lists:
                # if len(black_list)>0:
                #     self.find(black_list).click()
                # 是否可以 self.find(black_list)
                # find_elements 返回的是列表 没有找到元素则返回空列表
                elements = self._driver.find_elements(*black_list)
                if len(elements) > 0:
                    elements[0].click()
                    # 下一步：如果弹窗处理成功 再接着去find相关元素，怎么操作？？
                    return self.send(by, locator,value)
            raise e




    #定义获取数据方法，（数据驱动）
    def step(self,path):
        #打开本地的文件
        with open (path,"r",encoding="utf-8") as f:
            #读取yaml形式的文件，转变为python格式
            datas:list[dict] =yaml.safe_load(f)
            for data in datas:
                if "by" in data.keys():
                    element=self.find(data["by"],data["locator"])
                if "action" in data.keys():
                    if data["action"] == "click":
                        element.click()
                    if data["action"] == "send":
                        #{value}
                        content:str= data["value"]
                        for param in self._params:
                            content = content.replace("{%s}"%param,self._params[param])
                            #element.send_keys("content")
                            self.send(data["by"],data["locator"],content)



