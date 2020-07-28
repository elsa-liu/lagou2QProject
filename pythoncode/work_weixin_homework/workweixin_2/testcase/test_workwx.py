from pythoncode.work_weixin_homework.workweixin_2.page.main_page import Main


class Test_PageObject():

    def setup(self):
        self.main = Main()

    def test_delMember(self):
        a = self.main.goto_login().goto_membercontact().del_member()
        assert a == "李万鹏"
        #self.main.goto_login()
        #print (result)

    def test_importMember_fail(self):
        b =self.main.goto_login().goto_importmembers().import_files()
        self.main.add_cookie()
        assert b == "重新上传"


