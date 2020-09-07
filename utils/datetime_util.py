
#
# Author: ldq <15611213733@163.com>
# Date:   2017-6-26

from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse


class DateTimeUtil(object):
    days_per_year = 365
    days_per_month = 30

    @staticmethod
    def today_base(h=0, m=0, s=0):
        return datetime.now().replace(
            hour=h, minute=m, second=s, microsecond=0)

    @staticmethod
    def today_base_str(str_format="%Y-%m-%d"):
        return datetime.now().strftime(str_format)

    @staticmethod
    def today_datetime_to_str(h=0, m=0, s=0):
        today_datetime = DateTimeUtil.today_base(h, m, s)
        return today_datetime.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_date_base(date_base):
        return date_base.replace(hour=0, minute=0, second=0, microsecond=0)

    @staticmethod
    def date_to_str(target_date, str_format="%Y-%m-%d"):
        return target_date.strftime(str_format)

    @staticmethod
    def datetime_to_str(target_date, str_format="%Y-%m-%d %H:%M:%S"):
        return target_date.strftime(str_format)

    @staticmethod
    def str_to_date(date_str, str_format="%Y-%m-%d"):
        return datetime.strptime(date_str, str_format)

    @staticmethod
    def get_date_by_delta(date_base, date_delta):
        return date_base + timedelta(days=date_delta)

    @staticmethod
    def get_date_str_by_delta(date_base_str, date_delta):
        date_base = DateTimeUtil.str_to_date(date_base_str)
        return DateTimeUtil.date_to_str(date_base + timedelta(days=date_delta))

    @staticmethod
    def generate_month_str_by_param(year, month, str_format="%Y-%m"):
        return datetime(year, month, 1).strftime(str_format)

    @staticmethod
    def parse_datetime_str(date_str):
        return parse(date_str)

    @staticmethod
    def convert_datetime_item(date_base, str_format="%Y-%m-%d"):
        if isinstance(date_base, datetime):
            return date_base.strftime(str_format)
        return date_base

    @staticmethod
    def generate_month_str_list(date_base, limit_num):
        result = [
            DateTimeUtil.date_to_str(
                DateTimeUtil.get_pre_month_by_delta(date_base, delta), "%Y-%m")
            for delta in xrange(limit_num)]
        return result

    @staticmethod
    def get_pre_month_by_delta(date_base, delta):
        if delta == 0:
            return date_base.replace(day=1)
        year = date_base.year
        month = date_base.month

        if delta < month:
            return datetime(year, month - delta, 1)
        month_delta = delta - month
        year_delta = month_delta / 12 + 1
        month_delta %= 12
        return datetime(year - year_delta, 12 - month_delta, 1)

    @staticmethod
    def get_date_by_quarter_delta(date_base, quarter_delta):
        year = date_base.year
        quarter = DateTimeUtil.get_quarter_by_date(date_base)
        if quarter_delta < quarter:
            return DateTimeUtil.gen_date_by_quarter(
                year, quarter - quarter_delta)
        delta = quarter_delta - quarter
        year_delta = delta / 4 + 1
        delta %= 4
        return DateTimeUtil.gen_date_by_quarter(year - year_delta, 4 - delta)

    @staticmethod
    def gen_date_by_quarter(year, quarter):
        month = quarter * 3 - 2
        return datetime(year, month, 1)

    @staticmethod
    def get_quarter_by_date(date_base):
        return (date_base.month + 2) / 3

    @staticmethod
    def gen_date(year, month, day):
        return datetime(year, month, day)

    @staticmethod
    def gen_date_by_half_year(year, half_num):
        month = 1 if half_num == 1 else 7
        return datetime(year, month, 1)

    @staticmethod
    def get_half_end_date_by_date(start_date):
        return (datetime(start_date.year, 6, 30)
                if start_date.month < 7
                else datetime(start_date.year, 12, 31))

