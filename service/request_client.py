# -*- coding: utf-8 -*-

#
# Author: ldq <15611213733@163.com>
# Date:   2017-6-26

import http.client
import json
from datetime import datetime
from pprint import pprint


def query_news():
    httpClient = None
    try:
        # request_1_1 = {
        #     "stCode": "01257",
        #     "userId": "test_use_case",
        #     "limitNum": 1,
        #     "startTime": "2018-08-07",
        #     'cookie': {'finger': 'eyJvZmZzZXQiOiAiMjAxOC0wOC0wNyAxNDoxMzozMyJ9'},
        # }
        request_1_1 = {
            "cName": "杭州宏华数码科技股份有限公司",
            # "stCode": "00999",
            # "cikCode": "0001690666",
            "userId": "test_use_case",
            "cikCode": '0001534263',
            # "quoteType": 2,
            # "limitNum": 10,
            # "factorType": 1,
            # "cookie": "eyJvZmZzZXQiOiAiMjAyMC0wMy0zMCAwMDowMDowMCJ9"
        }

        start = datetime.now()
        params = json.dumps(request_1_1)
        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Accept": "text/plain"}
        # httpClient = http.client.HTTPConnection("127.0.0.1", 8632, timeout=30)
        httpClient = http.client.HTTPConnection("39.106.220.241", 8632, timeout=30)
        # httpClient = http.client.HTTPConnection("39.105.197.73", 8655, timeout=30)
        # httpClient = http.client.HTT/v2/companies/seniorPConnection("39.105.197.73", 8655, timeout=30)
        httpClient.request(
            # "POST", "/v1/companies/categoryInfo", params, headers)
            "POST", "/v1/companies/ipo/a", params, headers)
            # "POST", "/v1/us/companies/instant/ipo", params, headers)
        response = httpClient.getresponse()
        # print response.getheaders()
        # print response.status
        # print response.reason
        result = response.read().decode("utf-8")
        result = json.loads(result)
        pprint(result)
        # with open("第一创业证券股份有限公司.json","w") as f:
        #     json.dump(result, f, ensure_ascii=False, indent=5)
        # pprint(result)
        end = datetime.now()
        print(end - start)
    except Exception as e:
        print(e)
    finally:
        if httpClient is not None:
            httpClient.close()


if __name__ == "__main__":
    query_news()

