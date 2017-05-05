#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from core.BASE import get_base_dic


def get_char_dic(customchar):
    return get_base_dic(customchar, need_char_dic=True)
