# -*- encoding:utf-8 -*-

#
# Author: ldq<15611213733@163.com>
# Date: 2018/11/5

import threading
from DBUtils.PooledDB import PooledDB

import pymysql

from project_config import project_config
from utils.init_logging import init_log

LOGGER = init_log("MySQLDBManager", "violet_sql_processor.log")


class MysqlManager(object):
    _server = None
    _mutex = threading.Lock()

    def __init__(self):
        self.__client_dict = dict()
        for db_name, db_cfg in project_config.mysql_db_cfg.items():
            mysql_db_cfg = db_cfg["db_config"]
            re_pool = PooledDB(
                creator=pymysql,
                mincached=mysql_db_cfg["min_cached"],
                maxcached=mysql_db_cfg["max_cached"],
                maxconnections=mysql_db_cfg["max_connections"],
                host=mysql_db_cfg["path"],
                port=mysql_db_cfg["port"],
                user=mysql_db_cfg["user"],
                passwd=mysql_db_cfg["pwd"],
                db=mysql_db_cfg["db_name"],
                # use_unicode=False,
                charset=mysql_db_cfg["charset"])
            self.__client_dict[db_name] = re_pool

    @staticmethod
    def get_instance():
        if MysqlManager._server is None:
            MysqlManager._mutex.acquire()
            if MysqlManager._server is None:
                MysqlManager._server = MysqlManager()
            MysqlManager._mutex.release()
        return MysqlManager._server

    def __del__(self):
        for db_name, client in self.__client_dict.items():
            client.close()

    def query_data(self, db_name, query_condition):
        conn = None
        cur = None
        try:
            conn = self.__client_dict[db_name].connection()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(query_condition)
            data = cur.fetchall()
            return data or list()
        except Exception as e:
            LOGGER.exception(str(e))
            return list()
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
