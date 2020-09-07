# -*- encoding:utf-8 -*-

#
# Author: ldq<15611213733@163.com>
# Date: 2018/11/5

# if method occurs exception, RETURN_EXCEPTION returns.
RETURN_EXCEPTION = None

# service response' status def.
RESP_ERR = 0
RESP_SUC = 1

# if service occurs exception, or failure, SERVICE_ERR_RESP returns.
RESP_ERR_FEEDBACK = 0, {}

# service's in-params format def.
# ================================  ===================================


query_company_a_api_demo_v1 = {
    "type": dict,
    "constraint": [
        {"element_name": "stCode",
         "element_type": str},
        {"element_name": "userId",
         "element_type": str}]
}

