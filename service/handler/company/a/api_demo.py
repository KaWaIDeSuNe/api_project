# -*- encoding:utf-8 -*-
# Author: ldq <15611213733@163.com>
# Date: 2020-09-05 13:54
# File : api_demo.py 


from domain.company.a.api_demo import DoMainCompanyAAPIDemoV1
from project_config import project_constant
from service.handler.base.handler_base import HandlerBase


class CompanyAAPIDemoV1Handler(HandlerBase):
    __get_constraint = project_constant.query_company_a_api_demo_v1

    def __init__(self, application, request, **kwargs):
        HandlerBase.__init__(self, application, request, **kwargs)
        self.__company_selector = DoMainCompanyAAPIDemoV1()

    @HandlerBase.result_decorator
    @HandlerBase.in_params_check_decorator(__get_constraint)
    def process(self, request):
        response_content = (
            self.__company_selector.query_company_a_api_demo_v1(request))
        return response_content