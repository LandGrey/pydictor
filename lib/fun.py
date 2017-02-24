#!/usr/bin/env python
# coding:utf-8
# Store some simple functions for others module to import
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
import os
import time
import platform
from functools import reduce
from lib.data import CRLF, maxlen_switcher, count_switcher, startime


# judge run platform
def is_Windows():
    return platform.system() == "Windows"


def is_Linux():
    return platform.system() == "Linux"


def is_Mac():
    return platform.system() == "Darwin"


# Windows 10 (v1511) Adds Support for ANSI Escape Sequences
def is_higher_win10_v1511():
    if is_Windows():
        try:
            if int(platform.version().split('.')[0]) >= 10 and int(platform.version().split('.')[-1]) >= 1511:
                return True
            else:
                return False
        except:
            return False


# text highlight
class Colored(object):
    if is_Windows():
        os.system("color")
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    ORANGE = '\033[0;33;1m'
    BLUE = '\033[34m'
    FUCHSIA = '\033[35m'
    WHITE = '\033[37m'

    #: no color
    RESET = '\033[0m'

    def color_str(self, color, s):
        if is_higher_win10_v1511() or is_Linux() or is_Mac():
            return '{}{}{}'.format(getattr(self, color), s, self.RESET)
        else:
            return '{}'.format(s)

    def red(self, s):
        return self.color_str('RED', s)

    def green(self, s):
        return self.color_str('GREEN', s)

    def yellow(self, s):
        return self.color_str('YELLOW', s)

    def orange(self, s):
        return self.color_str('ORANGE', s)

    def blue(self, s):
        return self.color_str('BLUE', s)

    def fuchsia(self, s):
        return self.color_str('FUCHSIA', s)

    def white(self, s):
        return self.color_str('WHITE', s)

cool = Colored()


def finishprinter(count, storepath):
    print("[+] A total of :{0} lines{1}"
          "[+] Store in   :{2} {1}"
          "[+] Cost       :{3} seconds".format(cool.orange(str(count)), CRLF, cool.orange(storepath),
                                               cool.orange(str(time.time() - startime)[:6])))


def finishcounter(storepath):
    line_count = 0
    with open(storepath, 'r') as files:
        for _ in files:
            line_count += 1
    return line_count


# python version egt 3
def py_ver_egt_3():
    if int(platform.python_version()[0]) >= 3:
        return True


def range_compatible(minlength, maxlength_plus_one):
    if py_ver_egt_3():
        return range(minlength, maxlength_plus_one)
    else:
        return xrange(minlength, maxlength_plus_one)


def lengthchecker(minlen, maxlen):
    if str(minlen).isdigit() and str(maxlen).isdigit():
        if int(minlen) <= int(maxlen):
            if int(maxlen) > maxlen_switcher:
                exit(CRLF + cool.red("[-] Ensure that: maxlen <= %s" % maxlen_switcher))
            else:
                pass
        else:
            exit(CRLF + cool.red("[-] Ensure that: minlen <= maxlen"))
    else:
        exit(CRLF + cool.red("[-] Make sure that: minlen and maxlen is digital"))


def countchecker(charslength, *args):
    count_check = 0
    # chunk
    if len(args) == 0:
        if reduce(lambda a, b: a*b, range_compatible(1, charslength + 1)) > count_switcher:
            exit(CRLF + cool.fuchsia("[!] Build items more than count_switcher: %s" % str(count_switcher)))
    # conf
    elif len(args) == 1 and charslength == -1:
        if args[0] > count_switcher:
            exit(CRLF + cool.fuchsia("[!] Build items more than count_switcher: %s" % str(count_switcher)))
    # conf
    elif len(args) == 2 and charslength == -1:
        if args[0] * args[1] > count_switcher:
            exit(CRLF + cool.fuchsia("[!] Build items more than count_switcher: %s" % str(count_switcher)))
    # base
    elif len(args) == 2 and charslength != -1:
        for _ in range_compatible(args[0], args[1] + 1):
            count_check += pow(charslength, _)
        if count_check > count_switcher:
            exit(CRLF + cool.fuchsia("[!] Build items more than count_switcher: %s" % str(count_switcher)))
    # conf
    elif len(args) >= 3 and charslength == -1:
        allitems = 1
        for x in range_compatible(0, len(args)):
            allitems *= args[x]
        if allitems > count_switcher:
            exit(CRLF + cool.fuchsia("[!] Build items more than count_switcher: %s" % str(count_switcher)))
