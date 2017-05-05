#!/usr/bin/env python
# coding:utf-8
# sname + birth rule
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

from rules.SDrule import SDrule
from lib.data.data import pyoptions


def SB(sname, birth):
    for _ in SDrule(sname, birth):
        yield _

    for sn in sname:
        for bd in birth:
            # {sname birth SNAME}
            yield sn.lower() + bd + sn.upper()
            yield sn.lower() + bd[2:] + sn.upper()
            yield sn.lower() + bd[:4] + bd[4:].replace('0', '') + sn.upper()
            for suf in pyoptions.sedb_trick_suf:
                yield sn.lower() + bd + sn.upper() + suf
                yield sn.lower() + bd[2:] + sn.upper() + suf
                yield sn.lower() + bd[:4] + bd[4:].replace('0', '') + sn.upper() + suf
    # You can continue to add new and useful rules
    #
