#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

from tools.combiner import combiner_enter


def uniqbiner_enter(dirpath):
    return combiner_enter(dirpath, need_uniqifer=True)
