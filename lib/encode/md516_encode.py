#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2019 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""
from __future__ import unicode_literals

import hashlib


def md516_encode(item):
    """md5 message digest algorithm output 16 char"""
    try:
        return hashlib.md5(item.encode("utf-8")).hexdigest()[8:-8]
    except:
        return ''
