#!/usr/bin/env python
# coding:utf-8
# Single item rule
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""


def SingleRule(cname, ename, sname, birth, usedpwd, phone, uphone, hphone, email, postcode, nickname, idcard, jobnum, otherdate, usedchar):
    for cn in cname:
        yield cn
        yield cn.upper()
        yield cn[:1].upper() + cn[1:].lower()
    for en in ename:
        yield en
        yield en.upper()
        yield en[:1].upper() + en[1:].lower()
    for sn in sname:
        yield sn.lower()
        yield sn.upper()
        # {sname _ SNAME}
        yield sn.lower() + '_' + sn.upper()
        # {sname @ SNAME}
        yield sn.lower() + '@' + sn.upper()
        # {sname SNAME .}
        yield sn.lower() + sn.upper() + '.'
    for bd in birth:
        yield bd
        yield bd[2:]
        yield bd[:4] + bd[4:].replace('0', '')
    for upass in usedpwd:
        yield upass
        # {upass .}
        yield upass + '.'
        # {upass _}
        yield upass + '_'
        # {_ upass}
        yield '_' + upass
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
    for nn in nickname:
        yield nn
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
    for uc in usedchar:
        yield uc
