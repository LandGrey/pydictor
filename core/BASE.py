#!/usr/bin/env python
# coding:utf-8
# Build a dictionary based on common character set
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
import os
import string
import itertools
from lib.fun import finishprinter, finishcounter, countchecker, range_compatible
from lib.data import get_result_store_path, get_buildtime, operator, CRLF, BASE_prefix, CHAR_prefix, filextension, \
    base_dic_type

# dictionary type
description = "init"


# get the dictionary list
def getchars(type, need_char=False):
    global description
    flag = str(type)
    chars = []
    if type in base_dic_type and not need_char:
        if flag == base_dic_type[0]:
            chars = string.digits
            description = 'digits'
        elif flag == base_dic_type[1]:
            chars = string.ascii_lowercase
            description = 'lowercase'
        elif flag == base_dic_type[2]:
            chars = string.ascii_uppercase
            description = 'uppercase'
        elif flag == base_dic_type[3]:
            chars = string.printable[:36]
            description = 'digits_lowercase'
        elif flag == base_dic_type[4]:
            chars = string.digits + string.ascii_uppercase
            description = 'digits_uppercase'
        elif flag == base_dic_type[5]:
            chars = string.ascii_letters
            description = 'letters'
        elif flag == base_dic_type[6]:
            chars = string.printable[:62]
            description = 'digits_letters'
        return chars
    elif need_char:
        description = "chars"
        return type


def get_base_dic(minlength, maxlength, objflag, encodeflag, head, tail, need_char_dic=False):
    objflag = getchars(objflag, need_char=need_char_dic)
    countchecker(len(objflag), minlength, maxlength)
    global description
    dict_prefix = BASE_prefix
    if need_char_dic:
        dict_prefix = CHAR_prefix
    storepath = os.path.join(get_result_store_path(), "%s_%s_%s_%s_%s_%s%s" %
                             (dict_prefix, minlength, maxlength, description, get_buildtime(), encodeflag, filextension))
    with open(storepath, "a") as f:
        for i in range_compatible(minlength, maxlength+1):
            for item in itertools.product(objflag, repeat=i):
                f.write(operator.get(encodeflag)(head + "".join(item) + tail) + CRLF)
    finishprinter(finishcounter(storepath), storepath)
