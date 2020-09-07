
#
# Author: ldq <15611213733@163.com>
# Date:   2017-6-26

from datetime import datetime
import threading

import pymongo
import json
import gridfs

from project_config import project_config


class MongodbManager(object):
    _server = None
    _mutex = threading.Lock()

    @staticmethod
    def get_instance():
        if MongodbManager._server is None:
            MongodbManager._mutex.acquire()
            if MongodbManager._server is None:
                MongodbManager._server = MongodbManager()
            MongodbManager._mutex.release()
        return MongodbManager._server

    def __init__(self):
        self.__client_list = list()
        self.__db_dict = dict()
        self.__data_dict = dict()
        for db_name, db_cfg in project_config.mongo_db_cfg.items():
            client, db, collection_dict = self.__init_db(
                db_cfg["db_config"], db_cfg["collection_list"])
            self.__client_list.append(client)
            self.__db_dict[db_name] = collection_dict
            self.__data_dict[db_name] = db

    def __init_db(self, db_cfg, collection_name_list):
        client = pymongo.MongoClient(
            db_cfg["path"], db_cfg["port"], socketTimeoutMS=20000)
        db = client.get_database(db_cfg["db_name"])
        if db_cfg["need_auth"] is True:
            db.authenticate(db_cfg["user"], db_cfg["pwd"])

        collection_dict = dict()
        for collection_name in collection_name_list:
            collection = db.get_collection(collection_name)
            collection_dict[collection_name] = collection
        return client, db, collection_dict

    def __del__(self):
        for client in self.__client_list:
            client.close()

    def query_count(self, db_name, collection_name, query_condition=None):
        if db_name not in self.__db_dict:
            return None
        collection_dict = self.__db_dict[db_name]
        if collection_name not in collection_dict:
            return None
        return collection_dict[collection_name].count(query_condition)

    def query_data(self, db_name, collection_name, query_condition=None,
                query_field=None, cur_method_dict=dict()):
        if db_name not in self.__db_dict:
            return None
        collection_dict = self.__db_dict[db_name]
        if collection_name not in collection_dict:
            return None
        query_result = collection_dict[collection_name].find(
            query_condition, query_field)
        for cur_method, cur_args in cur_method_dict.items():
            if cur_method == "sort":
                query_result = query_result.sort(cur_args)
            elif cur_method == "skip":
                query_result = query_result.skip(cur_args)
            elif cur_method == "limit":
                query_result = query_result.limit(cur_args)
        return list(query_result)

    def group_query_data(self,
            db_name, collection_name, key, condition, initial, reduce_js):
        if db_name not in self.__db_dict:
            return None
        collection_dict = self.__db_dict[db_name]
        if collection_name not in collection_dict:
            return None
        query_result = collection_dict[collection_name].group(
            key=key, condition=condition, initial=initial, reduce=reduce_js)
        return query_result

    def distinct_data(self,
            db_name, collection_name, distinct_field, query_condition):
        if db_name not in self.__db_dict:
            return None
        collection_dict = self.__db_dict[db_name]
        if collection_name not in collection_dict:
            return None
        query_result = collection_dict[collection_name].distinct(
            distinct_field, query_condition)
        return query_result

    def aggregate_data(self, db_name, collection_name, pipeline):
        if db_name not in self.__db_dict:
            return
        collection_dict = self.__db_dict[db_name]
        if collection_name not in collection_dict:
            return
        query_result = collection_dict[collection_name].aggregate(pipeline)
        return query_result

    def update_data(self, db_name, collection_name,
                    update_condition, update_data):
        if db_name not in self.__db_dict:
            return
        collection_dict = self.__db_dict[db_name]
        if collection_name not in collection_dict:
            return
        modify_time = datetime.now()
        update_data["modify_time"] = modify_time
        update_result = collection_dict[collection_name].update(
            update_condition, {"$set": update_data}, upsert=True)
        return update_result

    def gridfs_find(self, db_name, collection_name, query_condition,
                    sort_field=None, limit_n=None, skip_n=None, need_file_info=False):
        if db_name not in self.__db_dict:
            return
        collection_dict = self.__db_dict[db_name]
        if collection_name not in collection_dict:
            return
        fs = self.__create_gridfs(db_name, collection_name)
        query_result = fs.find(query_condition, no_cursor_timeout=False)
        if sort_field is not None:
            query_result = query_result.sort(sort_field)
        if limit_n is not None:
            query_result = query_result.limit(limit_n)
        if skip_n is not None:
            query_result = query_result.skip(skip_n)
        data_item_list = list()
        for result in query_result:
            data_item = result.read()
            data_item = json.loads(data_item.decode("utf-8"))
            if need_file_info is True:
                data_item["file_info"] = result._file
            data_item_list.append(data_item)
        return data_item_list

    def __create_gridfs(self, db_name, collection_name):
        if db_name not in self.__db_dict:
            return None
        collection_dict = self.__db_dict[db_name]
        if collection_name not in collection_dict:
            return None
        db = self.__data_dict[db_name]
        return gridfs.GridFS(db, collection=collection_name)