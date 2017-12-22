#!/usr/bin/env python
# coding:utf-8
# author: LandGrey
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""
from __future__ import unicode_literals

import os
import time
import string
from lib.fun.fun import cool
from collections import Counter
from lib.fun.decorator import magic
from lib.data.data import pystrs, pyoptions


def counter_operator(original_file_path, justsave, justview, vs_count=pyoptions.default_vs_items):
    items = Counter(open(original_file_path, 'r').read().replace(string.punctuation, "").
                    split(pyoptions.counter_split)).most_common(vs_count)
    items_length = len(items)
    if vs_count > pyoptions.vs_counter_switcher:
        exit(pyoptions.CRLF + cool.fuchsia("[!] view items should Leq {0}".format(pyoptions.vs_counter_switcher)))
    elif items_length < vs_count:
        exit(pyoptions.CRLF + cool.fuchsia("[!] max items is {0}".format(items_length)))

    if justsave:
        @magic
        def counter():
            for _ in items:
                yield _[0]
    elif justview:
        print(pyoptions.CRLF * 2)
        for item in items:
            print("{0}Word:{2:20} -> {1:10} times".format("     "*5, cool.orange(item[1]), cool.orange(item[0])))
        print("[+] Cost:{} seconds".format(cool.orange(str(time.time() - pystrs.startime)[:6])))
    else:
        print(pyoptions.CRLF * 2)
        for item in items:
            print("{0}Word:{2:20} -> {1:10} times".format("     "*5, cool.orange(item[1]), cool.orange(item[0])))

        @magic
        def counter():
            for _ in items:
                yield _[0]


def counter_magic(*args):
    """['v','s','vs'] [file] [view_num]"""
    args = list(args[0])

    # counter lack file argument
    if len(args) == 2 and args[1] in pystrs.counter_cmd_range:
        exit(pyoptions.CRLF + cool.red("[-] {0} need specify the file path".format(pyoptions.tool_range[2])))
    # counter
    elif len(args) >= 3:
        if args[1] not in pystrs.counter_cmd_range:
            exit(pyoptions.CRLF + cool.red("[-] Need {0}'s options, choose from '{1}' or '{2}' or '{3}'".format(
                args[0], pystrs.counter_cmd_range[0], pystrs.counter_cmd_range[1], pystrs.counter_cmd_range[2])))
        if os.path.isfile(args[2]):
            # counter s file
            if len(args) == 3 and args[1] == pystrs.just_save_counter:
                counter_operator(args[2], True, False)
            # counter v file
            elif len(args) == 3 and args[1] == pystrs.just_view_counter:
                counter_operator(args[2], False, True)
            # counter vs file
            elif len(args) == 3 and args[1] == pystrs.save_and_view:
                counter_operator(args[2], False, False)
            # counter v file 100
            elif len(args) == 4 and args[1] == pystrs.just_view_counter and str(args[3]).isdigit():
                counter_operator(args[2], False, True,  vs_count=int(args[3]))
            # counter s file 100
            elif len(args) == 4 and args[1] == pystrs.just_save_counter and str(args[3]).isdigit():
                counter_operator(args[2], True, False, vs_count=int(args[3]))
            # counter vs file 100
            elif len(args) == 4 and args[1] == pystrs.save_and_view and str(args[3]).isdigit():
                counter_operator(args[2], False, False, vs_count=int(args[3]))
            else:
                exit(pyoptions.CRLF + cool.red("[-] Some unexpected input"))


        else:
            exit(pyoptions.CRLF + cool.red("[-] File: %s not exists" % args[2]))
    else:
        exit(pyoptions.CRLF + cool.fuchsia("[!] Usage: {} {}".format(args[0], pyoptions.tools_info.get(args[0]))))
