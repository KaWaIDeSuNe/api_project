
# Author: ldq<15611213733@163.com>
# Date:   2018-01-09


import regex


class Currency(object):
    def __init__(self):
        self.cn_nums = {
            '〇': 0,
            '一': 1,
            '二': 2,
            '三': 3,
            '四': 4,
            '五': 5,
            '六': 6,
            '七': 7,
            '八': 8,
            '九': 9,
        }
        self.cn_units = {
            '十': 10,
            '百': 10 ** 2,
            '千': 10 ** 3,
            '万': 10 ** 4,
            '亿': 10 ** 8,
        }
        self.patterns = [
            regex.compile(
                '(?P<bit>[千万亿]*)(?P<type>[元圆])|(?P<bit>[千万亿]+)(?P<type>[元圆]?)'),
            regex.compile(
                '(?P<type>人民币|港币|港元|美元|欧元|英镑|日元|韩元|加元|澳元|新西兰元|泰铢|越南盾)'),
            regex.compile('(?P<num>\d+\.?\d+)')
        ]
        self.currency_type_dict = {
            '人民币': 'CNY',
            '元': 'CNY',
            '圆': 'CNY',
            '港币': 'HKD',
            '港元': 'HKD',
            '美元': 'USD',
            '欧元': 'EUR',
            '英镑': 'GBP',
            '日元': 'JPY',
            '韩元': 'KRW',
            '加元': 'CAD',
            '澳元': 'AUD',
            '泰铢': 'THB',
            '越南盾': 'VND',
            '新西兰元': 'NZD',
        }

    def extract(self, _string):
        if _string is None:
            return '', ''
            # return ''
        _string = str(_string)
        bit, currency_type, number = None, None, None
        for pattern in self.patterns:
            match = pattern.search(_string)
            if match:
                d = match.groupdict()

                if d.get("bit"):
                    bit = self.cn_to_int(d["bit"])

                if d.get("type") in self.currency_type_dict:
                    currency_type = self.currency_type_dict[d["type"]]

                if d.get("num"):
                    number = d["num"]

        if bit is None:
            bit = 1
        if bit is not None and currency_type is None:
            currency_type = ''

        if number is None:
            number = ''
        else:
            number = float(number) * bit / (10 ** 4)

        number = self.float_to_str(number)

        return number, currency_type
        # return number

    def cn_to_int(self, s):
        if s[0] in self.cn_units:
            s = '一' + s
        match = regex.fullmatch(
            '((?P<nums>[〇一二三四五六七八九]+)(?P<units>[十百千万亿]*))+',
            s)
        if not match:
            return None

        ans = 0
        for nums, units in zip(match.capturesdict()['nums'],
                               match.capturesdict()['units']):
            num = ''
            for n in nums:
                num += str(self.cn_nums[n])
            unit = 1
            for u in units:
                unit *= self.cn_units.get(u, 1)
            ans += int(num) * unit
        return ans

    @staticmethod
    def float_to_str(number):
        if isinstance(number, str):
            return number
        return "%.2f" % number

    __call__ = extract


if __name__ == '__main__':
    txt = """50.000000万人民币    
    1000 万元    
    500 万元 
    100 万元 
    1001.000000万人民币    
    168.000000万人民币 
    500.000000万人民币 
    100 万元 
    200 万元 



    0.5万元人民币   
    500 万元 
    50 万元  
    10.000000万美元
    100 万元 
    60 万元  

    4万元人民币 

    50 万元  
    50.000000万人民币  

    10.000000万人民币  
    50 万元  
    10.000000万人民币  
    10.000000万人民币  
    100.000000万人民币 
    10.000000万人民币  
    5 万    
    50 万元 港元   
    30 万元  
    3.000000万人民币   
    5.000000万人民币   
    100 万元 
    50 万元  

    300.000000万人民币 
    108 万元 
    30.000000万人民币  
    50.000000万人民币  


    50 万元  

    10.000000万人民币  

    108.000000万人民币 
    50 万元  
    30.000000万人民币  
    50 万元  

    50 万元  


    3.000000万人民币   


    3.000000万人民币   


    30.000000万人民币  
    50.000000万人民币  
    3.000000万人民币   

    12.000000万美元   
    30.000000万人民币  

    200 万元 
    200 万元 
    10 万元  
    100.000000万人民币 
    200 万元 


    50.000000万人民币  
    50.000000万人民币  
    600 元 人民币  
    3.000000万人民币   
    10 万   

    60.000000万人民币  
    10.000000万人民币  

    150 万元 
    1000.000000万人民币    
    80.000000万人民币  

    100万元人民币   

    105.000000万人民币 
    50 万元  
    50 万元  
    30.000000万人民币  
    50.000000万人民币  
    300 万  
    (人民币)50万元  
    (人民币)110万元"""

    ext = Currency()
    for t in txt.split(u'\n'):
        print(ext(t), t)
    print(ext("2792万"))