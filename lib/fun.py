#!/usr/bin/env python
# coding:utf-8
# some simple function for others import
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
from functools import reduce
import os
from lib.data import CRLF, maxlen_switcher, count_switcher, prefix_range, get_result_store_path
from lib.shreder import shreder_file, shreder_dir


def finishprinter(count, storepath):
    print("[+] A total of %s lines%s[+] Store in %s" % (str(count), CRLF, storepath))


def finishcounter(storepath):
    line_count = 0
    with open(storepath, 'r') as files:
        for _ in files:
            line_count += 1
    return line_count


def lengthchecker(minlen, maxlen):
    if str(minlen).isdigit() and str(maxlen).isdigit():
        if int(minlen) <= int(maxlen):
            if int(maxlen) > maxlen_switcher:
                exit(CRLF + "[-] Ensure that: maxlen <= %s" % maxlen_switcher)
            else:
                pass
        else:
            exit(CRLF + "[-] Ensure that: minlen <= maxlen")
    else:
        exit(CRLF + "[-] Make sure that: minlen and maxlen is digital")


def countchecker(charslength, *args):
    count_check = 0
    # chunk
    if len(args) == 0:
        if reduce(lambda a, b: a*b, range(1, charslength + 1)) > count_switcher:
            exit(CRLF + "[!] Build items more than count_switcher: %s" % str(count_switcher))
    # conf
    elif len(args) == 1 and charslength == -1:
        if args[0] > count_switcher:
            exit(CRLF + "[!] Build items more than count_switcher: %s" % str(count_switcher))
    # conf
    elif len(args) == 2 and charslength == -1:
        if args[0] * args[1] > count_switcher:
            exit(CRLF + "[!] Build items more than count_switcher: %s" % str(count_switcher))
    # base
    elif len(args) == 2 and charslength != -1:
        for _ in range(args[0], args[1] + 1):
            count_check += pow(charslength, _)
        if count_check > count_switcher:
            exit(CRLF + "[!] Build items more than count_switcher: %s" % str(count_switcher))
    # conf
    elif len(args) >= 3 and charslength == -1:
        allitems = 1
        for x in range(len(args)):
            allitems *= args[x]
        if allitems > count_switcher:
            exit(CRLF + "[!] Build items more than count_switcher: %s" % str(count_switcher))


def cleaner(*args):
    _ = "".join(args)
    if _ and os.path.isdir(_):
        shreder_dir(_)
    elif _ and os.path.exists(_):
        shreder_file(_)
    elif _ and _.upper() in prefix_range:
        for filename in os.listdir(get_result_store_path()):
            if _.upper() in str(filename[0:6]).upper():
                shreder_file(os.path.join(get_result_store_path(), filename))
    else:
        exit(CRLF + "[-] invalid clean arguments")
