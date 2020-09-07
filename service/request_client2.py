# -*- coding: utf-8 -*-

#
# Author: ldq <15611213733@163.com>
# Date:   2017-6-26
import json
from pprint import pprint

import requests


url = "http://39.105.197.73:7687/v2/companies/companyBaseInfo"
url = "http://39.105.197.73:7687/v2/companies/contactInformation"
url = "http://39.105.197.73:7687/v2/companies/companyProfile"
url = "http://39.105.197.73:7687/v2/companies/shareMortgages"   # 股权出质
url = "http://39.105.197.73:7687/v2/companies/IpMortgages"   # 知识产权出质
url = "http://39.105.197.73:7687/v2/companies/adminPunishments"   # 行政处罚信息
url = "http://39.105.197.73:7687/v2/companies/punishCriticism"   # 部门处罚批评
url = "http://39.105.197.73:7687/v2/companies/courtPoorCredit"   # 法院失信人
url = "http://39.105.197.73:8632/v1/companies/transferPlate/th"
# url = "http://39.105.197.73:8632/v1/investors/pedigree"
# url = "http://127.0.0.1:7687/v2/companies/abnormalOperations"   # 经营异常信息
# url = "http://127.0.0.1:7687/v2/companies/hearAnns"   # 开庭公告
# url = "http://127.0.0.1:7687/v2/companies/courtAnns"   # 法院公告
# url = "http://127.0.0.1:7687/v2/companies/lawsuits"   # 法律诉讼
# url = "http://127.0.0.1:7687/v2/companies/courtExecution"   # 法院执行
# url = "http://127.0.0.1:7687/v2/companies/ChattelMortgages"   # 动产抵押
# url = "http://127.0.0.1:7687/v2/companies/companyChangeInfo"   # 变更信息
# url = "http://127.0.0.1:8632/v1/companies/business"
# url = "http://127.0.0.1:8632/v1/companies/gg/a"
# url = "http://39.105.197.73:8632/v1/companies/gg/th"
# url = "http://127.0.0.1:8632/v1/companies/gg/th"
# url = "http://127.0.0.1:8632/v1/companies/ipo/a"
# url = "http://127.0.0.1:8632/v1/companies/news/a"
# url = "http://127.0.0.1:8632/v1/companies/news/a/detail"
# url = "http://127.0.0.1:8632/v1/companies/transferPlate/th"
# url = "http://127.0.0.1:8632/v1/investors/pedigree"
# url = "http://39.106.220.241:8632/v1/companies/news/a"
# url = "http://39.106.220.241:8632/v1/companies/seniorExecutives"
# url = "http://39.106.220.241:8632/v1/companies/business"

# url = "http://127.0.0.1:8632/v1/companies/seniorExecutives"
# url = "http://127.0.0.1:8632/v1/companies/news/th"
# url = "http://127.0.0.1:8632/v1/companies/news/th/detail"
# url = "http://39.105.197.73:8631/v1/companies/news/a/detail"

parm = {"userId": "violet", "cName": "深圳市漫步者科技股份有限公司", "type": 30}
# parm = {"userId": "violet", "stCode": "835692", "type": 30}
# parm = {"userId": "violet", "stCode": "002351", "limitNum": 40, 'cookie': 'eyJvZmZzZXQiOiAyMH0='}
parm = {"userId": "violet", "stCode": "835692", "limitNum": 20,}
parm = {"userId": "violet", 'newId': '5ef26b42b347d30611cc8f0f'}
parm = {"userId": "violet", 'newId': '5ef26b42b347d30611cc8f0f'}
# parm = {"userId": "violet", "cName": "北京视野金融信息服务有限公司", "limitNum": 30}

parm = {"userId": "violet", "stCode": "430556", "limitNum": 100,
# 'cookie': 'eyJkb2NpZHMiOiBbIjVlZDUzYTIzYjM0N2QzMDYxMWNiMmIzYSIsICI1ZWQ0YmZhNWIzNDdkMzA2MTFjYjIyOWMiLCAiNWVkNDgzNzFiMzQ3ZDMwNjExY2IxZWFmIiwgIjVlZDAyNjU0YjM0N2QzMDYxMWNhZjY3MSIsICI1ZWNjOTIyYWIzNDdkMzA2MTFjYWJmMmEiLCAiNWViZDM5ZjViMzQ3ZDMwNjExYzlmYmQ2IiwgIjVlYmE2MzJlYjM0N2QzMDYxMWM5Yzk5NyIsICI1ZWE4MTc0MmIzNDdkMzA2MTFjOGYyMTYiLCAiNWU5NTUxODNiMzQ3ZDMwNjExYzgwMDBhIiwgIjVlOTUzZWViYjM0N2QzMDYxMWM3ZmY4NiIsICI1ZTY1N2FmYWIzNDdkMzA2MTFjNWJmZTAiLCAiNWU0ZjJmNGFiMzQ3ZDMwNjExYzRhNjQ3IiwgIjVlNGYyM2VmYjM0N2QzMDYxMWM0YTU0YiIsICI1ZTRlOThhZmIzNDdkMzA2MTFjNDlmNTkiLCAiNWU0ZTY3YTNiMzQ3ZDMwNjExYzQ5Yjg3IiwgIjVlNGU0ZTllYjM0N2QzMDYxMWM0OTkyZiIsICI1ZTQyNWI3Y2IzNDdkMzA2MTFjM2RlY2MiLCAiNWU0MDQzYTFiMzQ3ZDMwNjExYzNiZTUyIiwgIjVlMzUzYmJkYjM0N2QzMDYxMWMzNDQ2MCIsICI1ZTMyNWZmMGIzNDdkMzA2MTFjMzJlOWUiXSwgIjBfbWluX2luZGV4IjogMTUsICIwX21pbiI6ICI1ZWJhNjMyZWIzNDdkMzA2MTFjOWM5OTciLCAiMF9tYXhfaW5kZXgiOiAxNSwgIjFfbWluX2luZGV4IjogMTQxLCAiMV9tYXgiOiAiNWVkNTNhMjNiMzQ3ZDMwNjExY2IyYjNhIiwgIjFfbWF4X2luZGV4IjogMTYwLCAibWF4X3RpbWUiOiAxNTkxMDMyMzU1LCAibWluX3RpbWUiOiAxNTgwMzU5NjY0LCAiMV9taW4iOiAiNWUzMjVmZjBiMzQ3ZDMwNjExYzMyZTllIiwgIjBfbWF4IjogIjVlYmE2MzJlYjM0N2QzMDYxMWM5Yzk5NyJ9'
        }
# parm = {"userId": "violet", "cName": "老铺黄金股份有限公司"}

parm = {"userId":"sdicfof_seeyii","stCode":"430556","limitNum":100,"startTime":"2010-04-12","endTime":"2019-10-12"}

parm = {"userId": "violet", "limitNum": 20, 'stCode': '837199'}
# parm = {"userId": "violet", "limitNum": 20, 'cookie': 'eyJza2lwX251bSI6IDIwfQ=='}
# parm = {"userId": "violet", "limitNum": 20, 'invName': '中国平安人寿保险股份有限公司'}

res = requests.post(url, data=json.dumps(parm))

res_load = json.loads(res.text)
pprint(res_load)
# print(len(res_load["responseContent"]["content"]))
# print(res_load["responseContent"]["cookie"])
# print(json.dumps(res_load, ensure_ascii=False))







