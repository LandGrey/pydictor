#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2020 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import operator
import functools
import traceback
from itertools import product
from lib.data.data import pystrs, pyoptions
from lib.fun.fun import finalsavepath, finishprinter, cool
from lib.parse.confparse import elementparser, confmatcher


def build_pattern_dic(source=""):
    storepath = finalsavepath("pattern")
    pattern_set = patterncore(source)
    char_list = [sorted(set(i)) for i in pattern_set.values()]

    # count word list lines
    count = functools.reduce(operator.mul, [len(i) for i in pattern_set.values()], 1)
    if count >= pyoptions.count_switcher:
        exit_msg = pyoptions.CRLF + cool.fuchsia("[!] Build items more than pyoptions.count_switcher: %s%s"
                                                 "[!] Modify /lib/data/data.py count_switcher to adjust it" %
                                                 (str(pyoptions.count_switcher), pyoptions.CRLF))
        exit(exit_msg)

    # global variable transfer local variable to improved speed
    buffer = []
    buffer_size = pyoptions.buffer_size
    head = pyoptions.head
    tail = pyoptions.tail
    crlf = pyoptions.CRLF
    encode_name = pyoptions.encode
    encode_fun = pyoptions.operator.get(encode_name)

    try:
        with open(storepath, "w") as f:
            for item in map("".join, product(*char_list)):
                if encode_name == "none":
                    buffer.append(head + item + tail)
                else:
                    buffer.append(encode_fun(head + item + tail))
                if len(buffer) == buffer_size:
                    f.write(crlf.join(buffer)+crlf)
                    buffer = []
            f.write(crlf.join(buffer))
        finishprinter(storepath, count)
    except Exception as e:
        print(cool.red('[-] Exception as following:') + pyoptions.CRLF)
        print(traceback.print_exc())


def patterncore(resource):
    pattern_dict = {}

    try:
        confdicts = elementparser(confmatcher(resource))
    except IndexError:
        confdicts = {}
        exit(cool.red("[-] parse element error, please check your parsing element"))
    finalen = len(confdicts[pystrs.conf_head])
    for x in range(0, finalen):
        pattern_set_list = confdicts[pystrs.conf_char][x]
        pattern_dict[x] = "".join(pattern_set_list)

    return pattern_dict
