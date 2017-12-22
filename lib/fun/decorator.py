#!/usr/bin/env python
# coding:utf-8
# author: LandGrey
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
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
                item = filterforfun(item, head=pyoptions.head, tail=pyoptions.tail,
                                    lenght_is_filter=pyoptions.args_pick,
                                    minlen=pyoptions.minlen, maxlen=pyoptions.maxlen,
                                    regex_is_filter=True, regex=pyoptions.filter_regex,
                                    encode_is_filter=True, encode=pyoptions.encode,
                                    occur_is_filter=True,
                                    letter_occur=pyoptions.letter_occur,
                                    digital_occur=pyoptions.digital_occur,
                                    special_occur=pyoptions.special_occur,
                                    types_is_filter=True,
                                    letter_types=pyoptions.letter_types,
                                    digital_types=pyoptions.digital_types,
                                    special_types=pyoptions.special_types,
                                    )
                if item:
                    f.write(item + pyoptions.CRLF)
        finishprinter(storepath)
    except Exception as e:
        print(cool.red('[-] Exception as following:') + pyoptions.CRLF)
        print(traceback.print_exc())
