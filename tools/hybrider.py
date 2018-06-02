#!/usr/bin/env python
# coding:utf-8
# author: LandGrey
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""
from __future__ import unicode_literals

import os
import itertools
import traceback
from lib.data.data import pyoptions
from lib.fun.fun import finishprinter, cool, finalsavepath, fun_name


def hybrider_magic(*args):
    """[file1] [file2] ..."""
    args = list(args[0])

    filepaths = []
    hybrid_list = []
    if len(args) >= 2:
        for count in range(1, len(args)):
            directory = os.path.abspath(args[count])
            if not os.path.isfile(os.path.abspath(directory)):
                exit(pyoptions.CRLF + cool.red("[-] file: {} don't exists".format(directory)))
            else:
                filepaths.append(directory)
    else:
        exit(pyoptions.CRLF + cool.fuchsia("[!] Usage: {} {}".format(args[0], pyoptions.tools_info.get(args[0]))))
    storepath = finalsavepath(fun_name())

    try:
        for fp in filepaths:
            tmp = set()
            with open(fp, "r") as f:
                for line in f.readlines():
                    tmp.add(line.strip())
            hybrid_list.append(tmp)

        with open(storepath, "a") as f:
            for item in itertools.product(*hybrid_list):
                f.write(pyoptions.operator.get(pyoptions.encode)(pyoptions.head + "".join(item) + pyoptions.tail) +
                        pyoptions.CRLF)
        finishprinter(storepath)

    except Exception as ex:
        print(pyoptions.CRLF + cool.red("[-] Hybrid files failed, Looking: "))
        exit(pyoptions.CRLF + traceback.print_exc())
