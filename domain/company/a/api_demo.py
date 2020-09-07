# -*- encoding:utf-8 -*-
# Author: ldq <15611213733@163.com>
# Date: 2020-09-05 13:59
# File : api_demo.py 


from domain.base.domain_base import DoMainBase

from utils.datetime_util import DateTimeUtil
from utils.hump_transter import trans_wrapper


class DoMainCompanyAAPIDemoV1(DoMainBase):
    def __init__(self):
        super(DoMainCompanyAAPIDemoV1, self).__init__()

    def query_company_a_api_demo_v1(self, request):
        query_result = self._data_server.query_db_interface(
            "query_company_a_api_demo_v1", request)
        res = {"content": query_result}
        return res

