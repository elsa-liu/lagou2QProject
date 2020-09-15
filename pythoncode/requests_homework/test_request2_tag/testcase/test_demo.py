import pytest
import requests
'''
#企业微信标签
#1.实现最基本的7项功能
#2.将参数进行数据驱动
#3.可以自己制造随机参数
#4.xdist插件实现并行
#5.PO模式封装
#6.用PO模式封装 不能按此demo进行session的设置，因此使用老师的@pytest.fixtrue进行设置
'''

#获取token
def test_get_token():
    ID = "ww72a13bb159fd5fee"
    SECRET = "YymWsi34C4FWx4G3FnJCSur82ckeYhGJMM2VGAtrf4M"

    r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={ID}&corpsecret={SECRET}")
    return r.json()['access_token']
#制造随机参数方法1
def create_data():
    pass
    # data = [(str(random.randint(0, 999999)),
    #          "zhangsan1",
    #          str(random.randint(13800000000, 13899999999))
    #          ) for x in range(10)]


#制造随机参数方法2
def create_data2():
    data = [("c"+str(x),int(x)+13,["1user"+str(x),"2user"+str(x)],["1par"+str(x),"2par"+str(x)])for x in range(10)]
    # data = [("wu12345wu" + str(x), "zhangsan1", "138%08d" % x) for x in range(20)]
    return data

class TestContactTag:
    # #实例化session
    # s = requests.Session()
    # #将token值放置session中
    # s.params={"access_token":test_get_token()}
    @pytest.fixture(scope="session")
    def token(self):
        return test_get_token()


    def test_addtag(self,tagname,tagid,token):
        data={
            "tagname": tagname,
            "tagid": tagid
        }
        r=requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}",json=data)
        #r=self.s.post("https://qyapi.weixin.qq.com/cgi-bin/tag/create",json=data)
        print(r.json())
        return r.json()

    def test_get_taguser(self,tagid,token):
        params={
            "access_token":token,
            "tagid": tagid
        }
        r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/tag/get",params=params)
        print(r.json())
        return r.json()


    def test_update_tag(self,tagid,tagname,token):
        data={
               "tagid": tagid,
               "tagname": tagname
            }

        r=requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={token}",json=data)

        print(r.json())
        return r.json()

    def test_delete_tag(self,token,tagid=13):
        params={
            "access_token":token,
            "tagid":tagid
        }
        r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/delete",params=params)
        #r=self.s.get("https://qyapi.weixin.qq.com/cgi-bin/tag/delete",params=params)
        print(r.json())
        return r.json()

    def test_add_taguser(self,tagid,userlist,partylist,token):
        #函数的变量不能是可变对象？？ 待解决
        data={
            "tagid": tagid,
            "userlist": userlist,
            "partylist": partylist
        }
        r=requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers?access_token={token}", json=data)
        #r = self.s.post("https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers", json=data)
        print(r.json())
        return r.json()

    def test_del_taguser(self,tagid,userlist,partylist,token):
        data={
            "tagid": tagid,
            "userlist": userlist,
            "partylist": partylist
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers?access_token={token}",json=data)
        print(r.json())
        return r.json()

    def test_get_taglist(self,token):
        r=requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={token}")
        #r = self.s.get("https://qyapi.weixin.qq.com/cgi-bin/tag/list")
        print(r.json())
        return r.json()


    @pytest.mark.parametrize("tagname,tagid,userlsit,partylist",create_data2())
    def test_all(self,tagname,tagid,userlsit,partylist,token):
        print(f"{tagname},{tagid},{userlsit},{partylist}")
        #1.创建标签,并且处理创建标签过程中的异常
        try:
            assert "created" == self.test_addtag(tagname,tagid,token)["errmsg"]
        except AssertionError as e:
            print(e)
            if "invalid tagid" in e.__str__():
                #2.删除标签
                self.test_delete_tag(token,tagid)
                assert "created" == self.test_addtag(tagname,tagid,token)["errmsg"]
        #2.更新标签名，并断言
        update_tagname=tagname+"update"
        assert "updated" == self.test_update_tag(tagid,update_tagname,token)["errmsg"]
        #8.获取标签列表，并断言
        assert "ok" == self.test_get_taglist(token)["errmsg"]
        #4.获取标签成员
        assert "ok" == self.test_get_taguser(tagid,token)["errmsg"]
        #5.增加标签成员
        self.test_add_taguser(tagid,userlsit,partylist,token)
        #7.删除标签成员
        self.test_del_taguser(tagid,userlsit,partylist,token)













