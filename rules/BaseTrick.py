#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
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
    yield num1.replace('0', '') + num2
    yield num1 + num2.replace('0', '')
    yield num1.replace('0', '') + num2.replace('0', '')
    for mid in pyoptions.sedb_trick_mid:
        yield num1 + mid + num2
        yield num1.replace('0', '') + mid + num2
        yield num1 + mid + num2.replace('0', '')
        yield num1.replace('0', '') + mid + num2.replace('0', '')
        yield num2 + mid + num1
        yield num2.replace('0', '') + mid + num1
        yield num2 + mid + num1.replace('0', '')
        yield num2.replace('0', '') + mid + num1.replace('0', '')

    for suf in pyoptions.sedb_trick_suf:
        yield num1 + num2 + suf
        yield num1.replace('0', '') + num2 + suf
        yield num1 + num2.replace('0', '') + suf
        yield num1.replace('0', '') + num2.replace('0', '') + suf
        yield num2 + num1 + suf
        yield num2.replace('0', '') + num1 + suf
        yield num2 + num1.replace('0', '') + suf
        yield num2.replace('0', '') + num1.replace('0', '') + suf

    for pre in pyoptions.sedb_trick_pre:
        yield pre + num1 + num2
        yield pre + num1.replace('0', '') + num2
        yield pre + num1 + num2.replace('0', '')
        yield pre + num1.replace('0', '') + num2.replace('0', '')
        yield pre + num2 + num1
        yield pre + num2.replace('0', '') + num1
        yield pre + num2 + num1.replace('0', '')
        yield pre + num2.replace('0', '') + num1.replace('0', '')


def strnumjoin(str1, num1):
    yield str1 + num1
    yield str1 + num1.replace('0', '')
    for mid in pyoptions.sedb_trick_mid:
        yield num1 + mid + str1
        yield num1.replace('0', '') + mid + str1
        yield str1 + mid + num1
        yield str1 + mid + num1.replace('0', '')

    for suf in pyoptions.sedb_trick_suf:
        yield num1 + str1 + suf
        yield num1.replace('0', '') + str1 + suf
        yield str1 + num1 + suf
        yield str1 + num1.replace('0', '') + suf

    for pre in pyoptions.sedb_trick_pre:
        yield pre + num1 + str1
        yield pre + num1.replace('0', '') + str1
        yield pre + str1 + num1
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


# date format: yyyyMMdd
def dateshaper(date):
    shapes = []
    shapes.append(date)
    shapes.append(date[4:] + date[:4])
    shapes.append(date[2:])
    shapes.append(date[4:] + date[2:4])
    shapes.append(date[:4])
    shapes.append(date[4:])
    shapes.append(date[:4] + date[4:].replace('0', ''))
    shapes.append(date[4:].replace('0', ''))
    shapes.append(date[2:4] + date[4:].replace('0', ''))
    shapes.append(date[4:].replace('0', '') + date[2:4])
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
