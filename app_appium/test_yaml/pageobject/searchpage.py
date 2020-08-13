from app_appium.test_yaml.pageobject.basepage import BasePage


class Search(BasePage):
    def search(self,value):
        self._params["value"]=value
        self.step("../pageobject/datas/search_ele.yaml")

