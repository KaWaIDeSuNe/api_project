# -*- encoding:utf-8 -*-
#! /usr/local/bin/python

'''
Created on 2015-8-7

@author: ldq
'''

import unittest
import http.client
import json

from project_config import test_constant
from utils.data_structure_checker import DataStructureChecker


class TestServiceBase(unittest.TestCase):
    """
    set up
    """
    def setUp(self):
        self.httpClient = http.client.HTTPConnection(
            test_constant.REMOTE_HOST, test_constant.REMOTE_PORT,
            timeout=test_constant.TIME_OUT)
        self.headers = {"Content-type": "application/x-www-form-urlencoded",
                        "Accept": "text/plain"}

    def tearDown(self):
        """tear down"""
        if self.httpClient:
            self.httpClient.close()
        self.httpClient.close()

    def _getResponse(self, request, uri, constraint):
        params = json.dumps(request)
        self.httpClient.request("POST", uri, params, self.headers)
        response = self.httpClient.getresponse()
        result = response.read()
        result = json.loads(result)
        result = DataStructureChecker.do_check(result, constraint)
        return result

    def _get_response(self, request, uri):
        params = json.dumps(request)
        self.httpClient.request("POST", uri, params, self.headers)
        response = self.httpClient.getresponse()
        result = response.read().decode("utf-8")
        result = json.loads(result)
        return result

    @staticmethod
    def judge_result(raw_result):
        for re_result in raw_result:
            for re_key, re_value in re_result.items():
                if isinstance(re_value, str):
                    if re_key != re_value:
                        return False
                elif isinstance(re_value, dict):
                    for II_key, II_value in re_value.items():
                        if II_key == "gt":
                            if re_key <= II_value:
                                return False
                        elif II_key == "lt":
                            if re_key >= II_value:
                                return False
                        elif II_key == "gte":
                            if re_key < II_value:
                                return False
                        elif II_key == "lte":
                            if re_key > II_value:
                                return False
                        elif II_key == "equal":
                            if re_key != II_value:
                                return False
        return True
