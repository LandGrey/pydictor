#!/usr/bin/env python
# coding:utf-8
# author: LandGrey
"""
Copyright (c) 2016-2019 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import traceback
from lib.data.data import pyoptions
from lib.fun.filter import filterforfun
from lib.fun.fun import cool, unique, finalsavepath, finishprinter


def magic(func):
    storepath = finalsavepath(func.__name__)
    try:
        with open(storepath, "a") as f:
            for item in unique(func()):
                item = filterforfun(item)
                if item:
                    f.write(item + pyoptions.CRLF)
        finishprinter(storepath)
    except Exception as e:
        print(cool.red('[-] Exception as following:') + pyoptions.CRLF)
        print(traceback.print_exc())
