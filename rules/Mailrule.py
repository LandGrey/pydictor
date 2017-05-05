#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

from lib.data.data import pyoptions
from rules.BaseTrick import simplejoin, middlejoin, tailjoins, headjoins, wordshaper, dateshaper, mailshaper


def Mailrule(mail, joinstrs, isstrs=True):
    for m in mail:
        if isstrs:
            for joinstr in joinstrs:
                for _ in simplejoin(wordshaper(joinstr), mailshaper(m)):
                    yield _
                for _ in simplejoin(mailshaper(m), wordshaper(joinstr)):
                    yield _

                for mid in pyoptions.sedb_trick_mid:
                    for _ in middlejoin(wordshaper(joinstr), mailshaper(m), mid):
                        yield _
                    for _ in middlejoin(mailshaper(m), wordshaper(joinstr), mid):
                        yield _
                for suf in pyoptions.sedb_trick_suf:
                    for _ in tailjoins(wordshaper(joinstr), mailshaper(m), suf):
                        yield _
                    for _ in tailjoins(mailshaper(m), wordshaper(joinstr), suf):
                        yield _
                for pre in pyoptions.sedb_trick_pre:
                    for _ in headjoins(wordshaper(joinstr), mailshaper(m), pre):
                        yield _
                    for _ in headjoins(mailshaper(m), wordshaper(joinstr), pre):
                        yield _
        else:
            for joinstr in joinstrs:
                for _ in simplejoin(dateshaper(joinstr), mailshaper(m)):
                    yield _
                for _ in simplejoin(mailshaper(m), dateshaper(joinstr)):
                    yield _

                for mid in pyoptions.sedb_trick_mid:
                    for _ in middlejoin(dateshaper(joinstr), mailshaper(m), mid):
                        yield _
                    for _ in middlejoin(mailshaper(m), dateshaper(joinstr), mid):
                        yield _
                for suf in pyoptions.sedb_trick_suf:
                    for _ in tailjoins(dateshaper(joinstr), mailshaper(m), suf):
                        yield _
                    for _ in tailjoins(mailshaper(m), dateshaper(joinstr), suf):
                        yield _
                for pre in pyoptions.sedb_trick_pre:
                    for _ in headjoins(dateshaper(joinstr), mailshaper(m), pre):
                        yield _
                    for _ in headjoins(mailshaper(m), dateshaper(joinstr), pre):
                        yield _
