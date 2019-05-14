#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2019 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""
from __future__ import unicode_literals

from base64 import b32encode


def b32_encode(item):
    """base32 encode"""
    try:
        return (b32encode(item.encode('utf-8'))).decode()
    except:
        return ''
