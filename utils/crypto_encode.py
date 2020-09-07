
#
# Author: ldq<15611213733@163.com>
# Date:   2018/3/27

import sys
import re
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class prpcrypt():
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        length = 16
        count = len(text)
        add = length - (count % length)
        text = text + ('#' * add)
        self.ciphertext = cryptor.encrypt(text)
        return b2a_hex(self.ciphertext)

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip('#')


class Encode(object):
    def __init__(self):
        self.__encode_way = prpcrypt("offsetcountcount")

    def encode_catalog(self, cookie):
        cookie_list = list()
        for cookie_key, cookie_value in cookie.items():
            cookie_str = "@".join([cookie_key, cookie_value])
            cookie_list.append(cookie_str)
        content_str = "!".join(cookie_list)
        return self.__encode_way.encrypt(content_str)

    def decode_catalog(self, raw_result):
        cookie = dict()
        content_str = self.__encode_way.decrypt(raw_result)
        cookie_list = content_str.split("!")
        for cookie_str in cookie_list:
            re_cookie = cookie_str.split("@")
            if len(re_cookie) != 2:
                return cookie
            cookie[re_cookie[0]] = re_cookie[1]
        return cookie

