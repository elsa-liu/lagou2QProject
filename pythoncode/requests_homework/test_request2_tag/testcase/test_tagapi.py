import pytest

from pythoncode.requests_homework.test_request2_tag.test_resquest_tag.data_create import DataCreate
from pythoncode.requests_homework.test_request2_tag.test_resquest_tag.tag_about import TestContactTag
from pythoncode.requests_homework.test_request2_tag.test_resquest_tag.wework_pub import WeWork


class TestTag:

    def setup(self):
        #实例化
        self.access=TestContactTag()

    @pytest.fixture(scope="session")
    def token(self):
        return WeWork().test_get_token()


    @pytest.mark.parametrize("tagname,tagid,userlsit,partylist",DataCreate().create_tag_data())
    def test_all(self,tagname,tagid,userlsit,partylist,token):
        print(f"{tagname},{tagid},{userlsit},{partylist}")
        #1.创建标签,并且处理创建标签过程中的异常
        try:
            assert "created" == self.access.test_addtag(tagname,tagid,token)["errmsg"]
        except AssertionError as e:
            print(e)
            if "invalid tagid" in e.__str__():
                #2.删除标签
                self.access.test_delete_tag(token,tagid)
                assert "created" == self.access.test_addtag(tagname,tagid,token)["errmsg"]
        #2.更新标签名，并断言
        update_tagname=tagname+"update"
        assert "updated" == self.access.test_update_tag(tagid,update_tagname,token)["errmsg"]
        #8.获取标签列表，并断言
        assert "ok" == self.access.test_get_taglist(token)["errmsg"]
        #4.获取标签成员
        assert "ok" == self.access.test_get_taguser(tagid,token)["errmsg"]
        #5.增加标签成员
        self.access.test_add_taguser(tagid,userlsit,partylist,token)
        #7.删除标签成员
        self.access.test_del_taguser(tagid,userlsit,partylist,token)