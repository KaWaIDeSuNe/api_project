# -*- encoding:utf-8 -*-
# Author: ldq<15611213733@163.com>
# Date: 2019/4/17

import os

ENV_SWITCH = os.environ.get('ENV_SWITCH', 'dev')
NUM_PROCESSES = os.environ.get("NUM_PROCESSES")

if ENV_SWITCH == "online":
    # port
    AFFAIR_SERVER_PORT = "8632"
    # mongodb
    mongodb_db_path = ""
    # mysql
    db_path = ""
    mysql_user, mysql_pwd = "", ""
    # es
    es_user, es_pwd = "", ""
    NODE_CFGS = [
        {"host": "",
         "port": 9200},
        {"host": "",
         "port": 9200}]
    LOG_PATH_BASE = "log/"
else:
    # port
    AFFAIR_SERVER_PORT = "8632"
    # mongodb
    mongodb_db_path = ""
    # mysql
    db_path = ""
    mysql_user, mysql_pwd = "", ""
    # es
    es_user, es_pwd = "", ""
    NODE_CFGS = [
        {"host": "",
         "port": 9200}]
    LOG_PATH_BASE = ""

# log
LOG_OUT_NAME = "ServiceOut"
LOG_ERR_NAME = "ServiceErr"
LOG_INTERVAL = 1
SERVER_STARTUP_MSG = " server is running..."


mysql_db_cfg = {
    # "DB_NAME": {
    #     "db_config": {"path": db_path,
    #                   "port": 3306,
    #                   "user": mysql_user,
    #                   "pwd": mysql_pwd,
    #                   "db_name": "DB_NAME",
    #                   "max_cached": 10,
    #                   "min_cached": 1,
    #                   "max_connections": 10,
    #                   "charset": "utf8"}},

}

mongo_db_cfg = {
    # "DB_NAME": {
    #     "db_config": {"path": mongodb_db_path,
    #                   "port": 30000,
    #                   "user": "USER",
    #                   "pwd": "PWD",
    #                   "need_auth": True,
    #                   "db_name": "DB_NAME"},
    #     "collection_list": [
    #         "collection_name",
    #     ]},
}
