
#
# Author: ldq <15611213733@163.com>
# Date:   2017-6-26
from datetime import datetime, date

from utils.datetime_util import DateTimeUtil


def dict_fetch(data, keys, default=None):
    ret = dict()
    for key_item in keys:
        if isinstance(key_item, tuple):
            key_path = key_item[0].split(".")
            value = data.copy()
            for key in key_path:
                value = value.get(key, default)
                if value == default:
                    break

            if len(key_item) > 2:
                value = (key_item[2](value)
                         if value != default else default)
            if value is None:
                continue
            ret[key_item[1]] = value
        else:
            if key_item not in data:
                if default is not None:
                    ret[key_item] = default
            else:
                ret[key_item] = data[key_item]
    return ret


def set_all_date_to_str(data):
    for key, value in data.items():
        if isinstance(value, date) or isinstance(value, datetime):
            data[key] = DateTimeUtil.date_to_str(value)


def filter_invalid_value(clas_diagram):
    if isinstance(clas_diagram, dict):
        for key in clas_diagram.keys():
            value = clas_diagram[key]
            if isinstance(value, (str)):
                if value == "null":
                    del clas_diagram[key]
            elif value is None:
                del clas_diagram[key]
            else:
                filter_invalid_value(value)

    if isinstance(clas_diagram, list):
        for value in clas_diagram:
            filter_invalid_value(value)