#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import itertools
from lib.data.data import pyoptions
from lib.fun.fun import finishprinter, countchecker, range_compatible, finalsavepath, fun_name


def get_char_dic(objflag):
    storepath = finalsavepath(fun_name())

    countchecker(len(objflag), pyoptions.minlen, pyoptions.maxlen)
    with open(storepath, "a") as f:
        for i in range_compatible(pyoptions.minlen, pyoptions.maxlen+1):
            for item in itertools.product(objflag, repeat=i):
                if item:
                    f.write(pyoptions.operator.get(pyoptions.encode)(pyoptions.head + "".join(item) + pyoptions.tail) +
                            pyoptions.CRLF)

    finishprinter(storepath)
