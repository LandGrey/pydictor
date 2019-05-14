#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2019 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""
from __future__ import unicode_literals

try:
    from urllib import quote
except:
    from urllib.parse import quote

# note: python 2 and python3 maybe return different values because of different local encoding
# in current test_encode function, you can test '123456' will return same value and 'admin' will return differ value
#


def test_encode(item):
    """custom yourself encode method by modifying function"""
    c = chr(ord(item[0]) + len(item))
    for i in range(1, len(item)):
        c += chr(ord(item[i]) + ord(item[i - 1]))
    return quote(c)
