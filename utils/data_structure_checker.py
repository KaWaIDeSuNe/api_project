# -*- encoding:utf-8 -*-
#! /usr/local/bin/python

'''
Created on 2015-8-7

@author: ldq
'''

import re


class DataStructureChecker(object):
    """
    dictionary check:
    1 completeness check.
    2 type check.
    3 format check.

    constraint may just like that:
    [
        {
            "element_name": "limit_num",
            "element_type": int,
            "element_value": (DataStructureChecker.GT_OP_TYPE, 1),
            "is_necessary": True
        },
        {
            "element_name": "header",
            "element_type": dict,
            "is_necessary": True,
            "constraint" :
            [
                {
                    "element_name": "strategy_name",
                    "element_type": str,
                    "is_necessary": True
                },
                {
                    "element_name": "strategy_desc",
                    "element_type": str,
                    "is_necessary": False,
                }
            ]
        },
        {
            "element_name" : "tb_title",
            "element_type" : list,
            "is_necessary": False,
            "constraint" :
            {
                "element_type" : str,
                "element_format" : r"\d{4}-\d{2}-\d{2}",
                "element_num" : 10
            }
        }
    ]
    """
    @staticmethod
    def dict_check(data, constraints):
        # ------ if request's type is not dict, return false ------
        if type(data) != dict:
            return False

        for constraint in constraints:
            if "is_necessary" in constraint:
                if constraint["is_necessary"]:
    # ------ completeness check ------
                    if constraint["element_name"] not in data:
                        return False
                else:
                    if constraint["element_name"] not in data:
                        continue
            else:
                if constraint["element_name"] not in data:
                    return False

    # ------ type check ------
            element_type = constraint["element_type"]
            if isinstance(element_type, tuple):
                if type(data[constraint["element_name"]]) not in element_type:
                    return False
            else:
                if not isinstance(data[constraint["element_name"]],
                                  element_type):
                    return False
    # ------ format check ------
            if "element_format" in constraint:
                if not re.match(constraint["element_format"],
                                data[constraint["element_name"]]):
                    return False
    # -------value check -------
            if "element_value" in constraint:
                if not DataStructureChecker.value_check(
                        data[constraint["element_name"]],
                        constraint["element_value"]):
                    return False
    # ------ sub check ------
            if "constraint" in constraint:
                if constraint["element_type"] == dict:
                    if not DataStructureChecker.dict_check(
                            data[constraint["element_name"]],
                            constraint["constraint"]):
                        return False
                elif constraint["element_type"] == list:
                    if not DataStructureChecker.list_check(
                            data[constraint["element_name"]],
                            constraint["constraint"]):
                        return False
        return True

    """
    value chenck:
    1 type check.
    2 value check.
    """

    @staticmethod
    def value_check(data, constraints):
    # ------ if request's type is not incomparable, return false ------
        if not (isinstance(data, int) or isinstance(data, float)
                or isinstance(data, basestring)):
            return False
    # -------value check-----------
        for constraint in constraints:
            if constraint[0] == "lt":
                if  data >= constraint[1]:
                    return False
            elif constraint[0] == "gt":
                if  data <= constraint[1]:
                    return False
            elif constraint[0] == "eq":
                if isinstance(constraint[1], tuple):
                    if data not in constraint[1]:
                        return False
                else:
                    if data != constraint[1]:
                        return False
            elif constraint[0] == "lte":
                if data > constraint[1]:
                    return False
            elif constraint[0] == "gte":
                if data < constraint[1]:
                    return False
            else:
                return False
        return True



    """
    list check:
    1 type check.
    2 format check.
    3 semantic check

    constraint just like that:
    example1:
    {
        "element_type": str,
        "element_format": r"\d{4}-\d{2}-\d{2}",
        "element_num": 10
    }
    {
            "element_type": int,
            "element_element": (DataStructureChecker.GT_OP_TYPE, 1)
        }

    example2:
    {
        "element_type": dict,
        "constraint":
        [
            ...
        ]
    }
    """
    @staticmethod
    def list_check(data, constraint):
        # ------ if request's type is not list, return false ------
        if not isinstance(data, list):
            return False

        for param in data:
    # ------ type check ------
            if not isinstance(param, constraint["element_type"]):
                return False
    # ------ format check ------
            if "element_format" in constraint:
                if not re.match(constraint["element_format"], param):
                    return False
    # -------value check -------
            if "element_value" in constraint:
                if not DataStructureChecker.value_check(
                        data[constraint["element_name"]],
                        constraint["element_value"]):
                    return False
    # ------ sub check ------
            if "constraint" in constraint:
                if constraint["element_type"] == dict:
                    if not DataStructureChecker.dict_check(
                            param, constraint["constraint"]):
                        return False
                elif constraint["element_type"] == list:
                    if not DataStructureChecker.list_check(
                            param, constraint["constraint"]):
                        return False
    # ------ semantic check ------
        if "element_num" not in constraint:
            return True
        if constraint["element_num"] == len(data):
            return True
        else:
            return False

    @staticmethod
    def do_check(data, constraint):
        if constraint["type"] == dict:
            return DataStructureChecker.dict_check(
                data, constraint["constraint"])
        elif constraint["type"] == list:
            return DataStructureChecker.list_check(
                data, constraint["constraint"])
        return False
