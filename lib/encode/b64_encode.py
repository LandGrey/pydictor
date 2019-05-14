#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2019 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""
from __future__ import unicode_literals

from base64 import b64encode


def b64_encode(item):
    """base64 encode"""
    try:
        return (b64encode(item.encode('utf-8'))).decode()
    except:
        return ''
