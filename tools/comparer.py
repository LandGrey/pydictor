#!/usr/bin/env python
# coding:utf-8
# author: LandGrey
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import os
from lib.data.data import pyoptions
from lib.fun.filter import filterforfun
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
    with open(storepath, "a") as f:
        for item in minuend_list:
            if item not in subtrahend_list:
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
