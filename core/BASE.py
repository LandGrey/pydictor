#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import string
import itertools
from lib.data.data import paths, pystrs,  pyoptions
from lib.fun.fun import finishprinter, finishcounter, countchecker, range_compatible, mybuildtime, finalsavepath


# get the dictionary list
def getchars(type, need_char=False):
    flag = str(type)
    chars = []
    if type in pystrs.base_dic_type and not need_char:
        if flag == pystrs.base_dic_type[0]:
            chars = string.digits
        elif flag == pystrs.base_dic_type[1]:
            chars = string.ascii_lowercase
        elif flag == pystrs.base_dic_type[2]:
            chars = string.ascii_uppercase
        elif flag == pystrs.base_dic_type[3]:
            chars = string.printable[:36]
        elif flag == pystrs.base_dic_type[4]:
            chars = string.digits + string.ascii_uppercase
        elif flag == pystrs.base_dic_type[5]:
            chars = string.ascii_letters
        elif flag == pystrs.base_dic_type[6]:
            chars = string.printable[:62]
        return chars
    elif need_char:
        return type


def get_base_dic(objflag, need_char_dic=False):
    objflag = getchars(objflag, need_char=need_char_dic)
    countchecker(len(objflag), pyoptions.minlen, pyoptions.maxlen)
    dict_prefix = pystrs.BASE_prefix
    if need_char_dic:
        dict_prefix = pystrs.CHAR_prefix
    storepath = finalsavepath(paths.results_path, dict_prefix, mybuildtime(), pyoptions.filextension, paths.results_file_name)
    with open(storepath, "a") as f:
        for i in range_compatible(pyoptions.minlen, pyoptions.maxlen+1):
            for item in itertools.product(objflag, repeat=i):
                f.write(pyoptions.operator.get(pyoptions.encode)(pyoptions.head + "".join(item) + pyoptions.tail) +
                        pyoptions.CRLF)
    finishprinter(finishcounter(storepath), storepath)
