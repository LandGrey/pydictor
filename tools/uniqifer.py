#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

from lib.fun.filter import filterforfun
from lib.data.data import paths, pystrs, pyoptions
from lib.fun.fun import cool, finishcounter, finishprinter, unique, mybuildtime, finalsavepath


def uniqifer_enter(original_file_path, from_combiner=False):
    dict_prefix = pystrs.UNIQIFER_prefix
    if from_combiner:
        dict_prefix = pystrs.UNIQBINER_prefix
    storepath = finalsavepath(paths.results_path, dict_prefix, mybuildtime(), pyoptions.filextension,
                              paths.results_file_name)
    with open(original_file_path) as o_f:
        with open(storepath, "a") as s_f:
            for item in unique(o_f.readlines()):
                item = filterforfun(item.strip(), head=pyoptions.head, tail=pyoptions.tail,
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
                    s_f.write(item + pyoptions.CRLF)
    print("[+] Source of  :{0} lines".format(cool.orange(finishcounter(original_file_path))))
    finishprinter(finishcounter(storepath), storepath)
