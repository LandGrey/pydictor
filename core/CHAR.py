#!/usr/bin/env python
# coding:utf-8
# Build a dictionary based on custom char
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from core.BASE import get_base_dic


def get_char_dic(minlength, maxlength, customchar, encode, head, tail):
    return get_base_dic(minlength, maxlength, customchar, encode, head, tail, need_char_dic=True)
