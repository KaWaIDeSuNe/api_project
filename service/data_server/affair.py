# -*- encoding:utf-8 -*-

# Author: ldq<15611213733@163.com>
# Date: 2018/11/5

import tornado.web
from service.handler.company.a.api_demo import CompanyAAPIDemoV1Handler


class AffairDataServer(tornado.web.Application):
    def __init__(self):
        """Constructor"""
        handlers = [
            (r"/v1/a/apiDemo", CompanyAAPIDemoV1Handler),
        ]
        tornado.web.Application.__init__(self, handlers=handlers)
