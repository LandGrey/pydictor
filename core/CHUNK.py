#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import itertools
from lib.fun.decorator import magic
from lib.fun.fun import countchecker


def get_chunk_dic(objflag):
    countchecker(len(objflag))

    @magic
    def chunk():
        for item in itertools.permutations(objflag):
            yield "".join(item)
