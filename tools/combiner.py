#!/usr/bin/env python
# coding:utf-8
# author: LandGrey
"""
Copyright (c) 2016-2021 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""
from __future__ import unicode_literals

import os
import codecs
import mimetypes
import traceback
from lib.data.data import pyoptions
from lib.fun.fun import finishprinter, cool, finalsavepath, fun_name


def combiner_magic(*args):
    """[dir]"""
    args = list(args[0])

    if len(args) == 2:
        directory = os.path.abspath(args[1])
        if not os.path.isdir(os.path.abspath(directory)):
            exit(pyoptions.CRLF + cool.red("[-] path: {} don't exists".format(directory)))
    else:
        exit(pyoptions.CRLF + cool.fuchsia("[!] Usage: {} {}".format(args[0], pyoptions.tools_info.get(args[0]))))
    storepath = finalsavepath(fun_name())

    filepaths = []
    combine_list = []
    for rootpath, subdirsname, filenames in os.walk(directory):
        filepaths.extend([os.path.abspath(os.path.join(rootpath, _)) for _ in filenames])
    if len(filepaths) > 0:
        for _ in filepaths:
            if mimetypes.guess_type(_)[0] == 'text/plain':
                combine_list.append(_)
    try:
        with codecs.open(storepath, 'a', encoding="utf-8") as f:
            for onefile in combine_list:
                with codecs.open(onefile, 'r', encoding="utf-8") as tf:
                    f.write(tf.read())
        finishprinter(storepath)

    except Exception as ex:
        print(pyoptions.CRLF + cool.red("[-] Combine file failed, Looking: "))
        traceback.print_exc()
