#!/usr/bin/env python
# coding:utf-8
# author: LandGrey
"""
Copyright (c) 2016-2019 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import datetime
from lib.fun.fun import cool, is_en
from lib.data.data import pyoptions
from lib.fun.decorator import magic
from rules.BaseTrick import dateshaper


def birthday_magic(*args):
    """[begin_date] [end_date], date format: [yyyyMMdd or ddMMyyyy(--dmy option)]"""
    args = list(args[0])
    if len(args) == 3:
        begin_date = args[1]
        end_date = args[2]
    else:
        exit(pyoptions.CRLF + cool.fuchsia("[!] Usage: {} {}".format(args[0], pyoptions.plugins_info.get(args[0]))))

    def check_date(dt, desc="datetime", ymd_format=True):
        """
        :return: year month day
        """
        if len(dt) != 8 or not dt.isdigit():
            exit(cool.fuchsia("[!] {} format:[{}], such as:{}{}".format(desc, "yyyMMdd" if ymd_format else "ddMMyyyy", "20150806" if ymd_format else "08062015", pyoptions.CRLF)))
        if ymd_format:
            if int(dt[4:6]) > 12 or int(dt[4:6]) < 1 or int(dt[6:8]) > 31 or int(dt[6:8]) < 1:
                exit(cool.fuchsia("[!] {} date format: 1<= month <=12 and 1<= day <=31{}".format(desc, pyoptions.CRLF)))
            else:
                return int(dt[0:4]), int(dt[4:6]), int(dt[6:8])
        else:
            if int(dt[2:4]) > 12 or int(dt[2:4]) < 1 or int(dt[0:2]) > 31 or int(dt[0:2]) < 1:
                exit(cool.fuchsia("[!] {} date format: 1<= month <=12 and 1<= day <=31{}".format(desc, pyoptions.CRLF)))
            else:
                return int(dt[4:8]), int(dt[2:4]), int(dt[0:2])

    def check_range(s, e):
        if s[0] > e[0] or (s[0] == e[0] and s[1] > e[1]) or (s[1] == e[1] and s[2] > e[2]):
            exit(cool.fuchsia("[!] Start date should later than End date" + pyoptions.CRLF))
        else:
            return True

    @magic
    def birthday():
        start_valid = check_date(begin_date, desc="Start datetime", ymd_format=pyoptions.ymd_format)
        end_valid = check_date(end_date, desc="End datetime", ymd_format=pyoptions.ymd_format)
        valid = check_range(start_valid, end_valid) if start_valid and end_valid else False
        if valid:
            res = []
            begin = datetime.datetime.strptime(begin_date, "%Y%m%d" if pyoptions.ymd_format else "%d%m%Y")
            end = datetime.datetime.strptime(end_date, "%Y%m%d" if pyoptions.ymd_format else "%d%m%Y")
            while begin <= end:
                date_str = begin.strftime("%Y%m%d" if pyoptions.ymd_format else "%d%m%Y")
                res.extend(dateshaper(date_str))
                begin += datetime.timedelta(days=1)
            return res
