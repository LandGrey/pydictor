#!/usr/bin/env python
# coding:utf-8
# author: LandGrey
"""
Copyright (c) 2016-2021 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import traceback
from lib.data.data import pyoptions
from lib.fun.filter import fff_speed
from lib.fun.fun import cool, unique, finalsavepath, finishprinter


def magic(func):
    storepath = finalsavepath(func.__name__)

    # global variable transfer local variable to improved speed
    buffer = []
    buffer_size = pyoptions.buffer_size
    head = pyoptions.head
    tail = pyoptions.tail
    crlf = pyoptions.CRLF
    encode_name = pyoptions.encode
    encode_fun = pyoptions.operator.get(encode_name)

    minlen = pyoptions.minlen
    maxlen = pyoptions.maxlen
    args_pick = pyoptions.args_pick
    letter_occur = pyoptions.letter_occur
    digital_occur = pyoptions.digital_occur
    special_occur = pyoptions.special_occur
    occur_is_filter = pyoptions.occur_is_filter
    letter_types = pyoptions.letter_types
    digital_types = pyoptions.digital_types
    special_types = pyoptions.special_types
    types_is_filter = pyoptions.types_is_filter
    letter_repeat = pyoptions.letter_repeat
    digital_repeat = pyoptions.digital_repeat
    special_repeat = pyoptions.special_repeat
    repeat_is_filter = pyoptions.repeat_is_filter
    filter_regex = pyoptions.filter_regex
    regex_is_filter = pyoptions.regex_is_filter

    try:
        with open(storepath, "a") as f:
            for item in unique(func()):
                item = fff_speed(item, head, tail, minlen, maxlen, args_pick, encode_fun,
                                 letter_occur, digital_occur, special_occur, occur_is_filter,
                                 letter_types, digital_types, special_types, types_is_filter,
                                 letter_repeat, digital_repeat, special_repeat, repeat_is_filter,
                                 filter_regex, regex_is_filter)
                if item:
                    buffer.append(item)
                    if len(buffer) == buffer_size:
                        f.write(crlf.join(buffer) + crlf)
                        buffer = []
            f.write(crlf.join(buffer))
        finishprinter(storepath)
    except Exception as e:
        print(cool.red('[-] Exception as following:') + pyoptions.CRLF)
        print(traceback.print_exc())
