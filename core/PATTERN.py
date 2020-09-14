#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2020 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import operator
import itertools
import functools
import traceback
from core.CONF import get_conf_dic
from lib.fun.filter import encode_filter
from lib.data.data import pystrs, pyoptions
from lib.fun.fun import finalsavepath, finishprinter, cool
from lib.parse.confparse import elementparser, confmatcher


def build_pattern_dic(source=""):
    buffer = []
    buffer_size = 512
    storepath = finalsavepath("pattern")
    pattern_set = patterncore(source)
    char_list = [sorted(set(i)) for i in pattern_set.values()]
    try:
        with open(storepath, "w") as f:
            for item in map("".join, itertools.product(*char_list)):
                item = pyoptions.head + item + pyoptions.tail
                buffer.append(item if pyoptions.encode == "none" else encode_filter(item, encode=pyoptions.encode))
                if len(buffer) == buffer_size:
                    f.write(pyoptions.CRLF.join(buffer) + pyoptions.CRLF)
                    buffer = []
            f.write(pyoptions.CRLF.join(buffer))
        finishprinter(storepath)
    except Exception as e:
        print(cool.red('[-] Exception as following:') + pyoptions.CRLF)
        print(traceback.print_exc())


def patterncore(resource):
    pattern_set = {}

    try:
        confdicts = elementparser(confmatcher(resource))
    except IndexError:
        confdicts = {}
        exit(cool.red("[-] parse element error, please check your parsing element"))
    finalen = len(confdicts[pystrs.conf_head])
    for x in range(0, finalen):
        # pattern_set_list = confdicts[pystrs.conf_char][x]
        # keep parsing head and tail
        pattern_set_list = get_conf_dic(int(confdicts[pystrs.conf_minlen][x]),
                                        int(confdicts[pystrs.conf_maxlen][x]),
                                        confdicts[pystrs.conf_char][x],
                                        confdicts[pystrs.conf_encode][x],
                                        confdicts[pystrs.conf_head][x],
                                        confdicts[pystrs.conf_tail][x])
        pattern_set[x] = "".join(pattern_set_list)
    count = functools.reduce(operator.mul, [len(i) for i in pattern_set.values()], 1)
    if count >= pyoptions.count_switcher:
        exit_msg = pyoptions.CRLF + cool.fuchsia("[!] Build items more than pyoptions.count_switcher: %s%s"
                                                 "[!] Modify /lib/data/data.py count_switcher to adjust it" %
                                                 (str(pyoptions.count_switcher), pyoptions.CRLF))
        exit(exit_msg)
    return pattern_set
