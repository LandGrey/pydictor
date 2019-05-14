#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2019 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""
from __future__ import unicode_literals

try:
    # python 2
    from urllib import quote
except:
    # python 3
    from urllib.parse import quote


def url_encode(item):
    """url encode"""
    try:
        return quote(item.encode("utf-8"))
    except:
        return ''
