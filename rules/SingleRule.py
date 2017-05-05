#!/usr/bin/env python
# coding:utf-8
# Single item rule
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

from rules.BaseTrick import wordshaper


def SingleRule(cname, ename, sname, birth, usedpwd, phone, uphone, hphone, email, postcode, nickname, idcard, jobnum,
               otherdate, usedchar):
    for _ in wordshaper(cname, ename, sname, usedpwd, email, nickname, usedchar):
        yield _
    for bd in birth:
        yield bd
        yield bd[2:]
        yield bd[:4] + bd[4:].replace('0', '')
    for ph in phone:
        yield ph
    for uph in uphone:
        yield uph
    for hp in hphone:
        yield hp
    for em in email:
        yield em
        # {@xxx.xxx}
        yield '@' + em.split('@')[1]
    for pc in postcode:
        yield pc
    for ic in idcard:
        yield ic[:6]
        yield ic[-4:]
        yield ic[-6:]
        yield ic[-8:]
    for jn in jobnum:
        yield jn
    for od in otherdate:
        yield od
        yield od[2:]
        yield od[:4] + od[4:].replace('0', '')
    # You can continue to add new and useful rules
    #
