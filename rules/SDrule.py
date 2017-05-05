#!/usr/bin/env python
# coding:utf-8
# string + date rule
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

from rules.BaseTrick import *
from lib.data.data import pyoptions


def SDrule(cname, birth):
    for cn in cname:
        for bd in birth:
            for _ in simplejoin(wordshaper(cn), dateshaper(bd)):
                yield _
            for _ in simplejoin(dateshaper(bd), wordshaper(cn)):
                yield _
            for mid in pyoptions.sedb_trick_mid:
                for _ in middlejoin(wordshaper(cn), dateshaper(bd), mid):
                    yield _
                for _ in middlejoin(dateshaper(bd), wordshaper(cn), mid):
                    yield _
            for suf in pyoptions.sedb_trick_suf:
                for _ in tailjoins(wordshaper(cn), dateshaper(bd), suf):
                    yield _
                for _ in tailjoins(dateshaper(bd), wordshaper(cn), suf):
                    yield _
            for pre in pyoptions.sedb_trick_pre:
                for _ in headjoins(wordshaper(cn), dateshaper(bd), pre):
                    yield _
                for _ in headjoins(dateshaper(bd), wordshaper(cn), pre):
                    yield _
