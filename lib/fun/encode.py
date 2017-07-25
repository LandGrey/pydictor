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
    return (item.encode('utf-8')).decode()


def base64_encode(item):
    return (b64encode(item.encode('utf-8'))).decode()


def md5_encode(item):
    return (hashlib.md5(item.encode("utf-8"))).hexdigest()


def md5_16_encode(item):
    return hashlib.md5(item.encode("utf-8")).hexdigest()[8:-8]


def sha1_encode(item):
    return hashlib.sha1(item.encode("utf-8")).hexdigest()


def url_encode(item):
    return quote(item.encode("utf-8"))


def sha256_encode(item):
    return (hashlib.sha256(item.encode("utf-8"))).hexdigest()


def sha512_encode(item):
    return hashlib.sha512(item.encode("utf-8")).hexdigest()


# note: python 2 and python3 maybe return different values because of different local encoding
# in current test_encode function, you can test '123456' will return same value and 'admin' will return differ value
#
def test_encode(item):
    c = chr(ord(item[0]) + len(item))
    for i in range(1, len(item)):
        c += chr(ord(item[i]) + ord(item[i - 1]))
    return quote(c)
