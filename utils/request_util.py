# -*- encoding:utf-8 -*-

#
# Author: ldq<15611213733@163.com>
# Date: 2018/10/10

import requests
import json


class RequestsUtil(object):

    @staticmethod
    def post_request(url, data, ip, port):
        headers = {"Content-type": "application/json"}
        url = "http://{}:{}{}".format(ip, port, url)
        raw_result = requests.post(url, data=json.dumps(data), headers=headers)
        result = raw_result.content.decode("utf-8")
        result = json.loads(result)
        return result
