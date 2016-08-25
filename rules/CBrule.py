#!/usr/bin/env python
# coding:utf-8
# Build by: LandGrey 2016-08-25
#
# cname + birth rule
#
# This is a part of pydictor


def CBrule(cname, birth):
    res = []
    for cn in cname:
        for bd in birth:
            # {cname birth}
            res.append(cn + bd)
            # {cname @ birth}
            res.append(cn + '@' + bd)
            res.append(cn + '@' + bd[2:])
            res.append(cn + '@' + str(bd)[:4])
            res.append(cn + '@' + str(bd)[4:])
            res.append(cn + '@' + str(bd)[:4] + str(bd)[4:].replace('0', ''))
            # {birth @ cname}
            res.append(bd + '@' + cn)
            # {birth @ CNAMW}
            res.append(bd + '@' + str(cn).upper())
            # {cname _ birth}
            res.append(cn + '_' + bd)
            res.append(cn + '_' + bd[2:])
            res.append(cn + '_' + str(bd)[:4] + str(bd)[4:].replace('0', ''))
            # {cname birth _}
            res.append(cn + bd + '_')
            res.append(cn + bd[2:] + '_')
            res.append(cn + str(bd)[:4] + str(bd)[4:].replace('0', '') + '_')
            # {cname birth .}
            res.append(cn + bd + '.')
            res.append(cn + bd[2:] + '.')
            res.append(cn + str(bd)[:4] + str(bd)[4:].replace('0', '') + '.')
    return res