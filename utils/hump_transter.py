# -*- encoding:utf-8 -*-
# Author: ldq <15611213733@163.com>
# Date:   2020/5/28

def convert(one_str, space_character="_"):  # one_string:输入的字符串；space_character:字符串的间隔符，以其做为分隔标志
    string_list = str(one_str).split(space_character)  # 将字符串转化为list
    first = string_list[0].lower()
    others = string_list[1:]

    others_capital = [word.capitalize() for word in others]  # str.capitalize():将字符串的首字母转化为大写

    others_capital[0:0] = [first]

    hump_string = ''.join(others_capital)  # 将list组合成为字符串，中间无连接符。
    return hump_string


def translate(obj, deep=0):
    if isinstance(obj, dict):
        _dict = dict()
        for key, value in obj.items():
            _dict[convert(key)] = translate(value, deep + 1)
        return _dict

    if isinstance(obj, list):
        _list = list()
        for value in obj:
            _list.append(translate(value, deep + 1))
        return _list
    return obj


def trans_wrapper(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        new_res = translate(res)
        return new_res
    return inner


if __name__ == '__main__':
    d = {"end_3rd_listing": 1}
    o = translate(d)
    print(o)



