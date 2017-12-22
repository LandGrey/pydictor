#!/usr/bin/env python
# coding:utf-8
# author: LandGrey
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

from os.path import isfile
from lib.fun.decorator import magic
from lib.data.data import pyoptions
from lib.fun.fun import cool, finishcounter


def uniqifer_magic(*args):
    """[file]"""
    args = list(args[0])

    if len(args) == 2:
        original_file_path = args[1]
        if not isfile(original_file_path):
            exit(pyoptions.CRLF + cool.red("[-] File: {} don't exists".format(original_file_path)))
    else:
        exit(pyoptions.CRLF + cool.fuchsia("[!] Usage: {} {}".format(args[0], pyoptions.tools_info.get(args[0]))))

    @magic
    def uniqifer():
        with open(original_file_path) as o_f:
            for item in o_f.readlines():
                yield item.strip()

        print("[+] Source of  :{0} lines".format(cool.orange(finishcounter(original_file_path))))
