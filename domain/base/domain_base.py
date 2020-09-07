# -*- encoding:utf-8 -*-

#
# Author: ldq<15611213733@163.com>
# Date: 2018/11/5

import logging
from project_config import project_config
from data_service.data_server import DataServer


class DoMainBase(object):
    def __init__(self):
        self._data_server = DataServer.get_instance()
        self._log_out = logging.getLogger(project_config.LOG_OUT_NAME)
        self._log_err = logging.getLogger(project_config.LOG_ERR_NAME)
