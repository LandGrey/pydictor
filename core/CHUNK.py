#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import itertools
from lib.fun.filter import filterforfun
from lib.data.data import paths, pystrs, pyoptions
from lib.fun.fun import finishprinter, finishcounter, countchecker, mybuildtime, finalsavepath


def get_chunk_dic(objflag):
    countchecker(len(objflag))
    storepath = finalsavepath(paths.results_path, pystrs.CHUNK_prefix, mybuildtime(), pyoptions.filextension, paths.results_file_name)
    with open(storepath, "a") as f:
        for item in itertools.permutations(objflag):
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
                f.write(item + pyoptions.CRLF)
    finishprinter(finishcounter(storepath), storepath)
