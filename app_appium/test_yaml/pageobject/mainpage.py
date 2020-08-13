from app_appium.test_yaml.pageobject.basepage import BasePage
from app_appium.test_yaml.pageobject.marketpage import Market


class Main(BasePage):
    def goto_market(self):
        self.step("../pageobject/datas/main.yaml")
        return Market(self._driver)