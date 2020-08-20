import time

import pytest
import yaml

from pythoncode.appium_homework.appium_workwx2.page.apppage import App
with open("../../appium_workwx1/datas/member.yml","r",encoding="UTF-8") as f:
    datas=yaml.safe_load(f)
    addlist=datas["add"]
    dellist=datas["del"]


class Test_Memcontact:
    def setup_class(self):
        #实例化主页面
        self.app=App()
        self.main=self.app.start().goto_mainpage()

    def teardown_class(self):
        self.app.close()

    @pytest.mark.parametrize("name,gender,phone_num", addlist)
    def test_addmember(self,name,gender,phone_num):
        #@pytest.mark.parametrize("name,gender,phone_num",addlist)
       test_result= self.main.goto_contactlist().goto_addmember().addmember_manual().edit_name(name)\
            .edit_gender(gender).edit_phonenum(phone_num).click_save().get_result()

       assert test_result == "添加成功"
       time.sleep(2)

       self.app.back()
    @pytest.mark.parametrize("name",dellist)
    def test_delmember(self,name):
        result=self.main.goto_contactlist().click_name(name).goto_selector().del_member().if_memberhere(name)
        print(f"返回的数据{result}")

        assert result == True
