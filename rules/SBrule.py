#!/usr/bin/env python
# coding:utf-8
# Build by: LandGrey 2016-08-24
#
# sname + birth rule
#
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
            res.append(str(sn).lower() + str(bd).replace('0', '') + str(sn).upper())
            # {sname birth SNAME .}
            res.append(str(sn).lower() + bd + str(sn).upper() + '.')
            res.append(str(sn).lower() + str(bd)[2:] + str(sn).upper() + '.')
            res.append(str(sn).lower() + str(bd).replace('0', '') + str(sn).upper() + '.')
            # {sname birth SNAME _}
            res.append(str(sn).lower() + bd + str(sn).upper() + '_')
            res.append(str(sn).lower() + str(bd)[2:] + str(sn).upper() + '_')
            res.append(str(sn).lower() + str(bd).replace('0', '') + str(sn).upper() + '_')

    return res