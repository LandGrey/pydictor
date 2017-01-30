#!/usr/bin/env python
# coding:utf-8
# cname + birth rule
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""


def CBrule(cname, birth):
    for cn in cname:
        for bd in birth:
            # {cname birth}
            yield cn + bd
            yield cn + bd.replace('0', '')
            yield cn + bd[2:]
            yield cn + bd[2:].replace('0', '')
            yield cn[:1].upper() + cn[1:].lower() + bd
            yield cn[:1].upper() + cn[1:].lower() + bd.replace('0', '')
            yield cn[:1].upper() + cn[1:].lower() + bd[2:]
            yield cn[:1].upper() + cn[1:].lower() + bd[2:].replace('0', '')
            # {cname @ birth}
            yield cn + '@' + bd
            yield cn[:1].upper() + cn[1:].lower() + '@' + bd
            yield cn + '@' + bd[2:]
            yield cn[:1].upper() + cn[1:].lower() + '@' + bd[2:]
            yield cn + '@' + bd[:4]
            yield cn[:1].upper() + cn[1:].lower() + '@' + bd[:4]
            yield cn + '@' + bd[4:]
            yield cn[:1].upper() + cn[1:].lower() + '@' + bd[4:]
            yield cn + '@' + bd[:4] + bd[4:].replace('0', '')
            yield cn[:1].upper() + cn[1:].lower() + '@' + bd[:4] + bd[4:].replace('0', '')
            # {birth @ cname}
            yield bd + '@' + cn
            yield bd.replace('0', '') + '@' + cn
            yield bd + '@' + cn[:1].upper() + cn[1:].lower()
            # {birth @ CNAMW}
            yield bd + '@' + cn.upper()
            yield bd.replace('0', '') + '@' + cn.upper()
            # {cname _ birth}
            yield cn + '_' + bd
            yield cn[:1].upper() + cn[1:].lower() + '_' + bd
            yield cn + '_' + bd[2:]
            yield cn[:1].upper() + cn[1:].lower() + '_' + bd[2:]
            yield cn + '_' + bd[:4] + bd[4:].replace('0', '')
            yield cn[:1].upper() + cn[1:].lower() + '_' + bd[:4] + bd[4:].replace('0', '')
            # {cname birth _}
            yield cn + bd + '_'
            yield cn[:1].upper() + cn[1:].lower() + bd + '_'
            yield cn + bd[2:] + '_'
            yield cn[:1].upper() + cn[1:].lower() + bd[2:] + '_'
            yield cn + bd[:4] + bd[4:].replace('0', '') + '_'
            yield cn[:1].upper() + cn[1:].lower() + bd[:4] + bd[4:].replace('0', '') + '_'
            # {cname birth .}
            yield cn + bd + '.'
            yield cn[:1].upper() + cn[1:].lower() + bd + '.'
            yield cn + bd[2:] + '.'
            yield cn[:1].upper() + cn[1:].lower() + bd[2:] + '.'
            yield cn + bd[:4] + bd[4:].replace('0', '') + '.'
            yield cn[:1].upper() + cn[1:].lower() + bd[:4] + bd[4:].replace('0', '') + '.'
