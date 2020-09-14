#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import os
import time
import string
import locale
import traceback
from functools import reduce
from lib.fun.color import Colored
from lib.fun.osjudger import py_ver_egt_3
from lib.data.data import pystrs,  paths, pyoptions

cool = Colored()


# order preserving
def unique(seq, idfun=None):
    if idfun is None:
        def idfun(x): return x
    seen = {}
    results = []
    for item in seq:
        marker = idfun(item)
        if marker in seen:
            continue
        seen[marker] = 1
        results.append(item)
    return results


def rreplace(self, old, new, *max):
    count = len(self)
    if max and str(max[0]).isdigit():
        count = max[0]
    return new.join(self.rsplit(old, count))


def charanger(confstr):
    ranges = []
    for i in range(len(confstr.split(pyoptions.chars_split))):
        if os.path.isfile(confstr.split(pyoptions.chars_split)[i]):
            with open(confstr.split(pyoptions.chars_split)[i], 'r') as f:
                for line in f.readlines():
                    ranges.append(line.strip())
        elif pyoptions.char_range_split in confstr.split(pyoptions.chars_split)[i] and \
                        len(confstr.split(pyoptions.chars_split)[i].split(pyoptions.char_range_split)) == 2:
            start = confstr.split(pyoptions.chars_split)[i].split(pyoptions.char_range_split)[0]
            end = confstr.split(pyoptions.chars_split)[i].split(pyoptions.char_range_split)[1]
            for c in string.printable:
                if start <= c <= end:
                    ranges.append(c.strip())
        else:
            ranges.append(str(confstr.split(pyoptions.chars_split)[i]).strip())
    return ranges


def walks_all_files(directory):
    contents = []
    for _ in get_subdir_files_path(directory):
        with open(_, 'r') as f:
            for line in f.readlines():
                if line.strip() != '' and line.strip()[0] != pyoptions.annotator:
                    contents.append(line.strip())
    return unique(contents)


def walk_pure_file(filepath, pure=True):
    results = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if pure:
                if line.strip() != '':
                    results.append(line.strip())
            else:
                if line.strip() != '' and line.strip()[0] != pyoptions.annotator:
                    results.append(line.strip())
    return unique(results)


def get_subdir_files_path(directory, only_file_path=True):
    dirpaths = []
    filepaths = []
    for rootpath, subdirsname, filenames in os.walk(directory):
        dirpaths.extend([os.path.abspath(os.path.join(rootpath, _)) for _ in subdirsname])
        filepaths.extend([os.path.abspath(os.path.join(rootpath, _)) for _ in filenames])
    if only_file_path:
        return filepaths
    else:
        return dirpaths, filepaths


def range_compatible(minlength, maxlength_plus_one):
    if py_ver_egt_3():
        return range(minlength, maxlength_plus_one)
    else:
        return xrange(minlength, maxlength_plus_one)


def lengthchecker(minlen, maxlen, sedb=False):
    if str(minlen).isdigit() and str(maxlen).isdigit():
        if int(minlen) <= int(maxlen):
            if int(maxlen) > pyoptions.maxlen_switcher:
                if not sedb:
                    exit(pyoptions.CRLF + cool.red("[-] Ensure maxlen <= %s" % pyoptions.maxlen_switcher))
                else:
                    print(cool.fuchsia("[!] Ensure maxlen <= %s%s"
                                       "[!] Modify /lib/data/data.py maxlen_switcher to adjust it" %
                                       (pyoptions.maxlen_switcher, pyoptions.CRLF) + pyoptions.CRLF))
                    return False
            else:
                return True
        else:
            if not sedb:
                exit(pyoptions.CRLF + cool.red("[-] Ensure minlen <= maxlen"))
            else:
                print(cool.fuchsia("[!] Ensure minlen <= maxlen") + pyoptions.CRLF)
                return False
    else:
        if not sedb:
            exit(pyoptions.CRLF + cool.red("[-] Make sure minlen and maxlen is digit"))
        else:
            print(cool.fuchsia("[!] Make sure minlen and maxlen is digit") + pyoptions.CRLF)
            return False


def countchecker(charslength, *args):
    count_check = 0
    exit_msg = pyoptions.CRLF + cool.fuchsia("[!] Build items more than pyoptions.count_switcher: %s%s"
                                             "[!] Modify /lib/data/data.py count_switcher to adjust it" %
                                             (str(pyoptions.count_switcher), pyoptions.CRLF))
    # chunk
    if len(args) == 0:
        if reduce(lambda a, b: a*b, range_compatible(1, charslength + 1)) > pyoptions.count_switcher:
            exit(exit_msg)
    # conf
    elif len(args) == 1 and charslength == -1:
        if args[0] > pyoptions.count_switcher:
            exit(exit_msg)
    # conf
    elif len(args) == 2 and charslength == -1:
        if args[0] * args[1] > pyoptions.count_switcher:
            exit(exit_msg)
    # base
    elif len(args) == 2 and charslength != -1:
        for _ in range_compatible(args[0], args[1] + 1):
            count_check += pow(charslength, _)
        if count_check > pyoptions.count_switcher:
            exit(exit_msg)
    # conf
    elif len(args) >= 3 and charslength == -1:
        allitems = 1
        for x in range_compatible(0, len(args)):
            allitems *= args[x]
        if allitems > pyoptions.count_switcher:
            exit(exit_msg)


def fun_name(isfun=False):
    stack = traceback.extract_stack()
    script_path, code_line, func_name, text = stack[-2]
    script_name = os.path.split(script_path)[1][:-3]
    if isfun:
        return func_name
    else:
        return script_name


def is_en():
    return "en" in locale.getdefaultlocale()[0].lower()


def mybuildtime():
    return str(time.strftime("%H%M%S", time.localtime(time.time())))


def finishcounter(storepath):
    line_count = 0
    with open(storepath, 'r') as files:
        for _ in files:
            line_count += 1
    return line_count


def finishprinter(storepath, count=None):
    if not count:
        count = finishcounter(storepath)
    print("[+] A total of :{0:} lines{1}"
          "[+] Store in   :{2} {1}"
          "[+] Cost       :{3} seconds".format(cool.orange(count), pyoptions.CRLF, cool.orange(storepath),
                                               cool.orange(str(time.time() - pystrs.startime)[:6])))


def finalsavepath(prefix):
    directory = paths.results_path
    timestamp = mybuildtime()
    ext = pyoptions.filextension
    customname = paths.results_file_name
    filename = "%s_%s%s" % (prefix.lower(), timestamp, ext)
    filename = filename if not customname else customname
    storepath = os.path.join(directory, filename)
    return storepath
