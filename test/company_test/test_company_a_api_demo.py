# -*- encoding:utf-8 -*-
# Copyright (c) 2015 Shiye Inc.
# All rights reserved.
#
# Author: ldq <15611213733@163.com>
# Date: 2018/11/13 14:22

from test.test_service_base import TestServiceBase
# import unittest


class TestCompanyAAPIDemo(TestServiceBase):

    """
    test use case
    test_usecase_x_y
    x:
        1: normal
        2: margin
        3: exception
    y:
        seq.
    title: 工商处罚
    """
    def test_aaum_punishments_1_001(self):
        request = {"userId": "test_use_case",
                   "stCode": "221188"}
        result = self._get_response(request, "/v1/a/apiDemo")
        print(result)
        out_come = result["responseContent"]["content"][0]["stName"]
        target = "中国平安"
        self.assertTrue(out_come, target)

