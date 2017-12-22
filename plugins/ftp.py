#!/usr/bin/env python
# coding:utf-8
# author: LandGrey
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

from lib.fun.fun import cool
from lib.fun.decorator import magic
from lib.data.data import pyoptions


def ftp_magic(*args):
    """[keyword1] [keyword2] ..."""
    args = list(args[0])
    if len(args) == 1:
        exit(pyoptions.CRLF + cool.fuchsia("[!] Usage: {} {}".format(args[0], pyoptions.plugins_info.get(args[0]))))

    @magic
    def ftp():
        results = []
        default_password = ('ftp', 'anonymous', 'any@', 'craftpw', 'xbox', 'r@p8p0r+', 'pass', 'admin',
                            'lampp', 'password', 'Exabyte', 'pbxk1064', 'kilo1987', 'help1954', 'tuxalize')
        results += default_password
        weak_password = ('root', '123456', '111111', '666666', 'ftppass')
        results += weak_password
        for r in results:
            yield r

        tails = ['1', '01', '001', '123', 'abc', '!@#', '!QAZ', '1q2w3e', '!@#$', '!', '#', '.', '@123',
                 '2016', '2017', '2018', '@2016', '@2017', '@2018', ]
        for keyword in args:
            for tail in tails:
                yield keyword + tail
