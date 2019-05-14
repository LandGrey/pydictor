#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2019 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""
from __future__ import unicode_literals


def none_encode(item):
    """default and don't encode"""
    try:
        return (item.encode('utf-8')).decode()
    except:
        return ''
