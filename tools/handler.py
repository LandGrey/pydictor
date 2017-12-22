#!/usr/bin/env python
# coding:utf-8
# author: LandGrey
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import os
from lib.fun.fun import cool
from lib.fun.decorator import magic
from lib.data.data import pyoptions


def handler_magic(*args):
    """[file]"""
    args = list(args[0])

    if len(args) >= 2:
        path = args[1]
    else:
        exit(pyoptions.CRLF + cool.fuchsia("[!] Usage: {} {}".format(args[0], pyoptions.tools_info.get(args[0]))))
    if not os.path.isfile(path):
        exit(cool.red("[-] File don't exits" + pyoptions.CRLF))

    @magic
    def handler():
        with open(path, 'r') as f:
            for item in f.readlines():
                yield item.strip()
