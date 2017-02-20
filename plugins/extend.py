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
            yield _ + _.upper()
            yield _.upper() + _.upper()

            yield _[::-1]
            yield _ + _[::-1]

            yield _ + '0'
            yield _.upper() + '0'
            yield _[0].upper() + _[1:] + '0'

            yield _ + '1'
            yield _.upper() + '1'
            yield _[0].upper() + _[1:] + '1'

            yield _ + '2'
            yield _.upper() + '2'
            yield _[0].upper() + _[1:] + '2'

            yield _ + '3'
            yield _.upper() + '3'
            yield _[0].upper() + _[1:] + '3'

            yield _ + '4'
            yield _.upper() + '4'
            yield _[0].upper() + _[1:] + '4'

            yield _ + '5'
            yield _.upper() + '5'
            yield _[0].upper() + _[1:] + '5'

            yield _ + '6'
            yield _.upper() + '6'
            yield _[0].upper() + _[1:] + '6'

            yield _ + '7'
            yield _.upper() + '7'
            yield _[0].upper() + _[1:] + '7'

            yield _ + '8'
            yield _.upper() + '8'
            yield _[0].upper() + _[1:] + '8'

            yield _ + '9'
            yield _.upper() + '9'
            yield _[0].upper() + _[1:] + '9'

            yield _ + '!'
            yield _.upper() + '!'
            yield _[0].upper() + _[1:] + '!'

            yield _ + '.'
            yield _.upper() + '.'
            yield _[0].upper() + _[1:] + '.'

            yield _ + '?'
            yield _.upper() + '?'
            yield _[0].upper() + _[1:] + '?'

            yield _ + 's'
            yield _.upper() + 's'
            yield _[0].upper() + _[1:] + 's'

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

            yield 'qq' + _
            yield 'qq:' + _
            yield 'QQ' + _
            yield 'QQ:' + _
            yield _ + 'qq'

            yield _ + '..'

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
            yield _ + 'ABC'
            yield _.upper() + 'ABC'
            yield _[0].upper() + _[1:] + 'abc'
            yield _[0].upper() + _[1:] + 'ABC'

            yield 'abc' + _
            yield 'Abc' + _
            yield 'abc' + _.upper()

            yield _ + 'xyz'
            yield _.upper() + 'xyz'
            yield _[0].upper() + _[1:] + 'xyz'

            yield _ + 'XYZ'
            yield _.upper() + 'XYZ'
            yield _[0].upper() + _[1:] + 'XYZ'

            yield _ + '123'
            yield _.upper() + '123'
            yield _[0].upper() + _[1:] + '123'

            yield _ + '789'
            yield _.upper() + '789'
            yield _[0].upper() + _[1:] + '789'

            yield _ + '520'
            yield _.upper() + '520'
            yield _[0].upper() + _[1:] + '520'

            yield _ + '000'
            yield _.upper() + '000'
            yield _[0].upper() + _[1:] + '000'

            yield _ + '111'
            yield _.upper() + '111'
            yield _[0].upper() + _[1:] + '111'

            yield _ + '666'
            yield _.upper() + '666'
            yield _[0].upper() + _[1:] + '666'

            yield _ + '888'
            yield _.upper() + '888'
            yield _[0].upper() + _[1:] + '888'

            yield _ + '...'
            yield _[0].upper() + _[1:] + '...'

            yield _ + '!@#'
            yield _[0].upper() + _[1:] + '!@#'

            yield 'qaz' + _
            yield 'qaz' + _.upper()
            yield 'qqq' + _

            yield 'get' + _
            yield 'got' + _
            yield 'win' + _
            yield 'cao' + _
            yield 'fuck' + _
            yield 'Fuck' + _
            yield 'FUCK' + _
            yield 'fuck' + _.upper()
            yield 'fucker' + _
            yield 'fucked' + _
            yield 'Fucked' + _
            yield _ + 'fuck'
            yield _ + 'FUCK'
            yield _ + 'fucker'

            yield _ + 'qwer'
            yield _.upper() + 'qwer'
            yield _[0].upper() + _[1:] + 'qwer'
            yield _ + 'QWER'

            yield 'test' + _
            yield 'Test' + _
            yield 'test_' + _
            yield 'tester' + _
            yield 'Tester' + _
            yield _ + '_test'
            yield _ + '_tester'

            yield 'qwer' + _
            yield 'qwer' + _.upper()
            yield 'qwer_' + _
            yield 'qwer_' + _.upper()

            yield 'QWER' + _
            yield 'qwert' + _
            yield 'qwert' + _.upper()
            yield 'QWERT' + _
            yield 'qwerty' + _
            yield 'qwerty' + _.upper()
            yield 'qazxsw' + _
            yield 'qweasd' + _
            yield 'qwert' + _

            yield _ + '@123'
            yield _.upper() + '@123'
            yield _[0].upper() + _[1:] + '@123'

            yield _ + '#123'
            yield _.upper() + '#123'
            yield _[0].upper() + _[1:] + '#123'

            yield _ + '@163'
            yield _.upper() + '@163'
            yield _[0].upper() + _[1:] + '@163'

            yield _ + '@666'
            yield _.upper() + '@666'
            yield _[0].upper() + _[1:] + '@666'

            yield _ + '@888'
            yield _.upper() + '@123'
            yield _[0].upper() + _[1:] + '@888'

            yield _ + '@2016'
            yield _.upper() + '@2016'
            yield _[0].upper() + _[1:] + '@2016'

            yield _ + '@2017'
            yield _.upper() + '@2017'
            yield _[0].upper() + _[1:] + '@2017'

            yield _ + '@1q2w3e'
            yield _.upper() + '@1q2w3e'
            yield _[0].upper() + _[1:] + '@1q2w3e'

            yield _ + '!0123'
            yield _.upper() + '!0123'
            yield _[0].upper() + _[1:] + '!0123'

            yield _ + '#0123'
            yield _.upper() + '#0123'
            yield _[0].upper() + _[1:] + '#0123'

            yield _ + '1234'
            yield _.upper() + '1234'
            yield _[0].upper() + _[1:] + '1234'

            yield _ + '2000'
            yield _.upper() + '2000'
            yield _[0].upper() + _[1:] + '2000'

            yield _ + '2016'
            yield _.upper() + '2016'
            yield _[0].upper() + _[1:] + '2016'

            yield _ + '2017'
            yield _.upper() + '2017'
            yield _[0].upper() + _[1:] + '2017'

            yield _ + '12345'
            yield _.upper() + '12345'
            yield _[0].upper() + _[1:] + '12345'

            yield _ + '1q2w3e'
            yield _.upper() + '1q2w3e'
            yield _[0].upper() + _[1:] + '1q2w3e'

            yield '1q2w3e' + _
            yield '1q2w3e_' + _
            yield '1Q2W3E' + _
            yield '1q2w3e4r' + _
            yield '1q2w3e4r_' + _
            yield '1Q2W3E4R' + _
            yield '1q2w3e4r5t' + _
            yield '1Q2W3E4R5T' + _




