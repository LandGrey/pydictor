#!/usr/bin/env python
# coding:utf-8
# pydictor dictionary-handler tool: uniqbiner
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from tools.combiner import combiner_enter


def uniqbiner_enter(dirpath):
    return combiner_enter(dirpath, need_uniqifer=True)
