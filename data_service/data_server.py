# -*- encoding:utf-8 -*-
# Author: ldq <15611213733@163.com>

import threading

# 服务接口
from data_service.items.company.a.api_demo import CompanyAAPIDemo


class DataServer():
    _server = None
    _mutex = threading.Lock()

    @staticmethod
    def get_instance():
        if DataServer._server is None:
            DataServer._mutex.acquire()
            if DataServer._server is None:
                DataServer._server = DataServer()
            DataServer._mutex.release()
        return DataServer._server

    def __init__(self):
        #
        self.__company_a_api_demo_v1 = CompanyAAPIDemo()

        self.__db_interface_mapping = {
            "query_company_a_api_demo_v1": self.__company_a_api_demo_v1.query_company_a_api_demo_v1,
        }

    def query_db_interface(self, interface, param_dict=None):
        if param_dict is None:
            return self.__db_interface_mapping[interface]()
        return self.__db_interface_mapping[interface](param_dict)
