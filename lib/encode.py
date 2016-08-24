#!/usr/bin/env python
# coding:utf-8
# Build by LandGrey 2016-06-08
#
# encode & encrypt the strings
#

from urllib import quote
from base64 import b64encode
import hashlib


def base64_encode(item):
    return b64encode(item)


def md5_encode(item):
    return hashlib.md5(item).hexdigest()


def md5_16_encode(item):
    return hashlib.md5(item).hexdigest()[8:-8]


def sha1_encode(item):
    return hashlib.sha1(item).hexdigest()


def url_encode(item):
    return quote(item)


def sha256_encode(item):
    return hashlib.sha256(item).hexdigest()


def sha512_encode(item):
    return hashlib.sha512(item).hexdigest()

