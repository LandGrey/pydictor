#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import os
import itertools
from lib.data.data import paths, pystrs, pyoptions
from lib.fun.fun import finishprinter, finishcounter, countchecker, mybuildtime


def get_chunk_dic(objflag):
    countchecker(len(objflag))
    storepath = os.path.join(paths.results_path, "%s_%s_%s" %
                             (pystrs.CHUNK_prefix, mybuildtime(), pyoptions.filextension))
    with open(storepath, "a") as f:
        for item in itertools.permutations(objflag, len(objflag)):
            f.write(pyoptions.operator.get(pyoptions.encode)(pyoptions.head +
                                                             "".join(item) + pyoptions.tail) + pyoptions.CRLF)
    finishprinter(finishcounter(storepath), storepath)
