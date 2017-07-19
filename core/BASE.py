#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import os
import string
import itertools
from lib.fun.filter import filterforfun
from lib.data.data import paths, pystrs,  pyoptions
from lib.fun.fun import finishprinter, finishcounter, countchecker, range_compatible, mybuildtime

# dictionary type
description = "init"


# get the dictionary list
def getchars(type, need_char=False):
    global description
    flag = str(type)
    chars = []
    if type in pystrs.base_dic_type and not need_char:
        if flag == pystrs.base_dic_type[0]:
            chars = string.digits
            description = 'd'
        elif flag == pystrs.base_dic_type[1]:
            chars = string.ascii_lowercase
            description = 'L'
        elif flag == pystrs.base_dic_type[2]:
            chars = string.ascii_uppercase
            description = 'c'
        elif flag == pystrs.base_dic_type[3]:
            chars = string.printable[:36]
            description = 'dL'
        elif flag == pystrs.base_dic_type[4]:
            chars = string.digits + string.ascii_uppercase
            description = 'dc'
        elif flag == pystrs.base_dic_type[5]:
            chars = string.ascii_letters
            description = 'Lc'
        elif flag == pystrs.base_dic_type[6]:
            chars = string.printable[:62]
            description = 'dLc'
        return chars
    elif need_char:
        description = "C"
        return type


def get_base_dic(objflag, need_char_dic=False):
    objflag = getchars(objflag, need_char=need_char_dic)
    countchecker(len(objflag), pyoptions.minlen, pyoptions.maxlen)
    global description
    dict_prefix = pystrs.BASE_prefix
    if need_char_dic:
        dict_prefix = pystrs.CHAR_prefix
    this_name = "%s_%s%s" % (dict_prefix, mybuildtime(), pyoptions.filextension)
    paths.results_file_name = this_name if not paths.results_file_name else paths.results_file_name
    storepath = os.path.join(paths.results_path, paths.results_file_name)
    with open(storepath, "a") as f:
        for i in range_compatible(pyoptions.minlen, pyoptions.maxlen+1):
            for item in itertools.product(objflag, repeat=i):
                item = filterforfun("".join(item), head=pyoptions.head, tail=pyoptions.tail,
                                    lenght_is_filter=pyoptions.args_pick,
                                    minlen=pyoptions.minlen, maxlen=pyoptions.maxlen,
                                    regex_is_filter=True, regex=pyoptions.filter_regex,
                                    encode_is_filter=True, encode=pyoptions.encode,
                                    occur_is_filter=True,
                                    letter_occur=pyoptions.letter_occur, digital_occur=pyoptions.digital_occur,
                                    types_is_filter=True,
                                    letter_types=pyoptions.letter_types, digital_types=pyoptions.digital_types,
                                    )
                if item:
                    f.write(item + pyoptions.CRLF)
    finishprinter(finishcounter(storepath), storepath)
