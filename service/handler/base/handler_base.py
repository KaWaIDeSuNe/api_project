# -*- encoding:utf-8 -*-
# Author: ldq <15611213733@163.com>

import base64
from datetime import datetime
import json
import logging

import tornado.web
from tornado import gen
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor

from utils.data_structure_checker import DataStructureChecker
from project_config import project_config
from project_config import project_constant


class HandlerBase(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(100)

    def __init__(self, application, request, **kwargs):
        tornado.web.RequestHandler.__init__(
            self, application, request, **kwargs)
        self._log_out = logging.getLogger(project_config.LOG_OUT_NAME)
        self._log_err = logging.getLogger(project_config.LOG_ERR_NAME)
        self.__field_black_set = {"null", "None", " "}

    @run_on_executor
    def sleep(self):
        request = tornado.escape.json_decode(self.request.body)
        finger = request.get("cookie")
        if finger is not None:
             cookie_json = base64.b64decode(finger)
             request["cookie"] = json.loads(cookie_json)
        responseContent = self.process(request)
        return responseContent

    '''
    classdocs
    '''

    @gen.coroutine
    def post(self):
        start_time = datetime.now()
        try:
            responseState, responseContent = yield self.sleep()
            responseContent = self.__response_content_handle(responseContent)
            query_result = {"responseContent": responseContent,
                            "responseState": responseState}
            end_time = datetime.now()
            # log
            self._log_out.info("port=" + str(self.request.uri) +
                               "\t({request_ip})".format(request_ip = self.request.remote_ip) +
                               "\trequest=" + str(self.request.body) +
                               "\tcost=" + str(end_time - start_time))
        except Exception as e:
            query_result = {"responseContent": str(e),
                            "responseState": 0}
            end_time = datetime.now()
            # log
            self._log_err.error("port=" + str(self.request.uri) +
                                "\t({request_ip})".format(
                                    request_ip=self.request.remote_ip) +
                                "\trequest=" + str(self.request.body) +
                                "\terr=" + str(e) +
                                "\tcost=" + str(end_time - start_time))
        finally:
            if isinstance(query_result, dict):
                responseContent = query_result.get("responseContent")
                if isinstance(responseContent, dict):
                    cookie = query_result.get("responseContent", {}).get("cookie")
                    if cookie is not None:
                        query_result["responseContent"]["cookie"] = base64.b64encode(json.dumps(cookie).encode()).decode()
            self.write(json.dumps(query_result))
            self.finish()


    """
    after the execution of this method, it will invoke post method.
    Because post is an generator, so this approach makes post method to be an
    async generator.
    """
    def process_query(self, request, callback):
        callback(self.process(request))

    """
    override custom method
    """
    def process(self, request):
        pass

    """
    in-params check
    """
    def in_params_check(self, request, request_constraint):
        return DataStructureChecker.do_check(request, request_constraint)

    """
    in-params check decorator
    """
    @staticmethod
    def in_params_check_decorator(request_constraint):
        def in_params_checker(func):
            def __decorator(self, request):
                if not self.in_params_check(request, request_constraint):
                    raise ValueError("unavailable request")
                return func(self, request)
            return __decorator
        return in_params_checker

    """
    fetch param, if not exist, return None
    """
    def get_in_params(self, request, in_params):
        result_list = []
        for param in in_params:
            result_list.append(request[param]
                               if param in request else None)
        return tuple(result_list)

    """
    logger decorator
    """
    @staticmethod
    def result_decorator(func):
        def __decorator(self, request):
            start_time = datetime.now()
            try:
                responseContent = func(self, request)
                if responseContent is project_constant.RETURN_EXCEPTION:
                    return project_constant.RESP_ERR_FEEDBACK
                return project_constant.RESP_SUC, responseContent
            except Exception as e:
                end_time = datetime.now()
                self._log_err.error("port=" + str(self.request.uri) +
                                    "\trequest=" + str(self.request.body) +
                                    "\terr=" + str(e) +
                                    "\tcost=" + str(end_time - start_time))
                return project_constant.RESP_ERR_FEEDBACK
        return __decorator

    def __response_content_handle(self, data):
        if isinstance(data, dict):
            data_dict = dict()
            for k, v in data.items():
                value = self.__response_content_handle(v)
                data_dict[k] = value
            return data_dict
        elif isinstance(data, list):
            data_list = list()
            for item in data:
                value = self.__response_content_handle(item)
                data_list.append(value)
            return data_list
        elif isinstance(data, str):
            if data in self.__field_black_set:
                data = ""
            return data
        elif data is None:
            return ""
        else:
            return data