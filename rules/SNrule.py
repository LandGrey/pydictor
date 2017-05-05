#!/usr/bin/env python
# coding:utf-8
# string + num rule
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

from rules.BaseTrick import strnumjoin


def SNrule(strs, nums):
    for s in strs:
        for n in nums:
            for _ in strnumjoin(s, n):
                yield _
