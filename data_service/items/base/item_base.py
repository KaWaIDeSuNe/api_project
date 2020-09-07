# -*- encoding:utf-8 -*-
# Author: ldq <15611213733@163.com>
    
from db_manager.mysql_manager import MysqlManager
from db_manager.es_manager import EsManager
from db_manager.mongodb_manager import MongodbManager


class MysqlBase(object):
    def __init__(self):
        self._db_manager = MysqlManager.get_instance()


class EsBase(object):
    def __init__(self):
        self._db_manager = EsManager.get_instance()


class MongodbBase(object):
    def __init__(self):
        self._db_manager = MongodbManager.get_instance()
