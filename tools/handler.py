#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import os
from lib.data.data import paths, pystrs, pyoptions
from lib.fun.filter import filterforfun
from lib.fun.fun import finishprinter, finishcounter, mybuildtime, cool


def get_handler_dic(path):
    if not os.path.isfile(path):
        exit(cool.red("[-] File don't exits" + pyoptions.CRLF))
    storepath = os.path.join(paths.results_path, "%s_%s%s"
                             % (pystrs.HANDLER_prefix, mybuildtime(), pyoptions.filextension))
    handles = []
    with open(path, 'r') as f:
        for item in f.readlines():
            handles.append(item.strip())

    with open(storepath, 'a') as save:
        for item in handles:
            item = filterforfun("".join(item), head=pyoptions.head, tail=pyoptions.tail,
                                lenght_is_filter=pyoptions.args_pick,
                                minlen=pyoptions.minlen, maxlen=pyoptions.maxlen,
                                regex_is_filter=True, regex=pyoptions.filter_regex,
                                encode_is_filter=True, encode=pyoptions.encode,
                                occur_is_filter=True,
                                letter_occur=pyoptions.letter_occur,
                                digital_occur=pyoptions.digital_occur,
                                special_occur=pyoptions.special_occur,
                                types_is_filter=True,
                                letter_types=pyoptions.letter_types,
                                digital_types=pyoptions.digital_types,
                                special_types=pyoptions.special_types,
                                )
            if item:
                save.write(item + pyoptions.CRLF)
    finishprinter(finishcounter(storepath), storepath)
