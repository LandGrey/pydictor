#!/usr/bin/env python
# coding:utf-8
# num + num rule
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

from rules.BaseTrick import numjoinum


def NNrule(nums1, nums2):
    for num1 in nums1:
        for num2 in nums2:
            for _ in numjoinum(num1, num2):
                yield _
