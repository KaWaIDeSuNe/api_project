# -*- encoding:utf-8 -*-

#
# Author: ldq<15611213733@163.com>
# Date: 2018/11/5

import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import logging

import tornado.httpserver
import tornado.ioloop
import tornado.options

from tornado.options import define, options

from project_config import project_config
from service.data_server.affair import AffairDataServer
from utils import init_logging as log
import importlib, sys

port = project_config.AFFAIR_SERVER_PORT
if not project_config.NUM_PROCESSES:
    NUM_PROCESSES = None
else:
    NUM_PROCESSES = int(project_config.NUM_PROCESSES)

define("port", default=port, help="run on the given port", type=int)

if __name__ == "__main__":
    importlib.reload(sys)
    sys.getdefaultencoding()
    tornado.options.parse_command_line()
    application = AffairDataServer()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.bind(options.port)
    print(type(NUM_PROCESSES))
    http_server.start(num_processes=NUM_PROCESSES)

    # logging
    log_out_file = "api_service_%s_out.log" % port
    log_err_file = "api_service_%s_err.log" % port
    log.init_log(project_config.LOG_OUT_NAME, log_out_file)
    log.init_log(project_config.LOG_ERR_NAME, log_err_file)
    LOGGER_OUT = logging.getLogger(project_config.LOG_OUT_NAME)
    LOGGER_ERR = logging.getLogger(project_config.LOG_ERR_NAME)
    LOGGER_OUT.info(project_config.SERVER_STARTUP_MSG)

    # loop
    tornado.ioloop.IOLoop.instance().start()
