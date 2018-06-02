#!/usr/bin/env python
# coding:utf-8
# author: LandGrey
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import os
import traceback
import mimetypes
from lib.data.data import pyoptions
from lib.fun.decorator import magic
from lib.fun.fun import cool, finalsavepath, finishcounter


def uniqbiner_magic(*args):
    """[dir]"""
    args = list(args[0])

    if len(args) == 2:
        directory = os.path.abspath(args[1])
    else:
        exit(pyoptions.CRLF + cool.fuchsia("[!] Usage: {} {}".format(args[0], pyoptions.tools_info.get(args[0]))))

    filepaths = []
    combine_list = []
    for rootpath, subdirsname, filenames in os.walk(directory):
        filepaths.extend([os.path.abspath(os.path.join(rootpath, _)) for _ in filenames])
    if len(filepaths) > 0:
        for _ in filepaths:
            if mimetypes.guess_type(_)[0] == 'text/plain':
                combine_list.append(_)
    tempath = finalsavepath("combiner")

    try:
        with open(tempath, "a") as f:
            for onefile in combine_list:
                with open(onefile, 'r') as tf:
                    for line in tf.readlines():
                        f.write(line.strip() + pyoptions.CRLF)
    except Exception as ex:
        print(pyoptions.CRLF + cool.red("[-] Combine file failed, Looking: "))
        exit(pyoptions.CRLF + traceback.print_exc())

    @magic
    def uniqbiner():
        with open(tempath) as o_f:
            for item in o_f.readlines():
                yield item.strip()
        print("[+] Source of  :{0} lines".format(cool.orange(finishcounter(tempath))))
