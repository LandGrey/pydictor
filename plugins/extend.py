#!/usr/bin/env python
# coding:utf-8
# extend raw sensitive string to possible password
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
import os
from lib.data import get_result_store_path, get_buildtime, operator, CRLF, EXTEND_prefix, filextension
from lib.fun import finishprinter, finishcounter, cool


def getExtendDic(rawlist, encodeflag=""):
    if rawlist == []:
        exit(CRLF + cool.red("[-] raw extend file cannot be empty"))
    storepath = os.path.join(get_result_store_path(), "%s_%s_%s%s" %
                             (EXTEND_prefix, get_buildtime(), encodeflag, filextension))
    with open(storepath, 'w') as f:
        try:
            for _ in extend(rawlist):
                _ = str(_)
                if encodeflag == "":
                    f.write(_ + CRLF)
                else:
                    f.write(operator.get(encodeflag)(_ + CRLF))
        except:
            exit(CRLF + cool.red("[-] File's character encoding maybe error"))
    finishprinter(finishcounter(storepath), storepath)


def extend(*args):
    for arg in args:
        for _ in arg:
            _ = str(_).rstrip('\n').rstrip('\r')
            if not _.isupper():
                yield _
            yield _.upper()
            if not _.islower():
                yield _.lower()
            _ = _.lower()
            yield _ + _
            yield _[::-1]
            yield _ + _[::-1]
            yield _ + '0'
            yield _ + '1'
            yield _ + '2'
            yield _ + '3'
            yield _ + '4'
            yield _ + '5'
            yield _ + '6'
            yield _ + '7'
            yield _ + '8'
            yield _ + '9'
            yield _ + '!'
            yield _ + '.'
            yield _ + '?'
            yield _ + 's'
            yield _[0].upper() + _[1:]
            yield (_[0].upper() + _[1:])[::-1]
            yield _[0:-1] + _[-1:].upper()
            yield (_[0:-1] + _[-1:].upper())[::-1]
            yield _[0].upper() + _[1:] + _[0].upper() + _[1:]
            yield '1' + _
            yield '2' + _
            yield '3' + _
            yield '4' + _
            yield '5' + _
            yield '6' + _
            yield '7' + _
            yield '8' + _
            yield '9' + _
            yield _[0].upper() + _[1:] + '0'
            yield _[0].upper() + _[1:] + '1'
            yield _[0].upper() + _[1:] + '2'
            yield _[0].upper() + _[1:] + '3'
            yield _[0].upper() + _[1:] + '4'
            yield _[0].upper() + _[1:] + '5'
            yield _[0].upper() + _[1:] + '6'
            yield _[0].upper() + _[1:] + '7'
            yield _[0].upper() + _[1:] + '8'
            yield _[0].upper() + _[1:] + '9'
            yield _[0].upper() + _[1:] + '!'
            yield _[0].upper() + _[1:] + '.'
            yield _[0].upper() + _[1:] + '?'
            yield _[0].upper() + _[1:] + 's'
            yield _ + 'ed'
            yield _ + 'ing'
            yield _[0].upper() + _[1:] + 'ed'
            yield _[0].upper() + _[1:] + 'ing'
            if _[-1:] in 'aeiou':
                yield _[:-1] + 'ed'
                yield _[:-1] + 'ing'
                yield _[0].upper() + _[1:-1] + 'ed'
                yield _[0].upper() + _[1:-1] + 'ing'
            yield _ + 'abc'
            yield _ + 'xyz'
            yield 'abc' + _
            yield _ + '123'
            yield _ + '789'
            yield _ + '520'
            yield _ + '000'
            yield _ + '111'
            yield _ + '666'
            yield _ + '888'
