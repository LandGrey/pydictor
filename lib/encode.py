#!/usr/bin/env python
# coding:utf-8
# encode & encrypt functions
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

import hashlib
from base64 import b64encode

try:
    # python 2
    from urllib import quote
except:
    # python 3
    from urllib.parse import quote


def none_encode(item):
    return item.encode('utf-8').decode()


def base64_encode(item):
    return b64encode(item.encode('utf-8')).decode()


def md5_encode(item):
    return hashlib.md5(item.encode("utf-8")).hexdigest().decode()


def md5_16_encode(item):
    return (hashlib.md5(item.encode("utf-8")).hexdigest()[8:-8]).decode()


def sha1_encode(item):
    return hashlib.sha1(item.encode("utf-8")).hexdigest().decode()


def url_encode(item):
    return quote(item.encode("utf-8")).decode()


def sha256_encode(item):
    return hashlib.sha256(item.encode("utf-8")).hexdigest().decode()


def sha512_encode(item):
    return hashlib.sha512(item.encode("utf-8")).hexdigest().decode()
