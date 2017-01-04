#!/usr/bin/env python
# coding:utf-8
# sname + birth rule
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from CBrule import CBrule


def SBrule(sname, birth):
    res = CBrule(sname, birth)
    # You can continue to add new and useful rules
    #
    for sn in sname:
        for bd in birth:
            # {sname birth SNAME}
            res.append(str(sn).lower() + bd +str(sn).upper())
            res.append(str(sn).lower() + str(bd)[2:] + str(sn).upper())
            res.append(str(sn).lower() + str(bd)[:4] + str(bd)[4:].replace('0', '') + str(sn).upper())
            # {sname birth SNAME .}
            res.append(str(sn).lower() + bd + str(sn).upper() + '.')
            res.append(str(sn).lower() + str(bd)[2:] + str(sn).upper() + '.')
            res.append(str(sn).lower() + str(bd)[:4] + str(bd)[4:].replace('0', '') + str(sn).upper() + '.')
            # {sname birth SNAME _}
            res.append(str(sn).lower() + bd + str(sn).upper() + '_')
            res.append(str(sn).lower() + str(bd)[2:] + str(sn).upper() + '_')
            res.append(str(sn).lower() + str(bd)[:4] + str(bd)[4:].replace('0', '') + str(sn).upper() + '_')

    return res