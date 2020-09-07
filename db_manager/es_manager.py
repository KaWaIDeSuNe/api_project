# -*- encoding:utf-8 -*-

#
# Author: ldq <15611213733@163.com>
# Date: 2018/12/3

import threading
from elasticsearch import Elasticsearch

from project_config.project_config import NODE_CFGS, es_user, es_pwd


class EsManager(object):
    _server = None
    _mutex = threading.Lock()

    @staticmethod
    def get_instance():
        if EsManager._server is None:
            EsManager._mutex.acquire()
            if EsManager._server is None:
                EsManager._server = EsManager()
                EsManager._mutex.release()
        return EsManager._server

    def __init__(self):
        self.__es = Elasticsearch(
            NODE_CFGS, http_auth=(es_user, es_pwd))

    def query_data(self, index, doc_type, body):
        query_results = self.__es.search(
            index=index,
            doc_type=doc_type,
            body=body,
            params={"timeout": "1s"})
        return query_results if query_results else None
