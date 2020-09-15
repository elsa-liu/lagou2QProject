import pytest
import requests

from pythoncode.requests_homework.test_request2_tag.test_resquest_tag.base_api import BaseApi
from pythoncode.requests_homework.test_request2_tag.test_resquest_tag.wework_pub import WeWork


class TestContactTag(BaseApi):
    # #实例化session
    # s = requests.Session()
    # #将token值放置session中
    # s.params={"access_token":test_get_token()}

    def test_addtag(self,tagname,tagid,token):
        data={
            "method":"post",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params":{
                "access_token":token},
            "json":{
                "tagname": tagname,
                "tagid": tagid
            }
        }

        r=self.send_api(data)
        return r

    def test_get_taguser(self,tagid,token):
        data={
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/get",
            "params":{
            "access_token":token,
            "tagid": tagid
            }
        }
        r=self.send_api(data)
        return r


    def test_update_tag(self,tagid,tagname,token):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/update",
            "params": {
                "access_token": token
            },
            "json": {
                "tagname": tagname,
                "tagid": tagid
            }
        }

        r=self.send_api(data)

        return r

    def test_delete_tag(self,token,tagid=13):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params": {
                "access_token": token,
                "tagid": tagid
            }
        }
        r=self.send_api(data)
        return r

    def test_add_taguser(self,tagid,userlist,partylist,token):
        #函数的变量不能是可变对象？？ 待解决
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers",
            "params": {
                "access_token": token
            },
            "json": {
            "tagid": tagid,
            "userlist": userlist,
            "partylist": partylist
            }
        }
        r=self.send_api(data)
        return r

    def test_del_taguser(self,tagid,userlist,partylist,token):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers",
            "params": {
                "access_token": token
            },
            "json": {
            "tagid": tagid,
            "userlist": userlist,
            "partylist": partylist
            }
        }
        r = self.send_api(data)
        return r

    def test_get_taglist(self,token):

        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/list",
            "params": {
                "access_token": token
            }
        }
        r=self.send_api(data)
        return r




