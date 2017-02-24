#!/usr/bin/env python
# coding:utf-8
# Personal weak password dictionary
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
import os
from lib.fun import cool
from lib.data import build_in_dict_path, CRLF


# The 20 Most Common Keyboard Patterns
top_20_kb = (
     'qwerty', 'qwertyuiop', '1qaz2wsx', 'qazwsx',
     'asdfgh', 'zxcvbnm', '1234qwer', 'q1w2e3r4t5',
     'qwer1234', 'q1w2e3r4', 'asdfasdf', 'qazwsxedc',
     'asdfghjkl', 'q1w2e3', '1qazxsw2', '12QWaszx',
     'qwerasdzxc', 'mnbvcxz', 'a1b2c3d4', 'adgjmptw'
)

# Others Common Keyboard Patterns
other_char_kb = ('qwertyuiop', 'poiuytrewq', 'lkjhgfdsa', 'asdfghjkl', 'abcabc')

# Common Weak password
usual_weak_pass = (
    '123456', '123456789', '0',  '111111',
    '123123', '5201314', 'woaini1314', '1314520',
    '7758521', 'woaini', 'iloveyou', 'woaini520',
    '88888888', '666666'
)

# 25 Worst Passwords
worst_25_pass = (
    '123456', 'password', '12345678', 'qwerty',
    'abc123', '123456789', '11111', '1234567',
    'iloveyou', 'adobe123', '123123', 'admin',
    '1234567890', 'letmein', 'photoshop', '1234',
    'monkey', 'shadow', 'sunshine', '12345',
    'password1', 'princess', 'azerty', 'trustno1',
    '000000'
)

# IT youth weak password
ITpass = (
    '123456789', '12345678', '11111111', 'dearbook',
    '00000000', '123123123', '1234567890', '88888888',
    '111111111', '147258369', '987654321', 'aaaaaaaa',
    '1111111111', '66666666', 'a123456789', '11223344',
    '1qaz2wsx', 'xiazhili', '789456123', 'qqqqqqqq',
    '000000000', '3.1415926', '3_1415926'
)

weakpass101_list = []
weakpass101 = os.path.join(build_in_dict_path, "Weakpass101")
if os.path.isfile(weakpass101):
    try:
        with open(weakpass101) as f:
            for _ in f.readlines():
                weakpass101_list.append(_)
    except IOError as ex:
        exit(cool.red("[-] Weakpass101.txt operator error") + CRLF + ex.message)

joinall = top_20_kb + other_char_kb + usual_weak_pass + worst_25_pass + ITpass + tuple(weakpass101_list)
weak_pass_set = set(joinall)
