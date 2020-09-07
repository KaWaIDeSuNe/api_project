# -*- encoding:utf-8 -*-

#
# Author: ldq <15611213733@163.com>
# Date: 2018/11/30 8:55

from datetime import datetime,date

from utils.datetime_util import DateTimeUtil


class FieldHandlingBase(object):
    @staticmethod
    def field_cleaning(res_dict):
        '''
        清洗字段，把无效值去除（None，"无","null"）;
        :return: 去除无效字段后的字典
        '''
        clean_list = [None, "无", "null", "0", "——", "— —"]
        result = dict()
        for k in res_dict:
            if res_dict[k] not in clean_list:
                if isinstance(res_dict[k], int):
                    result[k] = res_dict[k]
                elif isinstance(res_dict[k], list):
                    result[k] = res_dict[k]
                elif isinstance(res_dict[k], dict):
                    result[k] = res_dict[k]
                else:
                    result[k] = res_dict[k].lstrip().replace('"', '')
        return result

    @staticmethod
    def update_dict(res_dict, key_map):
        for key_t in key_map:
            key_new, key_old = key_t
            res_dict[key_new] = res_dict.pop(key_old, "")
            if not res_dict[key_new]:
                res_dict.pop(key_new)
        return res_dict


if __name__ == '__main__':
    res_dict = {
        "name": "无",
        "age": " 15",
        "pass": None,
        "user_id": '',
    }
    res = FieldHandlingBase.field_cleaning(res_dict)
    print(res)
