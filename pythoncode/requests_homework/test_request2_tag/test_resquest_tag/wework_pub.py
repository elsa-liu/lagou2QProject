import requests

from pythoncode.requests_homework.test_request2_tag.test_resquest_tag.base_api import BaseApi


class WeWork(BaseApi):
    def test_get_token(self):
        # ID = "ww72a13bb159fd5fee"
        # SECRET = "YymWsi34C4FWx4G3FnJCSur82ckeYhGJMM2VGAtrf4M"
        data={
            "method":"get",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params":{
                "corpid":"ww72a13bb159fd5fee",
                 "corpsecret":"YymWsi34C4FWx4G3FnJCSur82ckeYhGJMM2VGAtrf4M"
            }
        }

        r=self.send_api(data)

        #r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={ID}&corpsecret={SECRET}")
        return r['access_token']