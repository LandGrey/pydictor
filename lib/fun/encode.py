#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import hashlib
from base64 import b64encode

try:
    # python 2
    from urllib import quote
except:
    # python 3
    from urllib.parse import quote


def none_encode(item):
    try:
        return (item.encode('utf-8')).decode()
    except:
        return ''


def base64_encode(item):
    try:
        return (b64encode(item.encode('utf-8'))).decode()
    except:
        return ''


def md5_encode(item):
    try:
        return (hashlib.md5(item.encode("utf-8"))).hexdigest()
    except:
        return ''


def md5_16_encode(item):
    try:
        return hashlib.md5(item.encode("utf-8")).hexdigest()[8:-8]
    except:
        return ''


def sha1_encode(item):
    try:
        return hashlib.sha1(item.encode("utf-8")).hexdigest()
    except:
        return ''


def url_encode(item):
    try:
        return quote(item.encode("utf-8"))
    except:
        return ''


def sha256_encode(item):
    try:
        return (hashlib.sha256(item.encode("utf-8"))).hexdigest()
    except:
        return ''


def sha512_encode(item):
    try:
        return hashlib.sha512(item.encode("utf-8")).hexdigest()
    except:
        return ''


# note: python 2 and python3 maybe return different values because of different local encoding
# in current test_encode function, you can test '123456' will return same value and 'admin' will return differ value
#
def test_encode(item):
    c = chr(ord(item[0]) + len(item))
    for i in range(1, len(item)):
        c += chr(ord(item[i]) + ord(item[i - 1]))
    return quote(c)
