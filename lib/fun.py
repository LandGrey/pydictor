#!/usr/bin/env python
# coding:utf-8
# some simple function for others import
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
import os
import platform
from functools import reduce
from lib.data import CRLF, maxlen_switcher, count_switcher


# judge run platform
# windows return 'Windows' and linux  return 'Linux'
def is_Windows():
    return platform.system() == "Windows"


def is_Linux():
    return platform.system() == "Linux"


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
        return '{}{}{}'.format(
            getattr(self, color),
            s,
            self.RESET
        )

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
    print("[+] A total of {0} lines{1}[+] Store in {2}".format(cool.orange(str(count)), CRLF, cool.orange(storepath)))


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


def range_compatible(minlength, maxlength_large_one):
    if py_ver_egt_3():
        return range(minlength, maxlength_large_one)
    else:
        return xrange(minlength, maxlength_large_one)


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
        if reduce(lambda a, b: a*b, range(1, charslength + 1)) > count_switcher:
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
        for _ in range(args[0], args[1] + 1):
            count_check += pow(charslength, _)
        if count_check > count_switcher:
            exit(CRLF + cool.fuchsia("[!] Build items more than count_switcher: %s" % str(count_switcher)))
    # conf
    elif len(args) >= 3 and charslength == -1:
        allitems = 1
        for x in range(len(args)):
            allitems *= args[x]
        if allitems > count_switcher:
            exit(CRLF + cool.fuchsia("[!] Build items more than count_switcher: %s" % str(count_switcher)))
