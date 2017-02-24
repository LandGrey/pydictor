#!/usr/bin/env python
# coding:utf-8
# Build a dictionary based one chunk-multiplication
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
import os
import itertools
from lib.fun import finishprinter, finishcounter, countchecker
from lib.data import get_result_store_path, get_buildtime, operator, CRLF, CHUNK_prefix, filextension


def get_chunk_dic(objflag, encodeflag, head, tail):
    countchecker(len(objflag))
    storepath = os.path.join(get_result_store_path(), "%s_%s_%s%s" %
                             (CHUNK_prefix, get_buildtime(), encodeflag, filextension))
    with open(storepath, "a") as f:
        for item in itertools.permutations(objflag, len(objflag)):
            f.write(operator.get(encodeflag)(head + "".join(item) + tail) + CRLF)
    finishprinter(finishcounter(storepath), storepath)
