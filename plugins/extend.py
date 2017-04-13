#!/usr/bin/env python
# coding:utf-8
# extend_enter raw sensitive string element to possible password
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
import os
import traceback
from lib.fun import finishprinter, finishcounter, cool
from lib.data import get_result_store_path, get_buildtime, operator, CRLF, EXTEND_prefix, filextension, \
    PASSCRAPER_prefix, extend_replace, annotator, build_in_dict_path


def raw_extend(_):
    yield _
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
    yield _ + '.'
    yield _ + '!'
    yield _ + '?'
    yield _ + 's'
    yield '1' + _
    yield '2' + _
    yield '3' + _
    yield '4' + _
    yield '5' + _
    yield '6' + _
    yield '7' + _
    yield '8' + _
    yield '9' + _
    yield 'my' + _
    yield 'qq' + _
    yield 'qq:' + _
    yield 'QQ' + _
    yield 'QQ:' + _
    yield _ + 'qq'
    yield _ + '..'
    yield _ + 'ed'
    yield _ + 'er'
    yield _ + 'or'
    yield _ + 'ing'
    yield _ + 'abc'
    yield _ + 'ABC'
    yield 'abc' + _
    yield 'Abc' + _
    yield _ + 'xyz'
    yield _ + 'XYZ'
    yield _ + '123'
    yield _ + '789'
    yield _ + '520'
    yield _ + '000'
    yield _ + '111'
    yield _ + '666'
    yield _ + '...'
    yield _ + '888'
    yield _ + '!@#'
    yield 'qaz' + _
    yield 'qqq' + _
    yield 'get' + _
    yield 'got' + _
    yield 'win' + _
    yield 'cao' + _
    yield 'fuck' + _
    yield 'Fuck' + _
    yield 'FUCK' + _
    yield 'fucker' + _
    yield 'fucked' + _
    yield 'Fucked' + _
    yield _ + 'fuck'
    yield _ + 'FUCK'
    yield _ + 'fucker'
    yield _ + 'qwer'
    yield _ + 'admin'
    yield 'admin' + _
    yield 'test' + _
    yield 'Test' + _
    yield 'test_' + _
    yield 'tester' + _
    yield 'Tester' + _
    yield _ + '_test'
    yield _ + '_tester'
    yield 'qwer' + _
    yield _ + 'QWER'
    yield 'QWER' + _
    yield 'qwert' + _
    yield 'qwer_' + _
    yield 'QWERT' + _
    yield 'qwerty' + _
    yield 'qazxsw' + _
    yield 'qweasd' + _
    yield 'qwert' + _
    yield _ + '@123'
    yield _ + '#123'
    yield _ + '@163'
    yield _ + '@666'
    yield _ + '@888'
    yield _ + '@2016'
    yield _ + '@2017'
    yield _ + '@1q2w3e'
    yield _ + '!0123'
    yield _ + '#0123'
    yield _ + '1234'
    yield _ + '2000'
    yield _ + '2016'
    yield _ + '2017'
    yield _ + '12345'
    yield _ + '1q2w3e'
    yield '1q2w3e' + _
    yield '1q2w3e_' + _
    yield '1Q2W3E' + _
    yield '1q2w3e4r' + _
    yield '1q2w3e4r_' + _
    yield '1Q2W3E4R' + _
    yield '1q2w3e4r5t' + _
    yield '1Q2W3E4R5T' + _
    if _[-1:] in "aeiou":
        yield _[:-1] + 'ed'
        yield _[:-1] + 'er'
        yield _[:-1] + 'or'
        yield _[:-1] + 'ing'
    else:
        yield _ + 'ed'
        yield _ + 'er'
        yield _ + 'or'
        yield _ + 'ing'


def extend_enter(*args):
    for arg in args:
        for _ in arg:
            _ = _.strip()
            # strange string extend_enter directly
            if not _.isupper() and not _.islower() and not _.isdigit():
                for x in raw_extend(_):
                    yield x
            # other common string replace some str before extend_enter
            for key, value in extend_replace.items():
                if key in _:
                    for x in raw_extend(_.replace(key, value, 1)):
                        yield x
            # raw string distortion
            for x in raw_extend(_.lower()):
                yield x
            for x in raw_extend(_[0].upper() + _[1:]):
                yield x
            for x in raw_extend(_.upper()):
                yield x
            # other
            _ = _.lower()
            yield _ + _.upper()
            yield _[::-1]
            yield _ + _[::-1]
            yield (_[0].upper() + _[1:])[::-1]
            yield _[0:-1] + _[-1:].upper()
            yield (_[0:-1] + _[-1:].upper())[::-1]
            yield _[0].upper() + _[1:] + _[0].upper() + _[1:]


def get_extend_dic(rawlist, encodeflag='none', need_passcratch=False):
    prefix = EXTEND_prefix
    if rawlist == []:
        exit(CRLF + cool.red("[-] raw extend_enter file cannot be empty"))
    if need_passcratch:
        prefix = PASSCRAPER_prefix
    storepath = os.path.join(get_result_store_path(), "%s_%s_%s%s" % (prefix, get_buildtime(), encodeflag, filextension))
    with open(storepath, "a") as f:
        try:
            if need_passcratch:
                with open(os.path.join(build_in_dict_path, 'CommonWebAdminPass.txt'), 'r') as wap:
                    for _ in wap.readlines():
                        if _.strip() != '' and _.strip()[0] != annotator:
                            f.write(operator.get(encodeflag)(str(_).strip() + CRLF))
            for _ in extend_enter(rawlist):
                f.write(operator.get(encodeflag)(str(_) + CRLF))
        except:
            traceback.print_exc()
            exit(CRLF + cool.red("[-] Some error"))
    finishprinter(finishcounter(storepath), storepath)






