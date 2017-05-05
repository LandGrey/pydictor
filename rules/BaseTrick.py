#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

from lib.fun.fun import unique
from lib.data.data import pyoptions
from lib.fun.leetmode import leet_mode_magic


def simplejoin(firstlist, secondlist):
    if type(firstlist) is list and type(secondlist) is list:
        for f in firstlist:
            for s in secondlist:
                yield f + s
    elif type(firstlist) is list and type(secondlist) is not list:
        for f in firstlist:
            yield f + secondlist
    elif type(firstlist) is not list and type(secondlist) is list:
            for s in secondlist:
                yield firstlist + s
    else:
        yield firstlist + secondlist


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
    shapes.append(date[2:])
    shapes.append(date[4:])
    shapes.append(date.replace('0', ''))
    shapes.append(date[2:].replace('0', ''))
    shapes.append(date[4:].replace('0', ''))
    return shapes


def wordshaper(word, *args):
    shapes = []
    if not args:
        shapes.append(word)
        shapes.append(word.lower())
        shapes.append(word.upper())
        shapes.append(word.capitalize())
        if pyoptions.sedb_leet:
            shapes.append(leet_mode_magic(word))
    else:
        if not type(word) is list:
            shapes.append(word)
            shapes.append(word.lower())
            shapes.append(word.upper())
            shapes.append(word.capitalize())
            if pyoptions.sedb_leet:
                shapes.append(leet_mode_magic(word))
        else:
            for w in word:
                shapes.append(w)
                shapes.append(w.lower())
                shapes.append(w.upper())
                shapes.append(w.capitalize())
                if pyoptions.sedb_leet:
                    shapes.append(leet_mode_magic(w))
        for arg in args:
            if not type(arg) is list:
                shapes.append(arg)
                shapes.append(arg.lower())
                shapes.append(arg.upper())
                shapes.append(arg.capitalize())
                if pyoptions.sedb_leet:
                    shapes.append(leet_mode_magic(arg))
            else:
                for a in arg:
                    shapes.append(a)
                    shapes.append(a.lower())
                    shapes.append(a.upper())
                    shapes.append(a.capitalize())
                    if pyoptions.sedb_leet:
                        shapes.append(leet_mode_magic(a))
    return unique(shapes)
