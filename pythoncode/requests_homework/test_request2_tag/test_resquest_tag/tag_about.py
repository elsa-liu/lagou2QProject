import requests

from pythoncode.requests_homework.test_request2_tag.test_resquest_tag.base_api import BaseApi
from pythoncode.requests_homework.test_request2_tag.test_resquest_tag.wework_pub import WeWork


class TagAbout(WeWork,BaseApi):

    def __init__(self):
        # 实例化session
        self.s = requests.Session()
        # 将token值放置session中
        self.s.params = {"access_token":self.test_get_token()}

    def test_addtag(self, tagname, tagid):
        data = {
            "tagname": tagname,
            "tagid": tagid
        }
        # r=requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.test_get_token()}",json=data)
        r = self.s.post("https://qyapi.weixin.qq.com/cgi-bin/tag/create", json=data)
        print(r.json())
        return r.json()

    def test_get_taguser(self, tagid):
        params = {
            "tagid": tagid
        }
        r = self.s.get("https://qyapi.weixin.qq.com/cgi-bin/tag/get", params=params)
        print(r.json())
        return r.json()

    def test_update_tag(self, tagid, tagname):
        data = {
            "tagid": tagid,
            "tagname": tagname
        }

        r = self.s.post("https://qyapi.weixin.qq.com/cgi-bin/tag/update", json=data)

        print(r.json())
        return r.json()

    def test_delete_tag(self, tagid=13):
        params = {
            "tagid": tagid
        }
        # r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/delete",params=params)
        r = self.s.get("https://qyapi.weixin.qq.com/cgi-bin/tag/delete", params=params)
        print(r.json())
        return r.json()

    def test_add_taguser(self, tagid, userlist, partylist):
        # 函数的变量不能是可变对象？？ 待解决
        data = {
            "tagid": tagid,
            "userlist": userlist,
            "partylist": partylist
        }
        r = self.s.post("https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers", json=data)
        print(r.json())
        return r.json()

    def test_del_taguser(self, tagid, userlist, partylist):
        data = {
            "tagid": tagid,
            "userlist": userlist,
            "partylist": partylist
        }
        r = self.s.post("https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers", json=data)
        print(r.json())
        return r.json()

    def test_get_taglist(self):
        r = self.s.get("https://qyapi.weixin.qq.com/cgi-bin/tag/list")
        print(r.json())
        return r.json()