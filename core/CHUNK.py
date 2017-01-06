#!/usr/bin/env python
# coding:utf-8
# build a chunk multiplication dictionary 
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

import os
import itertools
from lib.data import get_result_store_path, buildtime, operator, CRLF, CHUNK_prefix
from lib.fun import finishprinter
from lib.fun import countchecker


# create the dictionary files
def get_chunk_dic(objflag, encodeflag, head, tail):
    countchecker(len(objflag))
    count = 0
    storepath = os.path.join(get_result_store_path(), "%s_%s_%s.txt" %
                             (CHUNK_prefix, buildtime, encodeflag))
    with open(storepath, "w") as f:
        for item in itertools.permutations(objflag, len(objflag)):
            if encodeflag == "":
                f.write(head + "".join(item) + tail + CRLF)
                count += 1
            else:
                f.write(operator.get(encodeflag)(head + "".join(item) + tail) + CRLF)
                count += 1
    finishprinter(count, storepath)
