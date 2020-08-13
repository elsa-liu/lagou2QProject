from app_appium.test_yaml.pageobject.basepage import BasePage
from app_appium.test_yaml.pageobject.searchpage import Search


class Market(BasePage):
    def goto_search(self):
        self.step("../pageobject/datas/search.yaml")
        return Search(self._driver)

