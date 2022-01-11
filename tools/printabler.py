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
        with open(filepath, 'r') as f:
            for item in f.readlines():
                yield filter(lambda x: x in string.printable, item.strip())
