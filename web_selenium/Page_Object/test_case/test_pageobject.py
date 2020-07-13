from web_selenium.Page_Object.page.main import Main


class TestP0:
    def setup(self):
        self.main = Main()

    def test_register(self):
        assert self.main.goto_register().register()

    def test_login(self):
        pass
