#!/usr/bin/env python
# coding:utf-8
# strings + strings rule
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

from lib.data.data import pyoptions
from rules.BaseTrick import simplejoin, middlejoin, tailjoins, headjoins, wordshaper


def SSrule(strs1, strs2):
    for str1 in strs1:
        for str2 in strs2:
            for _ in simplejoin(str1, str2):
                yield _
            for _ in simplejoin(str2, str1):
                yield _
            for mid in pyoptions.sedb_trick_mid:
                for _ in middlejoin(wordshaper(str1), wordshaper(str2), mid):
                    yield _
                for _ in middlejoin(wordshaper(str2), wordshaper(str1), mid):
                    yield _
            for suf in pyoptions.sedb_trick_suf:
                for _ in tailjoins(wordshaper(str1), wordshaper(str2), suf):
                    yield _
                for _ in tailjoins(wordshaper(str2), wordshaper(str1), suf):
                    yield _
            for pre in pyoptions.sedb_trick_pre:
                for _ in headjoins(wordshaper(str1), wordshaper(str2), pre):
                    yield _
                for _ in headjoins(wordshaper(str2), wordshaper(str1), pre):
                        yield _
