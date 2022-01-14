#!/usr/bin/env python
# coding:utf-8
# author: LandGrey
"""
Copyright (c) 2016-2022 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import os
import string
from lib.fun.fun import cool
from lib.fun.decorator import magic
from lib.data.data import pyoptions
from lib.fun.osjudger import py_ver_egt_3


def printabler_magic(*args):
    """[filepath]"""
    args = list(args[0])

    if len(args) >= 2:
        filepath = args[1]
    else:
        exit(pyoptions.CRLF + cool.fuchsia("[!] Usage: {} {}".format(args[0], pyoptions.tools_info.get(args[0]))))
    if not os.path.isfile(filepath):
        exit(cool.red("[-] File don't exits" + pyoptions.CRLF))

    @magic
    def printabler():
        is_py3 = py_ver_egt_3()
        if is_py3:
            f = open(filepath, 'r', encoding='utf8', errors='replace')
        else:
            import codecs
            f = codecs.open(filepath, 'r', encoding='utf8', errors='replace')
        for item in f:
            item = item.strip()
            if item:
                ret = filter(lambda x: x in string.printable, item)
                if is_py3:
                    if len(list(ret)) == len(item):
                        yield item
                else:
                    if len(ret) == len(item):
                        yield item
        f.close()
