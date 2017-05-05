#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import platform


# judge run platform
def is_Windows():
    return platform.system() == "Windows"


def is_Linux():
    return platform.system() == "Linux"


def is_Mac():
    return platform.system() == "Darwin"


# Windows 10 (v1511) Adds Support for ANSI Escape Sequences
def is_higher_win10_v1511():
    if is_Windows():
        try:
            if int(platform.version().split('.')[0]) >= 10 and int(platform.version().split('.')[-1]) >= 1511:
                return True
            else:
                return False
        except:
            return False


# python version egt 3
def py_ver_egt_3():
    if int(platform.python_version()[0]) == 3:
        return True
