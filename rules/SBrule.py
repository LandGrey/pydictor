#!/usr/bin/env python
# coding:utf-8
# sname + birth rule
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
from rules.CBrule import CBrule


def SBrule(sname, birth):
    for _ in CBrule(sname, birth):
        yield _
    for sn in sname:
        for bd in birth:
            # {sname birth SNAME}
            yield sn.lower() + bd + sn.upper()
            yield sn.lower() + bd[2:] + sn.upper()
            yield sn.lower() + bd[:4] + bd[4:].replace('0', '') + sn.upper()
            # {sname birth SNAME .}
            yield sn.lower() + bd + sn.upper() + '.'
            yield sn.lower() + bd[2:] + sn.upper() + '.'
            yield sn.lower() + bd[:4] + bd[4:].replace('0', '') + sn.upper() + '.'
            # {sname birth SNAME _}
            yield sn.lower() + bd + sn.upper() + '_'
            yield sn.lower() + bd[2:] + sn.upper() + '_'
            yield sn.lower() + bd[:4] + bd[4:].replace('0', '') + sn.upper() + '_'
