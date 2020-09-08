import requests
#企业微信通讯录的增加，获取，更新，删除
def test_get_token():
    ID = "ww72a13bb159fd5fee"
    SECRET = "YymWsi34C4FWx4G3FnJCSur82ckeYhGJMM2VGAtrf4M"

    r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={ID}&corpsecret={SECRET}")
    return r.json()['access_token']

class TestContact:
    s = requests.Session()
    s.params={"access_token":test_get_token()}

    def test_addmember(self):
        data={
            "userid": "zhangsan",
            "name": "张三",
            "mobile": "13800000000",
            "department": [1]
        }
        #r=requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.test_get_token()}",json=data)
        r=self.s.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",json=data)
        print(r.json())

    def test_get_member(self):
        params={
            "userid":"zhangsan"
        }
        r=self.s.get("https://qyapi.weixin.qq.com/cgi-bin/user/get",params=params)
        print(r.json())


    def test_update_member(self):
        data={
            "userid": "zhangsan",
            "name": "张三2",
            "mobile": "13800000001",
            "department": [1]
        }
        #r=requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.test_get_token()}",json=data)
        r=self.s.post("https://qyapi.weixin.qq.com/cgi-bin/user/update",json=data)

        print(r.json())

    def test_delete_member(self):
        params={
            "userid":"zhangsan"
        }
        #r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/delete",params=params)
        r=self.s.get("https://qyapi.weixin.qq.com/cgi-bin/user/delete",params=params)
        print(r.json())



