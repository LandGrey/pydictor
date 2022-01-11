#!/usr/bin/env python
# coding:utf-8
# author: LandGrey
"""
Copyright (c) 2016-2021 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import os
from lib.data.data import pyoptions
from lib.fun.filter import fff_speed
from lib.fun.fun import walk_pure_file, cool, finishprinter, finalsavepath, fun_name


def comparer_magic(*args):
    """[minuend_file] [subtrahend_file]"""
    args = list(args[0])

    if len(args) != 3:
        exit(pyoptions.CRLF + cool.fuchsia("[!] Usage: {} {}".format(args[0], pyoptions.tools_info.get(args[0]))))
    storepath = finalsavepath(fun_name())

    minuend_file = args[1]
    subtrahend_file = args[2]
    if not os.path.isfile(os.path.abspath(pyoptions.args_tool[1])):
        exit(pyoptions.CRLF + cool.red("[-] file: {} don't exists".format(minuend_file)))
    if not os.path.isfile(os.path.abspath(pyoptions.args_tool[2])):
        exit(pyoptions.CRLF + cool.red("[-] file: {} don't exists".format(subtrahend_file)))

    minuend_list = walk_pure_file(minuend_file)
    subtrahend_list = walk_pure_file(subtrahend_file)

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

    with open(storepath, "a") as f:
        for item in minuend_list:
            if item not in subtrahend_list:
                item = fff_speed(item, head, tail, minlen, maxlen, args_pick, encode_fun,
                                 letter_occur, digital_occur, special_occur, occur_is_filter,
                                 letter_types, digital_types, special_types, types_is_filter,
                                 letter_repeat, digital_repeat, special_repeat, repeat_is_filter,
                                 filter_regex, regex_is_filter)
                if item:
                    f.write(item + pyoptions.CRLF)

    finishprinter(storepath)
