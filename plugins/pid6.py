#!/usr/bin/env python
# coding:utf-8
# author: LandGrey
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

from lib.data.data import pystrs
from lib.fun.decorator import magic
from lib.fun.fun import range_compatible


def pid6_magic(*args):
    """chinese id card last 6 digit"""

    posrule = lambda _: str(_) if _ >= 10 else "0" + str(_)
    # day
    value1314 = " ".join(posrule(x) for x in range_compatible(1, 32))
    value1516 = " ".join(posrule(x) for x in range_compatible(1, 100))
    post18 = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "X")
    value1718 = ""
    if pystrs.default_sex == pystrs.sex_range[0]:
        rand = ("1", "3", "5", "7", "9")
        for _ in rand:
            for _p in post18:
                value1718 += _ + _p + " "
    elif pystrs.default_sex == pystrs.sex_range[1]:
        rand = ("0", "2", "4", "6", "8")
        for _ in rand:
            for _p in post18:
                value1718 += _ + _p + " "
    elif pystrs.default_sex == pystrs.sex_range[2]:
        rand = " ".join(str(_) for _ in range_compatible(0, 10))
        for _ in rand.split(" "):
            for _p in post18:
                value1718 += _ + _p + " "

    @magic
    def pid6():
        for v1314 in value1314.split(" "):
            for v1516 in value1516.split(" "):
                for v1718 in value1718.split(" "):
                    if v1718 != "":
                        yield "".join(v1314 + v1516 + v1718)
