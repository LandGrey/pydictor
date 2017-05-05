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
from lib.fun.fun import cool, finishcounter, finishprinter, unique, mybuildtime


def uniqifer_enter(original_file_path, from_combiner=False):
    prefix = pystrs.UNIQIFER_prefix
    if from_combiner:
        prefix = pystrs.UNIQBINER_prefix
    storepath = os.path.join(paths.results_path, "%s_%s%s" % (prefix, mybuildtime(), pyoptions.filextension))
    with open(original_file_path) as o_f:
        with open(storepath, "a") as s_f:
            for _ in unique(o_f.readlines()):
                s_f.write(_)
    print("[+] Source of  :{0} lines".format(cool.orange(finishcounter(original_file_path))))
    finishprinter(finishcounter(storepath), storepath)
