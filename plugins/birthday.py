#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import datetime
from lib.fun.fun import cool
from rules.BaseTrick import dateshaper
from lib.fun.filter import filterforfun
from lib.data.data import paths, pystrs, pyoptions
from lib.fun.fun import finishprinter, finishcounter, finalsavepath, mybuildtime, unique


def birthday_magic(begin_date, end_date):
    def check_date(dt, desc="datetime"):
        if len(dt) != 8 or not dt.isdigit():
            exit(cool.fuchsia("[!] {} format:[YYYYMMDD], such as:19900512{}".format(desc, pyoptions.CRLF)))
        elif int(dt[4:6]) > 12 or int(dt[4:6]) < 1 or int(dt[6:8]) > 31 or int(dt[6:8]) < 1:
            exit(cool.fuchsia("[!] {} date format: 1<= month <=12 and 1<= day <=31{}".format(desc, pyoptions.CRLF)))
        else:
            return int(dt[:4]), int(dt[4:6]), int(dt[6:])

    def check_range(s, e):
        if s[0] > e[0] or (s[0] == e[0] and s[1] > e[1]) or (s[1] == e[1] and s[2] > e[2]):
            exit(cool.fuchsia("[!] Start date should later than End date" + pyoptions.CRLF))
        else:
            return True

    start_valid = check_date(begin_date, desc="Start datetime")
    end_valid = check_date(end_date, desc="End datetime")
    valid = check_range(start_valid, end_valid) if start_valid and end_valid else False
    storepath = finalsavepath(paths.results_path, pystrs.BIRTHDAY_prefix, mybuildtime(), pyoptions.filextension,
                              paths.results_file_name)
    if valid:
        res = []
        begin = datetime.datetime.strptime(begin_date, "%Y%m%d")
        end = datetime.datetime.strptime(end_date, "%Y%m%d")
        while begin <= end:
            date_str = begin.strftime("%Y%m%d")
            res.extend(dateshaper(date_str))
            begin += datetime.timedelta(days=1)
        with open(storepath, "a") as f:
            for item in unique(res):
                item = filterforfun(item, head=pyoptions.head, tail=pyoptions.tail,
                                    lenght_is_filter=pyoptions.args_pick,
                                    minlen=pyoptions.minlen, maxlen=pyoptions.maxlen,
                                    encode_is_filter=True, encode=pyoptions.encode,
                                    )
                if item:
                    f.write(item + pyoptions.CRLF)
        finishprinter(finishcounter(storepath), storepath)
