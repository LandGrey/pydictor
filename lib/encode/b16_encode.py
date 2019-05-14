#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2019 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""
from __future__ import unicode_literals

from base64 import b16encode


def b16_encode(item):
    """base16 encode"""
    try:
        return (b16encode(item.encode('utf-8'))).decode()
    except:
        return ''
