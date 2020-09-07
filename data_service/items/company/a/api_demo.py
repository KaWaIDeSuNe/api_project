# -*- encoding:utf-8 -*-
# Author: ldq <15611213733@163.com>
# Date: 2020-09-05 14:05
# File : api_demo.py 


import pymongo

from data_service.items.base.item_base import MongodbBase
from utils.datetime_util import DateTimeUtil


class CompanyAAPIDemo(MongodbBase):
    def __init__(self):
        super(CompanyAAPIDemo, self).__init__()

    def query_company_a_api_demo_v1(self, param_dict):
        import time
        time.sleep(5)
        query_result = [{"stName": "中国平安"}]
        return query_result