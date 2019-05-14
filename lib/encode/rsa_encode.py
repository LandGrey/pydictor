#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2019 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""
from __future__ import unicode_literals

from binascii import hexlify


def rsa_encode(item):
    """rsa algorithm and need modify code"""
    # replace your "n" and "e" hex value
    n_modulus_hex_string = 'd7190a042cd2db97ebc2ab4da366f2a7085556ed613b5a39c9fdd2bb2595d1dc'
    e_exponent_hex_string = '1001'

    if len(item) < 1:
        print("[!]exception item:[%s]" % item)
        return item
    public_modulus = int(n_modulus_hex_string, 16)
    public_exponent = int(e_exponent_hex_string, 16)
    item = int(hexlify(item[::-1].encode('utf-8')).decode(), 16)
    item = pow(item, public_exponent, public_modulus)
    return '%X' % item
