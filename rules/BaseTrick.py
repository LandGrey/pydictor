#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2019 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

from core.EXTEND import wordsharker
from lib.data.data import pyoptions
from lib.fun.fun import unique


def simplejoin(first, second):
    ff = ss = []
    if type(first) is list:
        ff.extend(first)
    else:
        ff.append(first)
    if type(second) is list:
        ff.extend(second)
    else:
        ff.append(second)
    for f in ff:
        for s in ss:
            yield f + s


def middlejoin(firstlist, secondlist, midstr):
    for f in firstlist:
        for s in secondlist:
            yield f + midstr + s


def headjoins(firstlist, secondlist, head):
    for f in firstlist:
        for s in secondlist:
            yield head + f + s


def tailjoins(firstlist, secondlist, tail):
    for f in firstlist:
        for s in secondlist:
            yield f + s + tail


def numjoinum(num1, num2):
    yield num1 + num2
    if pyoptions.level <= 1:
        yield num1.replace('0', '') + num2
        yield num1 + num2.replace('0', '')
        yield num1.replace('0', '') + num2.replace('0', '')
    for mid in pyoptions.sedb_trick_mid:
        yield num1 + mid + num2
        yield num2 + mid + num1
        if pyoptions.level <= 1:
            yield num1.replace('0', '') + mid + num2
            yield num1 + mid + num2.replace('0', '')
            yield num1.replace('0', '') + mid + num2.replace('0', '')
            yield num2.replace('0', '') + mid + num1
            yield num2 + mid + num1.replace('0', '')
            yield num2.replace('0', '') + mid + num1.replace('0', '')

    for suf in pyoptions.sedb_trick_suf:
        yield num1 + num2 + suf
        yield num2 + num1 + suf
        if pyoptions.level <= 1:
            yield num1.replace('0', '') + num2 + suf
            yield num1 + num2.replace('0', '') + suf
            yield num1.replace('0', '') + num2.replace('0', '') + suf
            yield num2.replace('0', '') + num1 + suf
            yield num2 + num1.replace('0', '') + suf
            yield num2.replace('0', '') + num1.replace('0', '') + suf

    for pre in pyoptions.sedb_trick_pre:
        yield pre + num1 + num2
        yield pre + num2 + num1
        if pyoptions.level <= 1:
            yield pre + num1.replace('0', '') + num2
            yield pre + num1 + num2.replace('0', '')
            yield pre + num1.replace('0', '') + num2.replace('0', '')
            yield pre + num2.replace('0', '') + num1
            yield pre + num2 + num1.replace('0', '')
            yield pre + num2.replace('0', '') + num1.replace('0', '')


def strnumjoin(str1, num1):
    yield str1 + num1
    if pyoptions.level <= 1:
        yield str1 + num1.replace('0', '')
    for mid in pyoptions.sedb_trick_mid:
        yield num1 + mid + str1
        yield str1 + mid + num1
        if pyoptions.level <= 1:
            yield num1.replace('0', '') + mid + str1
            yield str1 + mid + num1.replace('0', '')

    for suf in pyoptions.sedb_trick_suf:
        yield num1 + str1 + suf
        yield str1 + num1 + suf
        if pyoptions.level <= 1:
            yield num1.replace('0', '') + str1 + suf
            yield str1 + num1.replace('0', '') + suf

    for pre in pyoptions.sedb_trick_pre:
        yield pre + num1 + str1
        yield pre + str1 + num1
        if pyoptions.level <= 1:
            yield pre + num1.replace('0', '') + str1
            yield pre + str1 + num1.replace('0', '')


def mailshaper(mail):
    shapes = []
    part = mail.partition('@')
    shapes.append(mail)
    if part[2]:
        shapes.append(part[0])
        shapes.append(part[2])
        shapes.append(part[0] + part[1])
        shapes.append(part[1] + part[2])
    return shapes


# ymd format: yyyyMMdd      dmy format: ddMMyyyy
def dateshaper(date):
    shapes = []

    # 20150806 or 06082015
    shapes.append(date)
    if pyoptions.ymd_format:
        # 150806
        shapes.append(date[2:8])
        # 201586
        shapes.append(date[0:4] + date[4].replace("0", "") + date[5:6] + date[6].replace("0", "") + date[7:8])
        if pyoptions.level <= 1:
            # 15086
            shapes.append(date[2:6] + date[6].replace("0", "") + date[7:8])
            # 15806
            shapes.append(date[2:4] + date[4].replace("0", "") + date[5:8])
            # 2015086
            shapes.append(date[0:6] + date[6].replace("0", "") + date[7:8])
            # 2015806
            shapes.append(date[0:4] + date[4].replace("0", "") + date[5:8])
            # 086
            shapes.append(date[4:6] + date[6].replace("0", "") + date[7:8])
        if pyoptions.level <= 2:
            # 806
            shapes.append(date[4].replace("0", "") + date[5:8])
            # 86
            shapes.append(date[4].replace("0", "") + date[5:6] + date[6].replace("0", "") + date[7:8])
        if pyoptions.level <= 3:
            # 2015
            shapes.append(date[0:4])
            # 0806
            shapes.append(date[4:8])
            # 1586
            shapes.append(date[2:4] + date[4].replace("0", "") + date[5:6] + date[6].replace("0", "") + date[7:8])
    else:
        # 20150806
        shapes.append(date[4:8] + date[2:4] + date[0:2])
        # 060815
        shapes.append(date[0:4] + date[6:8])
        # 682015
        shapes.append(date[0].replace("0", "") + date[1] + date[2].replace("0", "") + date[3:8])
        if pyoptions.level <= 3:
            # 0608
            shapes.append(date[0:4])
            # 2015
            shapes.append(date[4:8])
            # 6815
            shapes.append(date[0].replace("0", "") + date[1] + date[2].replace("0", "") + date[3] + date[6:8])
            # 20150608
            shapes.append(date[4:8] + date[0:4])
    return shapes


def wordshaper(word, *args):
    shapes = []
    if not args:
        shapes.extend(wordsharker(word, pyoptions.sedb_leet))
    else:
        if not type(word) is list:
            shapes.extend(wordsharker(word, pyoptions.sedb_leet))
        else:
            for w in word:
                shapes.extend(wordsharker(w, pyoptions.sedb_leet))
        for arg in args:
            if not type(arg) is list:
                shapes.extend(wordsharker(arg, pyoptions.sedb_leet))
            else:
                for a in arg:
                    shapes.extend(wordsharker(a, pyoptions.sedb_leet))
    return unique(shapes)
