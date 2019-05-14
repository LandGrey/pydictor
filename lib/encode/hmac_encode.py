#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2019 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""
from __future__ import unicode_literals

import hmac
import hashlib
from lib.encode.md5_encode import md5_encode


def hmac_encode(item):
    """hmac message digest algorithm"""
    key = "random_key_in_html_js_or_other_place_if_it_is_not_changed"
    item = md5_encode(item)
    return hmac.new(key.encode("utf-8"), item.encode("utf-8"), hashlib.md5).hexdigest()
