#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2021 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import itertools
from lib.data.data import pyoptions
from lib.fun.fun import finishprinter, countchecker, range_compatible, finalsavepath, fun_name


def get_char_dic(objflag):
    storepath = finalsavepath(fun_name())

    countchecker(len(objflag), pyoptions.minlen, pyoptions.maxlen)

    # global variable transfer local variable to improved speed
    buffer = []
    buffer_size = pyoptions.buffer_size
    head = pyoptions.head
    tail = pyoptions.tail
    crlf = pyoptions.CRLF
    encode_name = pyoptions.encode
    encode_fun = pyoptions.operator.get(encode_name)

    with open(storepath, "a") as f:
        for i in range_compatible(pyoptions.minlen, pyoptions.maxlen+1):
            for item in itertools.product(objflag, repeat=i):
                if encode_name == "none":
                    buffer.append(head + "".join(item) + tail)
                else:
                    buffer.append(encode_fun(head + "".join(item) + tail))
                if len(buffer) == buffer_size:
                    f.write(crlf.join(buffer) + crlf)
                    buffer = []
        f.write(crlf.join(buffer))
    finishprinter(storepath)
