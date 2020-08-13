from app_appium.test_yaml.pageobject.apppage import App


class Test_case:
    def test_case1(self):
        App().start().main().goto_market().goto_search().search("jd")