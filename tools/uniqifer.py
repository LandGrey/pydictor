#!/usr/bin/env python
# coding:utf-8
# pydictor dictionary-handler tool: uniqifer
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
import os
from lib.fun import finishcounter, cool, finishprinter
from lib.data import filextension, get_result_store_path, get_buildtime, UNIQIFER_prefix, UNIQBINER_prefix


# order preserving
def fast_uniqify(seq, idfun=None):
    if idfun is None:
        def idfun(x): return x
    seen = {}
    results = []
    for item in seq:
        marker = idfun(item)
        if marker in seen:
            continue
        seen[marker] = 1
        results.append(item)
    return results


def uniqifer_enter(original_file_path, from_combiner=False):
    prefix = UNIQIFER_prefix
    if from_combiner:
        prefix = UNIQBINER_prefix
    storepath = os.path.join(get_result_store_path(), "%s_%s%s" % (prefix, get_buildtime(), filextension))
    with open(original_file_path) as o_f:
        with open(storepath, "a") as s_f:
            for _ in fast_uniqify(o_f.readlines()):
                s_f.write(_)
    print("[+] Source of  :{0} lines".format(cool.orange(finishcounter(original_file_path))))
    finishprinter(finishcounter(storepath), storepath)
