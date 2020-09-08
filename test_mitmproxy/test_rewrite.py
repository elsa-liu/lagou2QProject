import json
from pprint import pprint

from mitmproxy import http
#
def response(flow: http.HTTPFlow):
    if "quote.json" in flow.request.url:
        data = json.loads(flow.response.content)
        print("==============获得的返回数据===================")
        pprint(data)
        #对数据进行修改
        data["data"]["items"][1]["quote"]["name"]=(data["data"]["items"][1]["quote"]["name"])*2
        data["data"]["items"][2]["quote"]["name"] = ""
        print("===============修改后的数据======================")
        pprint(data)
        flow.response.text = json.dumps(data)



# def response(flow: http.HTTPFlow):
#     # redirect to different host
#     if "quote.json" in flow.request.url and "x=" in flow.request.url:
#         ## 先接收到返回信息
#         data = json.loads(flow.response.content)
#         print("=============修改前的信息============================")
#         pprint(data)