#!/usr/bin/env python
# coding:utf-8
# some simple function for others import
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from lib.data import *
from lib.shreder import shreder_file, shreder_dir


def finishprinter(count, storepath):
    print "[+] A total of %s lines%s" % (str(count), CRLF) +\
          "[+] Store in %s " % storepath


def lengthchecker(minlen, maxlen):
    if str(minlen).isdigit() and str(maxlen).isdigit():
        if int(minlen) <= int(maxlen):
            if int(maxlen) > maxlen_switcher:
                print CRLF + '[-] Make sure that: maxlen <= %s' % maxlen_switcher
                exit()
            else:
                pass
        else:
            print CRLF + '[-] Make sure that: minlen <= maxlen'
            exit()
    else:
        print CRLF + '[-] Make sure that: minlen and maxlen is digital'
        exit()


def countchecker(charslength, *args):
    count_check = 0
    # chunk
    if len(args) == 0:
        if reduce(lambda a, b: a*b, range(1, charslength + 1)) > count_switcher:
            print "[!] Build items more than count_switcher: %s" % str(count_switcher)
            exit()
    # conf
    elif len(args) == 1 and charslength == -1:
        if args[0] > count_switcher:
            print "[!] Build items more than count_switcher: %s" % str(count_switcher)
            exit()
    # conf
    elif len(args) == 2 and charslength == -1:
        if args[0] * args[1] > count_switcher:
            print "[!] Build items more than count_switcher: %s" % str(count_switcher)
            exit()
    # base
    elif len(args) == 2 and charslength != -1:
        for _ in range(args[0], args[1] + 1):
            count_check += pow(charslength, _)
        if count_check > count_switcher:
            print "[!] Build items more than count_switcher: %s" % str(count_switcher)
            exit()
    # conf
    elif len(args) >= 3 and charslength == -1:
        allitems = 1
        for x in range(len(args)):
            allitems *= args[x]
        if allitems > count_switcher:
            print "[!] Build items more than count_switcher: %s" % str(count_switcher)
            exit()


def cleaner(*args):
    _ = "".join(args)
    if _ and os.path.isdir(_):
        shreder_dir(_)
    elif _ and os.path.exists(_):
        shreder_file(_)
    elif _ and _.upper() in prefix_range:
        for filename in os.listdir(get_result_store_path()):
            if _.upper() in str(filename[0:6]).upper():
                shreder_file(os.path.join(result_store_path, filename))
    else:
        print '[-] invalid clean arguments'
        exit()