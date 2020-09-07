# -*- encoding:utf-8 -*-
# Copyright (c) 2015 Shiye Inc.
# All rights reserved.
#
# Author: ldq <liangduanqi@shiyejinrong.com>
# Date: 2019/1/10 15:44
from concurrent.futures import ThreadPoolExecutor
import requests
import time

def get_data(url):
    print(url)
    res = requests.post(url[0],json=url[1]).text
    print(res)

if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=1000)
    import time
    s = time.time()
    for i in range(1000):
        take = executor.submit(get_data, ("http://127.0.0.1:8632/v1/a/apiDemo",{"userId": "test_user", "stCode": "20000"}))
    executor.shutdown()
    print(time.time()-s)
    # print(requests.post("http://127.0.0.1:9102/v2.0/companies/company_change_info",json={"user_id":"b888f12669c5405a962d7561a780b860","lawsuit_id":801,"company":"洛阳顺势药业有限公司","company_id":"431","employment_id":500}).text)
    # time.sleep(2)
