#!/usr/bin/env python
# coding:utf-8
# extend raw sensitive string to possible password
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

import os
from lib.data import get_result_store_path, buildtime, operator, CRLF, EXTEND_prefix
from lib.fun import finishprinter


def getExtendDic(rawlist, encodeflag=""):
    if rawlist == []:
        exit(CRLF + "[-] raw extend file cannot be empty")
    count = 0
    storepath = os.path.join(get_result_store_path(), "%s_%s_%s.txt" %
                             (EXTEND_prefix, buildtime, encodeflag))
    with open(storepath, 'w') as f:
        try:
            for _ in extend(rawlist):
                _ = str(_)
                if encodeflag == "":
                    f.write(_ + CRLF)
                    count += 1
                else:
                    f.write(operator.get(encodeflag)(_ + CRLF))
        except Exception, e:
            exit(CRLF + "[-] File's character encoding maybe error")
    finishprinter(count, storepath)


def extend(*args):
    extendlist = []
    for arg in args:
        for _ in arg:
            _ = str(_).rstrip('\n').rstrip('\r')
            if not _.isupper():
                extendlist.append(_)
            extendlist.append(_.upper())
            if not _.islower():
                extendlist.append(_.lower())
            _ = _.lower()
            extendlist.append(_ + _)
            extendlist.append(_[::-1])
            extendlist.append(_ + _[::-1])
            extendlist.append(_ + '0')
            extendlist.append(_ + '1')
            extendlist.append(_ + '2')
            extendlist.append(_ + '3')
            extendlist.append(_ + '4')
            extendlist.append(_ + '5')
            extendlist.append(_ + '6')
            extendlist.append(_ + '7')
            extendlist.append(_ + '8')
            extendlist.append(_ + '9')
            extendlist.append(_ + '!')
            extendlist.append(_ + '.')
            extendlist.append(_ + '?')
            extendlist.append(_ + 's')
            extendlist.append(_[0].upper() + _[1:])
            extendlist.append((_[0].upper() + _[1:])[::-1])
            extendlist.append(_[0:-1] + _[-1:].upper())
            extendlist.append((_[0:-1] + _[-1:].upper())[::-1])
            extendlist.append(_[0].upper() + _[1:] + _[0].upper() + _[1:])
            extendlist.append('1' + _)
            extendlist.append('2' + _)
            extendlist.append('3' + _)
            extendlist.append('4' + _)
            extendlist.append('5' + _)
            extendlist.append('6' + _)
            extendlist.append('7' + _)
            extendlist.append('8' + _)
            extendlist.append('9' + _)
            extendlist.append(_[0].upper() + _[1:] + '0')
            extendlist.append(_[0].upper() + _[1:] + '1')
            extendlist.append(_[0].upper() + _[1:] + '2')
            extendlist.append(_[0].upper() + _[1:] + '3')
            extendlist.append(_[0].upper() + _[1:] + '4')
            extendlist.append(_[0].upper() + _[1:] + '5')
            extendlist.append(_[0].upper() + _[1:] + '6')
            extendlist.append(_[0].upper() + _[1:] + '7')
            extendlist.append(_[0].upper() + _[1:] + '8')
            extendlist.append(_[0].upper() + _[1:] + '9')
            extendlist.append(_[0].upper() + _[1:] + '!')
            extendlist.append(_[0].upper() + _[1:] + '.')
            extendlist.append(_[0].upper() + _[1:] + '?')
            extendlist.append(_[0].upper() + _[1:] + 's')
            extendlist.append(_ + 'ed')
            extendlist.append(_ + 'ing')
            extendlist.append(_[0].upper() + _[1:] + 'ed')
            extendlist.append(_[0].upper() + _[1:] + 'ing')
            if _[-1:] in 'aeiou':
                extendlist.append(_[:-1] + 'ed')
                extendlist.append(_[:-1] + 'ing')
                extendlist.append(_[0].upper() + _[1:-1] + 'ed')
                extendlist.append(_[0].upper() + _[1:-1] + 'ing')
            extendlist.append(_ + 'abc')
            extendlist.append(_ + 'xyz')
            extendlist.append('abc' + _)
            extendlist.append(_ + '123')
            extendlist.append(_ + '789')
            extendlist.append(_ + '520')
            extendlist.append(_ + '000')
            extendlist.append(_ + '111')
            extendlist.append(_ + '666')
            extendlist.append(_ + '888')
    return extendlist